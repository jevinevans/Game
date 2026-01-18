from __future__ import annotations

import random
import sys
from dataclasses import dataclass, field
from typing import Optional, Tuple

# =========================
# Models / State
# =========================


@dataclass
class Player:
    name: str
    hp: int
    max_hp: int
    attack: int
    defense: int
    has_key: bool = False


@dataclass
class Enemy:
    name: str
    hp: int
    max_hp: int
    attack: int
    defense: int


@dataclass
class CombatState:
    enemy: Enemy
    turn: str  # "player" or "enemy"
    log: list[str] = field(default_factory=list)


@dataclass
class LevelState:
    grid: list[list[str]]
    width: int
    height: int
    player_pos: Tuple[int, int]
    key_pos: Tuple[int, int]
    boss_pos: Tuple[int, int]


@dataclass
class GameState:
    mode: str  # "explore" or "combat" or "game_over"
    level: LevelState
    player: Player
    combat: Optional[CombatState] = None
    message: str = ""


# =========================
# Level / Initialization
# =========================


def create_level() -> LevelState:
    # Simple bordered room with key (K) and boss (B)
    raw = [
        "##########",
        "#..K.....#",
        "#........#",
        "#.....B..#",
        "##########",
    ]
    grid = [list(row) for row in raw]
    height = len(grid)
    width = len(grid[0])

    # Find positions
    key_pos = None
    boss_pos = None
    player_pos = (2, 2)  # starting position (row, col)

    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == "K":
                key_pos = (y, x)
            elif ch == "B":
                boss_pos = (y, x)

    if key_pos is None or boss_pos is None:
        raise ValueError("Level must contain K and B")

    return LevelState(
        grid=grid,
        width=width,
        height=height,
        player_pos=player_pos,
        key_pos=key_pos,
        boss_pos=boss_pos,
    )


def initial_game_state() -> GameState:
    level = create_level()
    player = Player(
        name="Hero",
        hp=20,
        max_hp=20,
        attack=6,
        defense=2,
    )
    return GameState(
        mode="explore",
        level=level,
        player=player,
        combat=None,
        message="Find the key (K) and face the boss (B).",
    )


# =========================
# Engine: Movement / Exploration
# =========================


def movement_delta(intent: str) -> Tuple[int, int]:
    intent = intent.lower()
    if intent in ("w", "up"):
        return -1, 0
    if intent in ("s", "down"):
        return 1, 0
    if intent in ("a", "left"):
        return 0, -1
    if intent in ("d", "right"):
        return 0, 1
    return 0, 0


def is_walkable(level: LevelState, y: int, x: int) -> bool:
    if y < 0 or y >= level.height or x < 0 or x >= level.width:
        return False
    tile = level.grid[y][x]
    return tile != "#"


def apply_movement(level: LevelState, dy: int, dx: int) -> Tuple[int, int]:
    y, x = level.player_pos
    new_y = y + dy
    new_x = x + dx
    if is_walkable(level, new_y, new_x):
        return new_y, new_x
    return y, x


def collect_key(state: GameState) -> GameState:
    state.player.has_key = True
    state.message = "You picked up the key!"
    # Optionally remove key from grid
    ky, kx = state.level.key_pos
    state.level.grid[ky][kx] = "."
    return state


def enter_combat(state: GameState, enemy_type: str) -> GameState:
    if enemy_type == "boss":
        enemy = Enemy(name="Dungeon Boss", hp=25, max_hp=25, attack=7, defense=3)
    else:
        enemy = Enemy(name="Goblin", hp=12, max_hp=12, attack=4, defense=1)

    state.mode = "combat"
    state.combat = CombatState(
        enemy=enemy, turn="player", log=["A wild {} appears!".format(enemy.name)]
    )
    state.message = "Combat started!"
    return state


def exit_combat(state: GameState, victory: bool) -> GameState:
    if victory:
        state.message = f"You defeated {state.combat.enemy.name}!"
        # If boss defeated, you win the game
        if state.combat.enemy.name == "Dungeon Boss":
            state.mode = "game_over"
            state.message = "You defeated the boss and cleared the dungeon!"
        else:
            state.mode = "explore"
    else:
        state.mode = "game_over"
        state.message = "You were defeated..."
    state.combat = None
    return state


def update_exploration(state: GameState, intent: str) -> GameState:
    dy, dx = movement_delta(intent)
    if dy == 0 and dx == 0:
        # Non-movement intent in explore mode
        if intent.lower() in ("q", "quit", "exit"):
            state.mode = "game_over"
            state.message = "You quit the game."
        else:
            state.message = "Use WASD to move, or 'q' to quit."
        return state

    new_y, new_x = apply_movement(state.level, dy, dx)
    state.level.player_pos = (new_y, new_x)

    # Check interactions
    if (new_y, new_x) == state.level.key_pos and not state.player.has_key:
        state = collect_key(state)

    if (new_y, new_x) == state.level.boss_pos:
        if state.player.has_key:
            state = enter_combat(state, "boss")
        else:
            state.message = "The boss blocks your way. You need the key first."

    return state


