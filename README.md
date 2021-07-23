# MicLock
MicLock is a tool for windows, written in python that allows of turn off, turn on, and lock the volume of microphone

***How does it work?***
When the pc is turned on, it disables the microphone, if you press hotkey you change the status of the microphone 
(if it is on, it turns it off, while if it is off, it sets it to on and set the volume to the value you have set)

***How to use:***
1. Move the "MicLock" folder in C:\windows
2. Install the requiments.txt with the command: 
   ```
    pip install -r requirements.txt
   ```
3. Open the file volume.txt and change the values in following way:
   In first line write the volume that you want lock (Default: 100)
   In the second line write the name of your microphone (Default: Microphone)
   In the third line write the hotkey that you want use to change the state of the microphone (Default: ctrl+alt)
   In the fourth line write every how many milliseconds you want to send a request to lock the volume (Default: 200)
4. In autostart\Miclock.bat you may need to specify the directory where python is installed
5. If you want MickLock.py to start automatically at startup
   in the regedit add in HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
   a new string value and in the value field add this path: C:\Windows\MicLock\autostart\Hide_MicLock.vbs


***Notes:***

1.If you change any value in the volume.txt file you have to restart the pc or restart 
  the python.exe and nircmdc.exe processes to see the changes applied
  
2.I tested it with python 3.7, I cannot guarantee it will work with other versions as well



