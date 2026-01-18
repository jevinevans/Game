"""
Description: Defins movement functions for the game
Developer: Jevin Evans
Date: 1.17.2026
"""

from typing import Tuple

from funclg.character.character import NonPlayableCharacter
from funclg.game.models import CombatState, GameState, LevelState
from funclg.utils.game_enums import GameAction


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
    if y < 0 or y >= level.level_size or x < 0 or x >= level.level_size:
        return False
    tile = level.level[y * level.level_size + x]
    return tile != "#"


def apply_movement(level: LevelState, dy: int, dx: int) -> Tuple[int, int]:
    y, x = level.player_pos
    new_y = y + dy
    new_x = x + dx
    if is_walkable(level, new_y, new_x):
        return new_y, new_x
    return y, x


def collect_key(state: GameState) -> GameState:
    state.has_key = True
    state.message = "You picked up the key!"
    # Optionally remove key from grid
    ky, kx = state.level.key_pos
    state.level.level[ky * state.level.level_size + kx] = "."
    return state


# TODO: 2026.01.17 - Update enemy to use list of predefined enemies
def enter_combat(state: GameState, enemy_type: str) -> GameState:
    if enemy_type == "boss":
        enemy = Enemy(name="Dungeon Boss", hp=25, max_hp=25, attack=7, defense=3)
    else:
        enemy = Enemy(name="Goblin", hp=12, max_hp=12, attack=4, defense=1)

    state.mode = GameAction.COMBAT
    state.combat = CombatState(enemy=enemy, turn="player", log=[f"A wild {enemy.name} appears!"])
    state.message = "Combat started!"
    return state


def exit_combat(state: GameState, victory: bool) -> GameState:
    if victory:
        state.message = f"You defeated {state.combat.enemy.name}!"
        # If boss defeated, you win the game
        if state.combat.enemy.name == "Dungeon Boss":
            state.mode = GameAction.WIN
            state.message = "You defeated the boss and cleared the dungeon!"
        else:
            state.mode = GameAction.EXPLORE
    else:
        state.mode = GameAction.LOSE
        state.message = "You were defeated..."
    state.combat = None
    return state


def update_exploration(state: GameState, intent: str) -> GameState:
    dy, dx = movement_delta(intent)
    if dy == 0 and dx == 0:
        # Non-movement intent in explore mode
        if intent.lower() in ("q", "quit", "exit"):
            state.mode = GameAction.GAME_OVER
            state.message = "You quit the game."
        else:
            state.message = "Use WASD to move, or 'q' to quit."
        return state

    new_y, new_x = apply_movement(state.level, dy, dx)
    state.level.player_pos = (new_y, new_x)

    # Check interactions
    if (new_y, new_x) == state.level.key_pos and not state.has_key:
        state = collect_key(state)

    if (new_y, new_x) == state.level.boss_pos:
        if state.has_key:
            state = enter_combat(state, "boss")
        else:
            state.message = "The boss blocks your way. You need the key first."

    return state
