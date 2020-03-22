# Video Game Log - 03.22.2020

<!-- Update Table with Current File Count -->
Item | Count
---|--
| Current Directories | 15
| Current Files | 74

## Changes Made and Work Done
------------------------------
- Completed Armor test. Created test, run, and results for test. __<3.22.2020>__
- Equipment.h: I added a stats function to go with the new Armor stats function. __<3.22.2020>__ 
- Equipment.h: I updated values and variables for item type change __<3.22.2020>__
- Figured out that CodeTests.bat is not really going to work, and needs to be reworked, because when the individual folders run is called, it does not return back to the main bat file. So will work on.
- Also figured out that the make files for making all of the CodesTest is not working either will probs need to be done in another way,
and I have removed the call from the function.

## Action Items
----------------
- [ ] FIX LINKED LIST
- [x] ARMOR Test __<3.22.2020>__ 
- [x] Armor Test needs to be made __<3.22.2020>__ 
- [ ] Work on Character.h

## Questions
------------
- Should Armor have a type to only accept equipment of that type or should character have a armor type and validate equipment of items?
   - Answer: When the user gets a role they will grab the armor type needed for the role and then validate armor equips. __<3.21.2020>__

- How should a player/store inventory be done (Linked List/Array)?

## TO DO's
-----------
- [ ] Update README to explain what code files
- [x] Having issues with pointers if object is deleted its is deleted from everywhere, need to find a way to copy a pointer. __<3.22.2020>__ 
  - [x] Create copy constructors __<3.22.2020>__ 


#### Test.cpp
- [ ] Fix Test.cpp File, is not printing out everything stops before the dequip, issue might be with the Equipment Array Weps....
    - Worked on Test File, found errors with printing armor that were causing the issue. Still in progress.

#### Equipment.h
- [ ] Create dataset of equipment

#### Armor.h
- [x]  Test File for Armor __<3.22.2020>__
  - [x]  Test isfull method __<3.22.2020>__
- [x] Having issues with change function, need to try new test to see what wrong __<3.22.2020>__
- [x] Thinking about changing the name of stats and print for Armor class to brief and stats _1.1.2018_ __<3.22.2020>__
  - [x] I did not like the way that Stats and Print look, either need a full or just a brief so I want to __<3.22.2020>__
- [x] Update/change the dialogs for equiping and dequiping items __<3.22.2020>__

#### Roles.h
- [ ] Create dataset of roles {mage, warrior, thieft/rouge, healer}
  - [ ] Give a set of powers for each role
- [ ] Create Read from file function

<br />

---
## Future Ideas 
---
### Project
- Create a runTest.bat to run the code tests 
- Add an Inventory Class or possible use a database
- STATS class for Equipment, Roles, Chars

### Test Files
- Update Test files to include new methods
- Update Test file format
  - Add printouts for what is being down
  - Print Test Name and Test performing at the top
- Test Files to Make:
  - CodeTest_Armor.cpp
  -  CodeTest_Character.cpp
  - CodeTest_Combat.cpp
  - CodeTest_Functions.cpp

### Test.cpp
- Implement full test once other pieces are together
- Create general validation tests that will verify weapons, armor, and classes.

### Equipment.h
- Create a dataset for items for each role and of each type
- Add more stats, durabiity, strength, etc. (Will get added to class as well and calulated sums will be done by the armor)

### Roles.h
- Ability Pointes can not be changed like a static object, have to find a way to fix this, may need an edit option.
- Add stats that can be summed up in the character
- Annotate Functions

### Armor.h - NEED TO MAKE TEST FILE TO SOLVE ISSUES
- [x] Adding slot checks to dequip method because it fails if slot is empty. __<3.22.2020>__
- [x] isFull method needs more too it, some tweaking __<3.22.2020>__
- [x] thinking about changing the name of stats and print for Armor class to brief and stats __<3.22.2020>__
	- [x] I did not like the way that Stats and Print look, either need a full or just a brief so I want to change the format of this somehow (back burner) __<3.22.2020>__
- [x] Having issues with change function, need to try new test to see what wrong __<3.22.2020>__
- [x] Change function, I'm not sure if i really need it considering i have the equip and unequip, but might use it to properly change items for the slots considering how memory is transfered or linked from one place to the other. __<3.22.2020>__
- [ ] Annotate methods

### Character.h
- Add small inventory to player
- leveling up capabilities
- Annotate methods

### Functions.cpp and Functions.h
- Added Linked List to hold all types of things/ Database?
- Finish readRoles(Classes) method
  - Print Classes to file first then,
  - Use file for Classes to be read 
- Annotate methods

### Makefiles
- Makefile for each Test
- Makefile for Test folder which will compile all subfolder files
  - Fix issues with not compiling of test values - 2/2/2020
- Makefile subfolder issue and will be finding a work arround

### BatFiles
- Update Bat files
