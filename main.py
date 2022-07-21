import os
import platform
import sys
import requests
import random
import re
import datetime
from getch import getch
from colr import Colr as C

operatingsys = platform.system()
if operatingsys == 'Windows':
    clear = 'cls'
elif operatingsys == 'Linux' or 'Darwin':
    clear = 'clear'

wordlist=""
site=""

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def makedirs():
    if os.path.isdir('results'):
        pass
    elif os.path.isdir('results') == False:
        os.system('mkdir -p results/{Soundcloud,Twitter,WeHeartIt,Instagram,Tiktok,Telegram,Reddit,Twitch,Behance,Solo.to,Linktree,Snapchat,Github,Hotmail,Yahoo,Pastebin,Steam,Tumblr,EpicGames,LastFM,Xbox,Roblox,Minecraft,txti.es,Tellonym}')

    if os.path.isdir('wordlists'):
        pass
    elif os.path.isdir('wordlists') == False:
        os.system('mkdir -p wordlists')

    if os.path.isdir('proxies'):
        pass
    elif os.path.isdir('proxies') == False:
        os.system('mkdir -p proxies')

def checker(url1, name1):
    global good
    global bad
    global count
    input1()
    menu()
    good = 0
    bad = 0
    count = 0
    time1 = str(datetime.datetime.now()).split('.')
    
    with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
        for line in a_file:
            global stripped_line
            count = count + 1
            stripped_line = line.strip()
            sess = requests.Session()
            req = sess.get("https://" + url1 + stripped_line, headers=HEADERS)

            if req.status_code == 200:
                bad = bad + 1
                print(style.RESET + "https://" + url1 + f"{stripped_line}")
                print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

            elif req.status_code == 404:
                good = good + 1
                print(style.RESET + "https://" + url1 + f"{stripped_line}")
                print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                with open("results/" + name1 + "/" + time1[0] + ".txt", "a") as results:
                    results.write("https://" + url1 + f"{stripped_line}" + "\n")

def input1():
    global wordlist1
    menu()
    wordlist1 = str(input("What is the name of the wordlist you want to use?\n"))

def soundcloud():
    checker("soundcloud.com/", "Soundcloud")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def twitter(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def weheartit(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def instagram(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def tiktok(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def telegram(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def reddit(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def twitch(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def behance(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def soloto(): 
    checker("solo.to/", "Solo.to")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def linktree():
    checker("linktr.ee/", "Linktree")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def snapchat(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def github():
    checker("github.com/", "Github")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def hotmail(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def yahoo(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def pastebin(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def steam(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def tumblr(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def epicgames(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def lastfm(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def xbox(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def roblox(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def minecraft(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def txties():
    checker("txti.es/", "txti.es")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def tellonym():
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def krunker(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def rentry(): # not done
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    getch()

def main():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 1/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Soundcloud\n(2) Twitter\n(3) WeHeartIt\n(4) Instagram\n(5) Tiktok\n(6) Telegram\n(7) Reddit\n(8) Twitch\n(9) Go to the next page\n(10) Quit\nChoice: "))
            if choice==1:
                soundcloud()
                continue
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
                break
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
        i = "                                                          page 2/4"
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
                break
            elif choice==10:
                os.system(clear)
                main()
                break
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
        i = "                                                          page 3/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Steam\n(2) Tumblr\n(3) Epic Games\n(4) LastFM\n(5) Xbox\n(6) Roblox\n(7) Minecraft\n(8) txti.es\n(9) Go to the next page\n(10) Go to the previous page\nChoice: "))
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
                main4()
                break
            elif choice==10:
                main2()
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                getch()
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            getch()
            continue

def main4():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 4/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Krunker\n(2) Rentry\n(3) Tellonym\n(4) Go to the previous page\nChoice: "))
            if choice==1:
                krunker()
            elif choice==2:
                rentry()
            elif choice==3:
                tellonym()
            elif choice==4:
                main3()
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                getch()
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            getch()
            continue

def menu():
    global i
    os.system(clear)
    print("""
  _    _  _____ ______ _____  _   _          __  __ ______  _____ 
 | |  | |/ ____|  ____|  __ \| \ | |   /\   |  \/  |  ____|/ ____|
 | |  | | (___ | |__  | |__) |  \| |  /  \  | \  / | |__  | (___  
 | |  | |\___ \|  __| |  _  /| . ` | / /\ \ | |\/| |  __|  \___ \ 
 | |__| |____) | |____| | \ \| |\  |/ ____ \| |  | | |____ ____) |
  \____/|_____/|______|_|  \_\_| \_/_/    \_\_|  |_|______|_____/ 
                                                                  
                                 made by github.com/paintingofblue
""" + i + """
__________________________________________________________________
""")
    i = ""

if __name__ == '__main__':
    main()