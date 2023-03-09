"""
Description:
    Name: TermuxToolkit
    Tool: A Daily-Use Termux Tools Package
    Author: OmniTotal
    GitHub: https://github.com/toxic-noob
    Version: 1.0

Note:
    All Tools are Open Source
    You are welcomed to Use any Code.
    But consider giving Credit!
"""


import os
import time
import sys
import shutil

# Consts
toolList = ["d-pro", "netspeed", "text", "weather", "search", "typingspeed", "share", "short", "charge", "play"]
binPath = "/data/data/com.termux/files/usr/bin"

columns = shutil.get_terminal_size().columns

# Flush print
def psb(text):
    text += "\n"
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)

# Logo
def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns+5))
    print("\033[94m│   \033[92m▀▛▘               ▀▛▘     ▜ ▌  ▗▐  \033[94m  │".center(columns+15))
    print("\033[94m│   \033[92m ▌▞▀▖▙▀▖▛▚▀▖▌ ▌▚▗▘ ▌▞▀▖▞▀▖▐ ▌▗▘▄▜▀ \033[94m  │".center(columns+15))
    print("\033[94m│   \033[92m ▌▛▀ ▌  ▌▐ ▌▌ ▌▗▚  ▌▌ ▌▌ ▌▐ ▛▚ ▐▐ ▖\033[94m  │".center(columns+15))
    print("\033[94m│   \033[92m ▘▝▀▘▘  ▘▝ ▘▝▀▘▘ ▘ ▘▝▀ ▝▀  ▘▘ ▘▀▘▀ \033[94m  │".center(columns+15))
    print("\033[94m│                              \033[94m          │".center(columns+9))
    print("\033[94m│ \033[95mAuthor \033[92m: \033[37mOmniTotal                     \033[94m│".center(columns+25))
    print("\033[94m│ \033[95mTool   \033[92m: \033[37mA Package of Termux Tools     \033[94m│".center(columns+25))
    print("\033[94m│ \033[95mGitHub \033[92m: \033[37mhttps://github.com/Toxic-Noob \033[94m│".center(columns+25))
    print("\033[94m│ \033[95mCoder  \033[92m: \033[37mOmniMate                 \033[92mV1.0\033[94m │".center(columns+29))
    print("\033[94m└────────────────────────────────────────┘\033[37m".center(columns+10))


# Install Tools
def install(tool):
    print(f"\n    \033[37m[\033[92m~\033[37m] Installing \033[92m{tool.title()}\033[37m: ", end="")
    os.system(f"cp -r tools/{tool} {binPath} > /dev/null 2>&1")
    if (tool == "typingspeed"):
        os.system(f"cp -r tools/sentences.txt {binPath} > /dev/null 2>&1")
    os.system(f"chmod +x {binPath}/{tool} > /dev/null 2>&1")
    time.sleep(1)
    print("Done")
    time.sleep(1)
    psb(f"    \033[37m[\033[92m*\033[37m] Type \033[90m{tool} \033[37mto Start tool Or to See Instractions")
    time.sleep(1)


# Video Dowmloader
def dPro():
    url = input("\n    \033[37m[\033[92m*\033[37m] Enter Video/YT Playlist Url\033[92m:> \033[37m")
    logo()
    os.system(f"python tools/d-pro \"{url}\"")

# Internet Speed Checker
def netspeed():
    os.system("python tools/netspeed")

# Paste Text
def text():
    text = input("\n    \033[37m[\033[92m*\033[37m] Enter Text or File path\033[92m:> \033[37m")
    logo()
    if (os.path.exists(text)):
        os.system(f"python tools/text -f \"{text}\"")
    else:
        os.system(f"python tools/text -t \"{text}\"")

# Get Weather Information
def weather():
    logo()
    os.system("python tools/weather")

# Search for an Item from Storage
def search():
    text = input("\n    \033[37m[\033[92m*\033[37m] Enter Text to Search\033[92m:> \033[37m")
    logo()
    os.system(f"python tools/search \"{text}\"")

# Check Typing speed
def typingspeed():
    logo()
    os.system("cd tools && python typingspeed")

# Share a File
def share():
    path = input("\n    \033[37m[\033[92m*\033[37m] Enter your File Path\033[92m:> \033[37m")
    logo()
    os.system(f"python tools/share -u \"{path}\"")

# Short an Url
def short():
    url = input("\n    \033[37m[\033[92m*\033[37m] Enter Large URL\033[92m:> \033[37m")
    logo()
    os.system(f"python tools/short \"{url}\"")

# Monior Device Charge
def charge():
    logo()
    os.system("python tools/charge")

# Play a Song
def play():
    topic = input("\n    \033[37m[\033[92m*\033[37m] Enter Song Name/Topic\033[92m:> \033[37m")
    logo()
    os.system(f"python tools/play \"{topic}\"")


# Install all Tools
def installAll():
    logo()
    for tool in toolList:
        install(tool)
    
    psb("\n\n    \033[37m[\033[92m*\033[37m] Installation Complete\n")
    exit()