# =========================
# Engine: Combat
# =========================


def calc_damage(attack: int, defense: int) -> int:
    base = attack - defense
    dmg = max(1, base + random.randint(-1, 2))
    return max(0, dmg)


def player_attack(state: GameState) -> GameState:
    dmg = calc_damage(state.player.attack, state.combat.enemy.defense)
    state.combat.enemy.hp = max(0, state.combat.enemy.hp - dmg)
    state.combat.log.append(f"You attack {state.combat.enemy.name} for {dmg} damage.")
    return state


def enemy_attack(state: GameState) -> GameState:
    dmg = calc_damage(state.combat.enemy.attack, state.player.defense)
    state.player.hp = max(0, state.player.hp - dmg)
    state.combat.log.append(f"{state.combat.enemy.name} hits you for {dmg} damage.")
    return state


def player_defend(state: GameState) -> GameState:
    # Simple defend: reduce next enemy damage by half (handled inline)
    state.combat.log.append("You brace yourself for the next attack.")
    dmg = calc_damage(state.combat.enemy.attack, state.player.defense + 3)
    state.player.hp = max(0, state.player.hp - dmg)
    state.combat.log.append(f"{state.combat.enemy.name} hits you for {dmg} damage (reduced).")
    return state


def update_combat(state: GameState, intent: str) -> GameState:
    if state.combat is None:
        return state

    intent = intent.lower().strip()

    if intent in ("1", "attack", "a"):
        state = player_attack(state)
    elif intent in ("2", "defend", "d"):
        state = player_defend(state)
    elif intent in ("3", "run", "r"):
        # Simple run chance
        if random.random() < 0.5:
            state.combat.log.append("You successfully ran away!")
            return exit_combat(state, victory=False)
        else:
            state.combat.log.append("You failed to run away!")
            state = enemy_attack(state)
            if state.player.hp <= 0:
                return exit_combat(state, victory=False)
            return state
    else:
        state.combat.log.append("Invalid action. Choose 1, 2, or 3.")
        return state

    # Check enemy defeat
    if state.combat.enemy.hp <= 0:
        return exit_combat(state, victory=True)

    # Enemy turn (if still alive)
    state = enemy_attack(state)

    # Check player defeat
    if state.player.hp <= 0:
        return exit_combat(state, victory=False)

    return state


# =========================
# Engine: Dispatcher
# =========================


def update_game(state: GameState, intent: str) -> GameState:
    if state.mode == "explore":
        return update_exploration(state, intent)
    elif state.mode == "combat":
        return update_combat(state, intent)
    else:
        return state


# =========================
# UI: Rendering
# =========================


def render_level(state: GameState) -> None:
    level = state.level
    y_p, x_p = level.player_pos

    print("\n=== Dungeon Level ===")
    for y in range(level.height):
        row_chars = []
        for x in range(level.width):
            if (y, x) == (y_p, x_p):
                row_chars.append("P")
            else:
                row_chars.append(level.grid[y][x])
        print("".join(row_chars))
    print()
    print(
        f"Player HP: {state.player.hp}/{state.player.max_hp}  Key: {'Yes' if state.player.has_key else 'No'}"
    )
    if state.message:
        print(state.message)


def render_combat(state: GameState) -> None:
    c = state.combat
    print("\n=== Combat ===")
    print(f"Enemy: {c.enemy.name}")
    print(f"Enemy HP: {c.enemy.hp}/{c.enemy.max_hp}")
    print(f"Player HP: {state.player.hp}/{state.player.max_hp}")
    print()
    if c.log:
        for line in c.log[-4:]:
            print(line)
    print()
    print("Choose action:")
    print("[1] Attack")
    print("[2] Defend")
    print("[3] Run")


def render_game_over(state: GameState) -> None:
    print("\n=== Game Over ===")
    print(state.message)
    print("Thanks for playing.")


def render(state: GameState) -> None:
    if state.mode == "explore":
        render_level(state)
    elif state.mode == "combat":
        render_combat(state)
    elif state.mode == "game_over":
        render_game_over(state)


# =========================
# UI: Input
# =========================


def get_player_intent(state: GameState) -> str:
    if state.mode == "explore":
        return input("\nMove (WASD) or 'q' to quit: ").strip()
    elif state.mode == "combat":
        return input("Action (1/2/3): ").strip()
    else:
        return ""


# =========================
# Main Loop
# =========================


def main() -> None:
    random.seed()
    state = initial_game_state()

    while True:
        render(state)
        if state.mode == "game_over":
            break
        intent = get_player_intent(state)
        state = update_game(state, intent)

    # Final render to show game over message
    render(state)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
