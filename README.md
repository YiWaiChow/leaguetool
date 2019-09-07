# leaguetool
just a league of legend champ selector


**milestone** 
- Make textbase version(Finished)
- create a gui for the tool( Finished)
- link the textbase version to the gui(Finished)
- intergrate everything into a exe(Finished)'
          
 **Concept:**\
 the score calculated for each champion is base on\
 -user main champion\
 -attribute that needed in the current game(Based on the champion selected)\
 the goal of the programn is to output the champions that has the highest score inturns meaning the champions that needed the most in current game
 
**Defining Feature:**\
the storing of the champions after score is calculated is done using an modified AVL Tree, it is to achieve a O(log(n)) runtime  when outputing the champions with the highest score ( where n is the number of champions)

**Usage**:

textbased version:
- run main.py

GUI version:
- run GUIversion.py / GUIversion.exe

**Future Improvement**
- implement a improved score calculating system
- improve GUI visual design
