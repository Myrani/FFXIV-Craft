# FFXIV-Craft
An FFXIV queue crafting system/manager : more than a macro repeater, this one can swap jobs and do custom orders, wanna craft 200 planks, ingots 
or anything else in any quantities while you sleep ? now, you can ! 

This project was born on a whim, didn't find any good craft manager that wasn't either just a macro repeater or a botting soft, had some time, so I made my own !

The soft is still in beta, all the main functions are available but if you find any bug, please do report them ! even smaller ones !
# Install
If you just want to use the software and are not interested in the code, all good !

  - Just use the .exe file like a regular program and enjoy !  

Non standard python3 library used for any potential tweeks you wanna add !

  - Quick install-All command : 
  
    pip3 install -r requirements.txt

  - Pyautogui : https://pyautogui.readthedocs.io/en/latest/
    
    Quick install -> pip3 install pyautogui
  
  - PyQt5 : https://doc.qt.io/qtforpython/
    
    Quick install -> pip3 install PyQt5
 
 
# Tutorial
How does the program works ?

There's 3 steps : 
  - Create a new "Job" by clicking on the ~ create a job button ~
  - Fill in all the info the craft need :
    - The outfit you want to wear to craft this job 
    - The item name you want to craft
    - The quantity of said to craft
    - The keys to proc the macro in plain text and in proc order (first: ctrl , second: &)
    - The usual time your macro need to proc 
    - You can personalize the quality of each craft components by specifying it quality Area,by default it will just press the FFXIV Fabricate button
      otherwise it will mimic the top to bottom quality settings
    - Add it to the Current planned Joblist, and you can save it for a later use if you select the "remember" option to save you some time next time
  - Once every jobs are specified , press the ~ Start Crafting ~ button, once done, you'll have 5 seconds to go back on the game window after that the manager          will start Working !
    
