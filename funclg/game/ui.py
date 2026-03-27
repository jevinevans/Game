"""
Description: This module handles the rendering of the game UI
Developer: Jevin Evans
Date: 1.17.2026
"""

# =========================
# UI: Rendering
# =========================

from funclg.game.models import GameState
from funclg.utils.game_enums import GameAction


# TODO: 2026.01.17 - Add more player stats/info
def render_level(state: GameState) -> None:
    level = state.level
    y_p, x_p = level.player_pos

    print("\n=== Dungeon Level ===")
    for y in range(level.level_size):
        row_chars = []
        for x in range(level.level_size):
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
    if state.mode == GameAction.EXPLORE:
        render_level(state)
    elif state.mode == GameAction.COMBAT:
        render_combat(state)
    elif state.mode == GameAction.GAME_OVER:
        render_game_over(state)
