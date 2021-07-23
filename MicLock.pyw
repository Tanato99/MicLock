import keyboard
from win10toast import ToastNotifier
import os
import subprocess


def change_status_mic(status_mic, toaster, vol, name_mic):
    if status_mic:
        status_mic = False
        execute_command(status_mic, toaster, vol, name_mic)
    elif not status_mic:
        status_mic = True
        execute_command(status_mic, toaster, vol, name_mic)
    return status_mic


def execute_command(status_mic, toaster, vol, name_mic):
    if status_mic:
        turn_on_mic(name_mic)
        set_volume_at_volume()
        toaster.show_toast("MicTool", "Mic ON\nVolume set to " + vol, "C:\\Windows\\MicLock\\resources\\microphone.ico",
                           duration=3)

    elif not status_mic:
        turn_off_mic(name_mic)
        toaster.show_toast("MicTool", "Mic OFF", "C:\\Windows\\MicLock\\resources\\microphone.ico", duration=3)


def turn_on_mic(name_mic):
   os.system("C:\\Windows\\MicLock\\resources\\SoundVolumeView.exe /unmute" + " " + name_mic)


def turn_off_mic(name_mic):
    os.system("cd c:\\windows\\system32 && taskkill /f /IM nircmdc.exe > nul 2> nul")
    os.system("C:\\Windows\\MicLock\\resources\\SoundVolumeView.exe /mute" + " " + name_mic)


def set_volume_at_volume():
    subprocess.run(["C:\\windows\\system32\\cscript.exe", "C:\\Windows\\MicLock\\start_loop_mic.vbs"])


def read_file():
    with open("C:\\Windows\\MicLock\\Volume.txt", 'r') as file:
        vol = file.readline(4)
        name_mic = file.readline(20)
        hotkey = file.readline(15)
        msec = file.readline(10)
    file.close()
    return vol.strip('\n'), name_mic.strip('\n'), hotkey.strip('\n'), msec.strip('\n')


def create_bat_loop_mic(str_vol_extended, msec):
    txt_loop_mic = "C:\\windows\\MicLock\\resources\\nircmdc.exe loop 172800 " + msec + " setsysvolume " + str_vol_extended + " default_record"
    with open("C:\\Windows\\MicLock\\loop_mic.bat", 'w') as file:
        file.write(txt_loop_mic)
    file.close()


def main():
    vol, name_mic, hotkey, msec = read_file()
    vol_extended = int((65535 * int(vol)) / 100)
    str_vol_extended = str(vol_extended)
    create_bat_loop_mic(str_vol_extended, msec)
    toaster = ToastNotifier()
    status_mic = False
    execute_command(status_mic, toaster, vol, name_mic)
    while True:
        if keyboard.is_pressed(hotkey):
            status_mic = change_status_mic(status_mic, toaster, vol, name_mic)


if __name__ == "__main__":
    main()