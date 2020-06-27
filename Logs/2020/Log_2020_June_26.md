# FUN Command Line Game Log - 06.26.2020

<!-- Update Table with Current File Count -->
Item | Count
---|--
| Current Directories | 16
| Current Files | 84

_Date_ - When item was added <br />
__\<Date\>__ - When Item was completed

## Changes Made and Work Done
------------------------------
- Created cases for LinkedList CodeTest
- Creating Stats class remove stats function
- Creating Stats print to file function

## Action Items
----------------
- [ ] Stats Class: printToFile _6.26.2020_
- [ ] Stats Class: remove stats function _6.26.2020_
- [ ] Work on Character.h _2.17.2020_
- [ ] Stats Integration _6.26.2020_

## Questions
------------
- Should Armor have a type to only accept equipment of that type or should character have a armor type and validate equipment of items?
   - Answer: When the user gets a role they will grab the armor type needed for the role and then validate armor equips. __<3.21.2020>__
- How should a player/store inventory be done (Linked List/Array/RBDB)?
- Need to figure out how to fix makefile for this case _6.26.2020_  
  - Figured out that CodeTests.bat is not really going to work, and needs to be reworked, because when the individual folders run is called, it does not return back to the main bat file. So will work on.
  - Also figured out that the make files for making all of the CodesTest is not working either will probs need to be done in another way, and I have removed the call from the function.

## TO DO's
-----------
- [ ] Update README to explain what code files _3.21.2020_
- [x] Create stats class (equipment, role, character) _3.22.2020_ __<5.29.2020>__
- [ ] Integrate stat class into the other classes 
  - [ ] Add to Equipment Class _6.26.2020_
  - [ ] Add to Role Class _6.26.2020_
  - [ ] Add to Character Class _6.26.2020_  


#### Test.cpp
- [ ] Fix Test.cpp File, is not printing out everything stops before the dequip, issue might be with the Equipment Array Weps....
    - Worked on Test File, found errors with printing armor that were causing the issue. Still in progress.

#### Equipment.h
- [ ] Create dataset of equipment

#### Armor.h
- [ ] Annotate Methods _5.29.2020_

#### Roles.h
- [ ] Create dataset of roles {mage, warrior, thieft/rouge, healer}
  - [ ] Give a set of powers for each role
- [ ] Create Read from file function
- [ ] Create copy constructors _5.24.2020_
  - [x] Create __<5.24.2020>__
  - [ ] Test
- [ ] Work on Code Test 1
  - [ ] Does not fully complete test, most likely an issue with the linked list

#### Character.h
- [ ] Armor Equips
  - [ ] Full Armor Equip
  - [ ] Individual Functions
  - [ ] Armor Equip/Dequip head
  - [ ] Armor Equip/Dequip chest
  - [ ] Armor Equip/Dequip pants
  - [ ] Armor Equip/Dequip weapon
- [ ] Role changes
  - [ ] Adding powers
  - [ ] accessing powers
- [ ] Level Up for STATs and trickle down to all objects and classes
- [ ] create reload, when equipment is changed _5.25.2020_ _6.26.2020_
  - _Moving to Character because that is where the recalculation will happen. Also may not have to reload, but use the remove stat and add stat for equip and dequipt_ _6.26.2020_
  - _May need if we want to get the updated level up of objects but will need heavy testing_ _6.26.2020_
- [ ] Combat
  - [ ] Attacking and defending, not sure if i will need a whole class for this or not

#### Stats.h _5.25.2020_
- [ ] Create remove stat function _5.30.2020_

#### LinkedList.h _6.26.2020_
- [ ] Create Code Test _6.26.2020_
  - [ ] Equipment Tests _6.26.2020_
    - [x] Created file _<6.26.2020>_
  - [ ] Role Tests _6.26.2020_
    - [x] Created file _<6.26.2020>_
  - [ ] Armor Tests _6.26.2020_
- [ ] Testing creation and deletion functions _6.26.2020_
- [ ] Testing loading functions _6.26.2020_


<br />

---
## Future Ideas 
---
### Project
- Create a runTest.bat to run the code tests 
- Add an Inventory Class or possible use a database
- STATS class for Equipment, Roles, Chars

### Makefiles
- Makefile for each Test
- Makefile for Test folder which will compile all subfolder files
  - Fix issues with not compiling of test values - 2/2/2020
- Makefile subfolder issue and will be finding a work arround

### BatFiles
- Update Bat files

### Test Files
- Update Test files to include new methods
- Update Test file format
  - Add printouts for what is being down
  - Print Test Name and Test performing at the top
- Test Files to Make:
  - CodeTest_Armor.cpp
  - CodeTest_Character.cpp
  - CodeTest_Combat.cpp
  - CodeTest_Functions.cpp

### Functions.cpp and Functions.h
- Added Linked List to hold all types of things/ Database?
- Finish readRoles(Classes) method
  - Print Classes to file first then,
  - Use file for Classes to be read 
- Annotate methods

### Test.cpp
- Implement full test once other pieces are together
- Create general validation tests that will verify weapons, armor, and classes.

### Character.h
- Add small inventory to player
- leveling up capabilities
- Annotate methods

### Roles.h
- Ability Pointes can not be changed like a static object, have to find a way to fix this, may need an edit option.
- Add stats that can be summed up in the character
- Annotate Functions

### Armor.h
- create reload, when equipment is changed _5.25.2020_
- Annotate methods

### Equipment.h
- Create a dataset for items for each role and of each type
- Add more stats, durabiity, strength, etc. (Will get added to class as well and calulated sums will be done by the armor)

### Stats.h _5.25.2020_
- Annotate methods

### LinkedList _6.26.2020_
- Code Tests to test functions
- Annotate methods