# Install Custom Tool
def installCustom():
    logo()
    psb("\n    \033[37m[\033[92m*\033[37m] Select your Tool to Install:\n")
    
    print("    [\033[92m01\033[37m] D-Pro (\033[92mVideo Downloader\033[37m)")
    print("    [\033[92m02\033[37m] Netspeed (\033[92mInternet Speed Checker\033[37m)")
    print("    [\033[92m03\033[37m] Text (\033[92mPaste Text and Share\033[37m)")
    print("    [\033[92m04\033[37m] Weather (\033[92mCheck Weather\033[37m)")
    print("    [\033[92m05\033[37m] Search (\033[92mSearch for Item\033[37m)")
    print("    [\033[92m06\033[37m] Typingspeed (\033[92mTyping Speed Checker\033[37m)")
    print("    [\033[92m07\033[37m] Share (\033[92mShare Files\033[37m)")
    print("    [\033[92m08\033[37m] Short (\033[92mShorten Url\033[37m)")
    print("    [\033[92m09\033[37m] Charge (\033[92mMonitor Phone Charging\033[37m)")
    print("    [\033[92m10\033[37m] Play (\033[92mPlay Song from YouTube\033[37m)")
    
    print("\n    [\033[92m00\033[37m] Exit")
    
    op = input("\n    [\033[92m*\033[37m] Enter your Choice\033[92m:> \033[37m")
    
    if (op in ["00", "0"]):
        exit("\033[37m")
    
    if not (op == "10"):
        op = op.replace("0", "")
    
    while not (op in [str(x) for x in range(1, 11)]):
        psb("\n    \033[37m[\033[91m!\033[37m] Wrong Input!")
        op = input("\n    [\033[92m*\033[37m] Enter your Choice:> \033[92m")
    if not (op == "10"):
        op = op.replace("0", "")
    
    tool = toolList[int(op) - 1]
    install(tool)
    exit("")

# Install Required Packeges
def installReq():
    os.system("python setup.py")

# Check For Update
def update():
    logo()
    psb("\n    \033[37m[\033[92m*\033[37m] Please Wait")
    psb("    \033[37m[\033[92m*\033[37m] Checking Update")
    
    import requests
    import json

    try:
        oldVersion = json.loads(open(".version", "r").read())["version"]
    except:
        oldVersion = 0.0
    
    try:
        newVersion = requests.get("https://raw.githubusercontent.com/Toxic-Noob/TermuxToolkit/main/.version").json()["version"]
    except requests.exceptions.ConnectionError:
        psb("\n    [\033[91m!\033[37m] Error Occured!")
        psb("    [\033[92m*\033[37m] Are you connected to Internet?\n")
        sys.exit()
    except json.decoder.JSONDecodeError:
        newVersion = 0.01
    
    if (newVersion != oldVersion):
        psb("\n    [\033[92m*\033[37m] Tool Update Found!")
        time.sleep(0.6)
        psb("    [\033[92m*\033[37m] Updating...")
        
        time.sleep(2)
        os.system("cd .. && rm -rf TermuxToolkit && git clone https://github.com/toxic-noob/TermuxToolkit > /dev/null 2>&1")
        psb("\n    [\033[92m*\033[37m] Update Complete!")
        print("\n    \033[37m[\033[92m*\033[37m] Staring tool...")
        time.sleep(2)
        os.system("cd .. && cd TermuxToolkit && python main.py")
        sys.exit()
    
    else:
        psb("\n    [\033[92m*\033[37m] You are Already using the Updated Version of TermuxToolkit!\n")
        sys.exit()

        
        
    
    


# Main Menu
def menu():
    logo()
    
    psb("\n    \033[37m[\033[92m*\033[37m] Choose Your Option:\n")
    
    print("    [\033[92m01\033[37m] D-Pro \t\t(\033[90mVideo Downloader\033[37m)")
    print("    [\033[92m02\033[37m] Netspeed \t(\033[90mInternet Speed Checker\033[37m)")
    print("    [\033[92m03\033[37m] Text \t\t(\033[90mPaste Text and Share\033[37m)")
    print("    [\033[92m04\033[37m] Weather \t(\033[90mCheck Weather\033[37m)")
    print("    [\033[92m05\033[37m] Search \t(\033[90mSearch for Item\033[37m)")
    print("    [\033[92m06\033[37m] Typingspeed \t(\033[90mTyping Speed Checker\033[37m)")
    print("    [\033[92m07\033[37m] Share \t\t(\033[90mShare Files\033[37m)")
    print("    [\033[92m08\033[37m] Short \t\t(\033[90mShorten Url\033[37m)")
    print("    [\033[92m09\033[37m] Charge \t(\033[90mMonitor Phone Charging\033[37m)")
    print("    [\033[92m10\033[37m] Play \t\t(\033[90mPlay Song from YouTube\033[37m)")
    
    print("\n    [\033[92m11\033[37m] Install All Tools")
    print("    [\033[92m12\033[37m] Install Custom Tool")
    print("    [\033[92m13\033[37m] Install Required Packages")
    print("    [\033[92m14\033[37m] Update TermuxToolkit")
    print("\n    [\033[92m15\033[37m] Exit")
    
    op = input("\n    [\033[92m*\033[37m] Enter your Choice\033[92m:> \033[37m")
    if not (op == "10"):
        op = op.replace("0", "")
    
    while not (op in [str(x) for x in range(1,16)]):
        psb("\n    \033[37m[\033[91m!\033[37m] Wrong Input!")
        op = input("\n    [\033[92m*\033[37m] Enter your Choice\033[92m:> \033[37m")
    if not (op == "10"):
        op = op.replace("0", "")
    
    if (op == "15"):
        exit("")
    
    # Instead of if...elif...else - ing, make a function list and call by it's index
    
    funcList = [dPro, netspeed, text, weather, search, typingspeed, share, short, charge, play, installAll, installCustom, installReq, update]
    
    funcList[int(op) -1 ]()


menu()
