"""
Description: This defines the turn based combat system for FUNCLG
Developer: Jevin Evans
Date: 1.17.2026
"""

import random

from funclg.game.models import GameState
from funclg.game.movement import exit_combat


# TODO: 2026.01.17 - Refactor to use character stats and abilities
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
