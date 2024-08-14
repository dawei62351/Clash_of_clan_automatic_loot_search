# Clash_of_clan_automatic_loot_search
This is a python script to help automatically search for a big loot base<br><br>

This is done with pyautogui, which can manipulate screen and mouse.  And then pytesseract was used to extract text from image to assess the loot.<br><br>

The mouse click locations are hard coded.<br><br>

To use this code, open up clash of clan with bluestack.  Disable onscreen button.  Move the game window to the top-left of your screen(1080p).  <br>
Place the python script window beside the game window.  Make sure the game window is not covered.<br>
You will probably need to change the x,y coordinate for you trainning camp(line 57).<br>
Then run the script, it will re-train the most recent troop and start searching. <br>
It is not 100% consistant.  But it works pretty well.  <br>
Once it found a good loot base, it will pop up a alert with a sound cue(my voice saying: "found it!").<br>
Then do the attack yourself and go back to the home base.<br>
Then just repeat until you are done.  <br>
