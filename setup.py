"""
Description:
    Package Setup script for TermuxToolkit
    Author: OmniTotal
"""


import os
import time
import subprocess as sb


termuxApi = False if (sb.getoutput("command -v termux-tts-speak") == "") else True
storage = True if (sb.getoutput("cd /sdcard/") == "") else False

print("\n    [\033[92m!\033[47m] Installing Required Packages, Please wait...")

if not (termuxApi):
    print("\n    [\033[92m*\033[37m] Installing Termux-Api...\n")
    os.system("pkg install termux-api -y")

print("\n    [\033[92m*\033[37m] Installing mpv...\n")
os.system("pkg install mpv -y")

print("\n    [\033[92m*\033[37m] Installing requests...\n")
os.system("pip install requests")

print("\n    [\033[92m*\033[37m] Installing bs4...\n")
os.system("pip install bs4")

print("\n    [\033[92m*\033[37m] Installing helpscript...\n")
os.system("pip install helpscript")

print("\n    [\033[92m*\033[37m] Installing Speestest-Cli")
os.system("pip install speedtest-cli")

if not (storage):
    print("\n    [\033[92m*\033[37m] Grant storage Permission to Termux...\n")
    os.system("termux-setup-storage")

if not (termuxApi):
    print("\n\n    [\033[92m*\033[37m] Install Termux-API Apk and Install\n")
    print("    [!] APK Link: https://f-droid.org/repo/com.termux.api_51.apk")
    print("\n    [*] Don't worry, the app is secure ;)\n")

time.sleep(1)
print("\n    [\033[92m*\033[37m] Installation Complete!\n")
