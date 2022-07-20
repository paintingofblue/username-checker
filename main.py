import os
import platform
import requests
import random
from getch import getch

sys = platform.system()
if sys == 'Windows':
    clear = 'cls'
elif sys == 'Linux' or 'Darwin':
    clear = 'clear'

wordlist=""
site=""
proxy=""

def makedirs():
    if os.path.isdir('results') == True:
        pass
    elif os.path.isdir('results') == False:
        os.system('mkdir -p results')

    if os.path.isdir('wordlists') == True:
        pass
    elif os.path.isdir('wordlists') == False:
        os.system('mkdir -p wordlists')

    if os.path.isdir('proxies') == True:
        pass
    elif os.path.isdir('proxies') == False:
        os.system('mkdir -p proxies')

def menu():
    global i
    print("""
  _    _  _____ ______ _____  _   _          __  __ ______  _____ 
 | |  | |/ ____|  ____|  __ \| \ | |   /\   |  \/  |  ____|/ ____|
 | |  | | (___ | |__  | |__) |  \| |  /  \  | \  / | |__  | (___  
 | |  | |\___ \|  __| |  _  /| . ` | / /\ \ | |\/| |  __|  \___ \ 
 | |__| |____) | |____| | \ \| |\  |/ ____ \| |  | | |____ ____) |
  \____/|_____/|______|_|  \_\_| \_/_/    \_\_|  |_|______|_____/ 
                                                                  
                                                      made by lila
""" + i + """
__________________________________________________________________
"""
)
    i = ""

def soundcloud():
    os.system(clear)
    menu()
    print("soundcloud")
    getch()

def twitter():
    os.system(clear)
    menu()
    print("twitter")
    getch()

def weheartit():
    os.system(clear)
    menu()
    print("weheartit")
    getch()

def instagram():
    os.system(clear)
    menu()
    print("instagram")
    getch()

def tiktok():
    os.system(clear)
    menu()
    print("tiktok")
    getch()

def telegram():
    os.system(clear)
    menu()
    print("telegram")
    getch()

def reddit():
    os.system(clear)
    menu()
    print("reddit")
    getch()

def twitch():
    os.system(clear)
    menu()
    print("twitch")
    getch()

def behance():
    os.system(clear)
    menu()
    print("behance")
    getch()

def soloto():
    os.system(clear)
    menu()
    print("soloto")
    getch()

def linktree():
    os.system(clear)
    menu()
    print("linktree")
    getch()

def snapchat():
    os.system(clear)
    menu()
    print("snapchat")
    getch()

def github():
    os.system(clear)
    menu()
    print("github")
    getch()

def hotmail():
    os.system(clear)
    menu()
    print("hotmail")
    getch()

def yahoo():
    os.system(clear)
    menu()
    print("yahoo")
    getch()

def pastebin():
    os.system(clear)
    menu()
    print("pastebin")
    getch()

def steam():
    os.system(clear)
    menu()
    print("steam")
    getch()

def tumblr():
    os.system(clear)
    menu()
    print("tumblr")
    getch()

def epicgames():
    os.system(clear)
    menu()
    print("epicgames")
    getch()

def lastfm():
    os.system(clear)
    menu()
    print("lastfm")
    getch()

def xbox():
    os.system(clear)
    menu()
    print("xbox")
    getch()

def roblox():
    os.system(clear)
    menu()
    print("roblox")
    getch()

def minecraft():
    os.system(clear)
    menu()
    print("minecraft")
    getch()

def txties():
    os.system(clear)
    menu()
    print("txties")
    getch()

def tellonym():
    os.system(clear)
    menu()
    print("tellonym")
    getch()

def main():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 1/3"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Soundcloud\n(2) Twitter\n(3) WeHeartIt\n(4) Instagram\n(5) Tiktok\n(6) Telegram\n(7) Reddit\n(8) Twitch\n(9) Go to the next page\n(10) Quit\nChoice: "))
            if choice==1:
                soundcloud()
            elif choice==2:
                twitter()
            elif choice==3:
                weheartit()
            elif choice==4:
                instagram()
            elif choice==5:
                tiktok()
            elif choice==6:
                telegram()
            elif choice==7:
                reddit()
            elif choice==8:
                twitch()
            elif choice==9:
                main2()
            elif choice==10:
                os.system(clear)
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                getch()
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            getch()
            continue

def main2():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 2/3"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Behance\n(2) Solo.to\n(3) Linktree\n(4) Snapchat\n(5) Github\n(6) Hotmail\n(7) Yahoo\n(8) Pastebin\n(9) Go to the next page\n(10) Go to the previous page\nChoice: "))
            if choice==1:
                behance()
            elif choice==2:
                soloto()
            elif choice==3:
                linktree()
            elif choice==4:
                snapchat()
            elif choice==5:
                github()
            elif choice==6:
                hotmail()
            elif choice==7:
                yahoo()
            elif choice==8:
                pastebin()
            elif choice==9:
                main3()
            elif choice==10:
                os.system(clear)
                main()
            else:
                print("That was an incorrect answer. Press any key to continue")
                getch()
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            getch()
            continue

def main3():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 3/3"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Steam\n(2) Tumblr\n(3) Epic Games\n(4) LastFM\n(5) Xbox\n(6) Roblox\n(7) Minecraft\n(8) txti.es\n(9) Tellonym\n(10) Go to the previous page\nChoice: "))
            if choice==1:
                steam()
            elif choice==2:
                tumblr()
            elif choice==3:
                epicgames()
            elif choice==4:
                lastfm()
            elif choice==5:
                xbox()
            elif choice==6:
                roblox()
            elif choice==7:
                minecraft()
            elif choice==8:
                txties()
            elif choice==9:
                tellonym()
            elif choice==10:
                os.system(clear)
                main()
            else:
                print("That was an incorrect answer. Press any key to continue")
                getch()
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            getch()
            continue

if __name__ == '__main__':
    main()