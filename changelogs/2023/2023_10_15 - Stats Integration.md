# FUN Command Line Game Log: 10.15.2023 - 
<!-- Update: Current Log date -->

Last Updated: 11.5.2023 <!-- Update with previous log date -->
Version: 0.5.13
<!-- Update version number when changes made-->
<!-- Verions Additions 
  + 1.0.0 is for major project wide changes like adding a whole new concept/face change
    + V1 = MVP CLI version of game
    + V2 = integration of Textual package and any visiualization features
  + 0.1.0 is for current feature version updates including additions/removal/revamp of methods or parts (general idea of things)
  + 0.0.1 is for minor changes including: bug fixes, additions to current methods
 -->

<!-- _Date_ - When item was added  
__\<Date\>__ - When Item was completed
-->
<!-- Update Table with Current File Count -->

## Current Goals

- [ ] Stats integration 
- [x] Define Game Play
- [ ] Create a level generation process -> 0.6
- [ ] Define game combat and interaction -> 0.7
- [ ] Game Manager
  - [ ] level creation
  - [ ] Combat initiation
  - [ ] character movement


## Changes Made and Work Done

------------------------------
<!-- Update version number when changes made-->

### In Progress
- [#117](https://github.com/jevinevans/Game/issues/117) [Fix] [+0.0.1]

### Added/Changed
- [#120](https://github.com/jevinevans/Game/issues/120) [2023.11.5] [v0.5.13]
- [#45](https://github.com/jevinevans/Game/issues/45) [2023.11.5] [v0.5.12]
- [#44](https://github.com/jevinevans/Game/issues/44) [2023.10.22] [v0.5.11]
- [#103](https://github.com/jevinevans/Game/issues/103) [2023.10.15] [v0.5.10]

### Fixed

### Informational


------------------------------

## Message - 11.5.2023

1. Updating modifier add/mult name change (starting PR)
1. Add more test coverage for character module tests

---------------------------

- Modifiers
  - Change "adds" to "base" and "mults" to "percentage" (big change, but better clarity) [!!!!!!!!!!]
    - Needs to be #1 in the next set of tasks after issue is created
  - improve random mod generation process
  - temporary for combat needs (will just be used on stats and can be removed when combat complete)
  - Create add, subtrack, and comparisions

- build a npc manager
  - Create a default list of enemies that should be used

- Level manager and creation process
  - Enemy/Boss generation
  - level manager - use to build levels
  - Level statistic checking

- Combat

- Manager Menu's
  - Split into different modules for game data and character data