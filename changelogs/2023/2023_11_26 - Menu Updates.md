# FUN Command Line Game Log: 11.26.2023 - 11.27.2023 
<!-- Update: Current Log date -->

Last Updated: 11.27.2023 <!-- Update with previous log date -->
Version: 0.6.2
<!-- Update version number when changes made-->
<!-- Verions Additions 
  + 1.0.0 is for major project wide changes like adding a whole new concept/face change
    + V1 = MVP CLI version of game
    + V2 = integration of Textual package and any visiualization features
  + 0.1.0 is for current feature version updates including additions/removal/revamp of methods or parts (general idea of things)
  + 0.0.1 is for minor changes including: bug fixes, additions to current methods
 -->

## MOTD - 11.5.2023
-------------------


## Changes
------------------------------

### Added

- Added a menu to game_managers
- Added testing coverage for menu_funcs
- Added questionary functionality to menus (closes #107)
- Update settings managers to include character and game specific menus (closes #122)

### Fixed

### Informational


------------------------------


# Long Term Priority
---------------------------
- Manager Menu's
  - Split into different modules for game data and character data
  
- Level manager and creation process
  - Enemy/Boss generation
  - level manager - use to build levels
  - Level statistic checking

- Game Format
  - level creation
  - Combat initiation
  - character movement

- Modifiers
  - improve random mod generation process
  - temporary for combat needs (will just be used on stats and can be removed when combat complete)
  - Create add, subtrack, and comparisions

- build a npc manager
  - Create a default list of enemies that should be used

