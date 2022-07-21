# Stat-Tracker
Stat Tracker for speedrun atttemps, using pynput.

Numpad 0-9 are the outputs in the selected txt file from top to bottom, pressing a numpad key increments the corrosponding integer by 1 by default.

Pressing left Shift increments the incrementing value by 1.

	ESX: press Shift, press num1, the first integer goes up two, press Shift 2 times, press num1, the first integer goes up 4.
  
Pressing left Alt does the same as Shift but increments negatively.

Pressing left Ctrl resets the incrementing value to the default of 1.

Pressing Esc will exit the program.

	Note: All values, in the txt and the value of the incrementor, are only changed upon release of the key, holding a key down will do nothing.
  
The first and second value are setup to reset to 0 on program launch, but these values are tracked lifetime as the 8th and 9th values.

Upon statup enter the filename, excluding directory and file extension, of the the data set you would like to modify and hit enter. If a matching filename is found in the Stats folder it will open the file and start listening for your numpad. If a matching filename cannot be found you will be asked to enter a correct one. If you wish to exit before loading a filename type "exit" instead. Functionality for switching data sets after intial selection has not yet been implemented.

lool xd
