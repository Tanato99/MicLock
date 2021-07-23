Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Windows\MicLock\loop_mic.bat" & Chr(34), 0
Set WshShell = Nothing