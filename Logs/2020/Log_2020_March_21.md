# Video Game Log - 03.21.2020

<!-- Update Table with Current File Count -->
Item | Count
---|--
| Current Directories | 15
| Current Files | 69

## Changes Made and Work Done
------------------------------
- Updated Equipment stats by adding NULL values for numbers. __<3.21.2020>__
- Updated equipement test and corresponding files __<3.21.2020>__
- Figured out that CodeTests.bat is not really going to work, and needs to be reworked, because when the individual folders run is called, it does not return back to the main bat file. So will work on.
- Also figured out that the make files for making all of the CodesTest is not working either will probs need to be done in another way,
and I have removed the call from the function.

## Action Items
----------------
- [x] Test equipment validation method __<3.21.2020>__
- [ ] Armor Test needs to be made
- [ ] Work on Character.h
- [x] Turn Logs into Markdown files __<3.21.2020>__

## Questions
------------
- Should Armor have a type to only accept equipment of that type or should character have a armor type and validate equipment of items?
   - Answer: When the user gets a role they will grab the armor type needed for the role and then validate armor equips. __<3.21.2020>__

- How should a player/store inventory be done (Linked List/Array)?

## TO DO's
-----------
- [ ] Update README to explain what code files
- [ ] Having issues with pointers if object is deleted its is deleted from everywhere, need to find a way to copy a pointer. 
  - [ ] Create copy constructors
- [x] Update Armor types, and associated data __<3.21.2020>__

#### Test.cpp
- [ ] Fix Test.cpp File, is not printing out everything stops before the dequip, issue might be with the Equipment Array Weps....
    - Worked on Test File, found errors with printing armor that were causing the issue. Still in progress.

#### Equipment.h
- [ ] Create dataset of equipment
- [x] Need to test new validation method __<3.21.2020>__
- [x] add -1 null value to AT, IT, WT __<3.21.2020>__
- [x] Change AT 0 -> no armor needed so that it will have 0 -> 3 and -1 will be a null value. __<3.21.2020>__

#### Armor.h
- [ ]  Test File for Armor
  - [ ]  Test isfull method
- [ ] Having issues with change function, need to try new test to see what wrong
- [ ] Thinking about changing the name of stats and print for Armor class to brief and stats _1.1.2018_
  - I did not like the way that Stats and Print look, either need a full or just a brief so I want to

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

### Roles.h
- Ability Pointes can not be changed like a static object, have to find a way to fix this, may need an edit option.
- Annotate Functions

### Armor.h - NEED TO MAKE TEST FILE TO SOLVE ISSUES
    - Adding slot checks to dequip method because it fails if slot is empty.
    - isFull method needs more too it, some tweaking - 1/31/2019
    - thinking about changing the name of stats and print for Armor class to brief and stats - 1/1/2018
	- I did not like the way that Stats and Print look, either need a full or just a brief so I want to change the format of this somehow (back burner) - 1/1/2018
	 Having issues with change function, need to try new test to see what wrong
    - Change function, I'm not sure if i really need it considering i have the equip and unequip, but might use it to properly change items for the slots considering how memory is transfered or linked from one place to the other. [Work in Progress]
	- Annotate methods

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
