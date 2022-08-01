import os
import platform
import requests
import datetime
import time
import json
from validate_email import validate_email

operatingsys = platform.system()
if operatingsys == 'Windows':
    import msvcrt
    clear = 'cls'
    getch1 = 'msvcrt.getch()'
    mainfunc = 'main()'
elif operatingsys == 'Linux' or 'Darwin':
    from getch import getch # type:ignore
    clear = 'clear'
    getch1 = 'getch()'
    mainfunc = 'main()'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

notdone = "This site isn't done.\n\nPress any key to return to the main menu."

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
    sites = "Behance EpicGames Github Hotmail Twitch Krunker LastFM Linktree Minecraft Pastebin Reddit Rentry Snapchat Solo.to Soundcloud Steam Tellonym Tiktok Tumblr Twitter WeHeartIt Xbox Yahoo txti.es".split()
    if os.path.isdir('results'):
        pass
    elif os.path.isdir('results') == False:
        os.system("mkdir results")
        for items in sites:
            path = os.path.join("results/", items)
            os.mkdir(path)
    if os.path.isdir('wordlists'):
        pass
    elif os.path.isdir('wordlists') == False:
        os.system('mkdir wordlists')

def checker(url1, name1):
    global good
    global bad
    global count
    good = 0
    bad = 0
    count = 0
    time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
    input1()
    menu()
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
                with open("results/" + name1 + "/" + time1 + ".txt", "a") as results:
                    results.write("https://" + url1 + f"{stripped_line}" + "\n")
            time.sleep(interval)

def input1():
    while True:
        global wordlist1
        global interval
        global i
        i = ""
        menu()
        wordlist1 = str(input("What is the name of the wordlist you want to use?\n(Note that the program automatically appends .txt to your input.)\n"))
        try:
            open('wordlists/' + wordlist1 + '.txt', "r")
            pass
        except:
            menu()
            print("The file you entered either doesn't exist or was incorrectly entered.\nPlease try again.\n\nPress any key to continue.")
            exec(getch1)
            exec(mainfunc)
            break
        menu()
        interval = float(input("What delay do you want to have inbetween checks?\n(This is helpful to avoid ratelimiting & anti-spam measures on some sites.)\n"))
        break

def soundcloud():
    while True:
        checker("soundcloud.com/", "Soundcloud")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def twitter():
    while True:
        global good
        global bad
        global count
        global i
        i = ''
        good = 0
        bad = 0
        count = 0
        menu()
        time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
        input1()
        menu()
        with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
            for line in a_file:
                global stripped_line
                count = count + 1
                stripped_line = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://nitter.it/{stripped_line}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(style.RESET + f"https://twitter.com/{stripped_line}")
                    print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(style.RESET + "https://twitter.com/"f"{stripped_line}")
                    print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                    with open("results/Twitter/" + time1 + ".txt", "a") as results:
                        results.write("https://twitter.com/"f"{stripped_line}" + "\n")
                time.sleep(interval)
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break
    

def weheartit():
    while True:
        checker("weheartit.com/", "WeHeartIt")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def tiktok(): # not done
    while True:
        menu()
        print(notdone)
        #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def twitch():
    while True:
        global good
        global bad
        global count
        global i
        i = ''
        good = 0
        bad = 0
        count = 0
        menu()
        time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
        input1()
        menu()
        with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
            for line in a_file:
                global stripped_line
                count = count + 1
                stripped_line = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://twitchtracker.com/{stripped_line}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(style.RESET + f"https://twitch.tv/{stripped_line}")
                    print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(style.RESET + "https://twitch.tv/"f"{stripped_line}")
                    print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                    with open("results/Twitch/" + time1 + ".txt", "a") as results:
                        results.write("https://twitch.tv/"f"{stripped_line}" + "\n")
                time.sleep(interval)
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def reddit():
    while True:
        global good
        global bad
        global count
        global i
        i = ''
        good = 0
        bad = 0
        count = 0
        menu()
        time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
        input1()
        menu()
        with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
            for line in a_file:
                global stripped_line
                count = count + 1
                stripped_line = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://libredd.it/user/{stripped_line}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(style.RESET + f"https://www.reddit.com/u/{stripped_line}")
                    print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(style.RESET + "https://www.reddit.com/u/"f"{stripped_line}")
                    print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                    with open("results/Reddit/" + time1 + ".txt", "a") as results:
                        results.write("https://www.reddit.com/u/"f"{stripped_line}" + "\n")
                time.sleep(interval)
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def behance():
    while True:
        checker("behance.net/", "Behance")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def soloto(): 
    while True:
        checker("solo.to/", "Solo.to")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def linktree():
    while True:
        checker("linktr.ee/", "Linktree")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def snapchat(): # not done
    while True:
        menu()
        print(notdone)
        #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def github():
    while True:
        checker("github.com/", "Github")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def hotmail(): # not done
    while True:
        menu()
        print(notdone)
        #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def yahoo(): # not done
    while True:
        menu()
        print(notdone)
        #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def pastebin():
    while True:
        checker("pastebin.com/u/", "Pastebin")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def steam(): 
    while True:
        global good
        global bad
        global count
        global i
        i = ''
        good = 0
        bad = 0
        count = 0
        menu()
        time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
        input1()
        menu()
        with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
            for line in a_file:
                global stripped_line
                count = count + 1
                stripped_line = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://steamid.io/lookup/{stripped_line}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(style.RESET + f"https://steamcommunity.com/id/{stripped_line}")
                    print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(style.RESET + "https://steamcommunity.com/id/"f"{stripped_line}")
                    print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                    with open("results/Reddit/" + time1 + ".txt", "a") as results:
                        results.write("https://steamcommunity.com/id/"f"{stripped_line}" + "\n")
                time.sleep(interval)
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def tumblr():
    while True:
        input1()
        menu()
        good = 0
        bad = 0
        count = 0
        time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
        
        with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
            for line in a_file:
                global stripped_line
                count = count + 1
                stripped_line = line.strip()
                sess = requests.Session()
                req = sess.get("https://" + f"{stripped_line}" + ".tumblr.com", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(style.RESET + "https://" + f"{stripped_line}" + ".tumblr.com")
                    print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(style.RESET + "https://" + f"{stripped_line}" + ".tumblr.com")
                    print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                    with open("results/Tumblr/" + time1 + ".txt", "a") as results:
                        results.write("https://" + f"{stripped_line}" + ".tumblr.com\n")
                time.sleep(interval)
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def epicgames(): # not done
    while True:
        menu()
        print(notdone)
        #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def lastfm():
    while True:
        checker("last.fm/user/", "LastFM")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def xbox(): # not done
    while True:
        menu()
        print(notdone)
        #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def minecraft():
    while True:
        global i
        good = 0
        bad = 0
        count = 0
        time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
        i = ""
        input1()
        menu()
        makedirs()
        minecraft = 'Available-Later Available'.split()
        if os.path.isdir('results/Minecraft/Available-Later') and os.path.isdir('results/Minecraft/Available'):
            pass
        elif os.path.isdir('results/Minecraft/Available-Later') == False and os.path.isdir('results/Minecraft/Available') == False:
            for items in minecraft:
                path = os.path.join("results/Minecraft/", items)
                os.mkdir(path)
        with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
            for line in a_file:
                global stripped_line
                count = count + 1
                stripped_line = line.strip()
                url = f'https://faav-namemc-api.herokuapp.com/status/{stripped_line}'
                r = requests.get(url)
                if r.json()['success'] == True and r.json()['status'] == "unavailable":
                    bad = bad + 1
                    print(style.RESET + stripped_line)
                    print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

                elif r.json()['success'] == True:
                    if r.json()['status'] == 'available':
                        good = good + 1
                        print(style.RESET + stripped_line)
                        print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                        with open("results/Minecraft/Available/" + time1 + ".txt", "a") as results:
                            results.write(stripped_line + "\n")
                    elif r.json()['status'] == 'available_later':
                        good = good + 1
                        print(style.RESET + stripped_line)
                        print(style.GREEN + "[+] " + style.RESET + " Username available soon" + "\n")
                        with open("results/Minecraft/Available-Later/" + time1 + ".txt", "a") as results:
                            results.write(stripped_line + " - Available on " + str(datetime.datetime.fromtimestamp(r.json()['unix'] / 1000)) + "\n")
                time.sleep(interval)   
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def txties():
    while True:
        checker("txti.es/", "txti.es")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def tellonym():
    while True:
        checker("tellonym.me/", "Tellonym")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def krunker():
    while True:
        global i
        good = 0
        bad = 0
        count = 0
        time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
        i = ""
        input1()
        menu()
        with open('wordlists/' + wordlist1 + '.txt', "r") as a_file:
            for line in a_file:
                global stripped_line
                count = count + 1
                stripped_line = line.strip()
                url = f'https://kr.vercel.app/api/profile?username={stripped_line}&raw=false'
                url1 = "krunker.io/social.html?p=profile&q="
                r = requests.get(url)
                if r.text == "Internal Server Error" or len(stripped_line) <= 2:
                    bad = bad + 1
                    print(style.RESET + "https://" + url1 + f"{stripped_line}")
                    print(style.RED + "[-] " + style.RESET + " Username not available" + "\n")

                elif r.json()['success'] == False:
                    if r.json()['error'] == 'Player not found':
                        good = good + 1
                        print(style.RESET + "https://" + url1 + f"{stripped_line}")
                        print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                        with open("results/Krunker/" + time1 + ".txt", "a") as results:
                            results.write("https://" + url1 + f"{stripped_line}" + "\n")
                
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def rentry():
    while True:
        checker("rentry.co/", "Rentry")
        menu()
        print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
        exec(getch1)
        exec(mainfunc)
        break

def main():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 1/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Soundcloud\n(2) Twitter\n(3) WeHeartIt\n(4) Rentry\n(5) Tiktok - not done\n(6) Tellonym\n(7) Reddit\n(8) Twitch\n(9) Go to the next page\n(10) Quit\nChoice: "))
            if choice==1:
                soundcloud()
                break
            elif choice==2:
                twitter()
                break
            elif choice==3:
                weheartit()
                break
            elif choice==4:
                rentry()
                break
            elif choice==5:
                tiktok()
                break
            elif choice==6:
                tellonym()
                break
            elif choice==7:
                reddit()
                break
            elif choice==8:
                twitch()
                break
            elif choice==9:
                main2()
                break
            elif choice==10:
                os.system(clear)
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                exec(getch1)
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            exec(getch1)
            continue

def main2():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 2/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Behance\n(2) Solo.to\n(3) Linktree\n(4) Snapchat - not done\n(5) Github\n(6) Hotmail/Outlook - checks all TLDS\n(7) Yahoo - checks all TLDS\n(8) Pastebin\n(9) Go to the next page\n(10) Go to the previous page\nChoice: "))
            if choice==1:
                behance()
                break
            elif choice==2:
                soloto()
                break
            elif choice==3:
                linktree()
                break
            elif choice==4:
                snapchat()
                break
            elif choice==5:
                github()
                break
            elif choice==6:
                hotmail()
                break
            elif choice==7:
                yahoo()
                break
            elif choice==8:
                pastebin()
                break
            elif choice==9:
                main3()
                break
            elif choice==10:
                os.system(clear)
                main()
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                exec(getch1)
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            exec(getch1)
            continue

def main3():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 3/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Steam\n(2) Tumblr\n(3) Epic Games - not done\n(4) LastFM\n(5) Xbox - not done\n(6) Krunker\n(7) Minecraft\n(8) txti.es\n(9) Go to the next page\n(10) Go to the previous page\nChoice: "))
            if choice==1:
                steam()
                break
            elif choice==2:
                tumblr()
                break
            elif choice==3:
                epicgames()
                break
            elif choice==4:
                lastfm()
                break
            elif choice==5:
                xbox()
                break
            elif choice==6:
                krunker()
                break
            elif choice==7:
                minecraft()
                break
            elif choice==8:
                txties()
                break
            elif choice==9:
                main4()
                break
            elif choice==10:
                main2()
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                exec(getch1)
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            exec(getch1)
            continue

def main4():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 4/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Placeholder\n(2) Go to the previous page\nChoice: "))
            if choice==1:
                menu()
                print(notdone)
                exec(getch1)
                main()
                break
            elif choice==2:
                main3()
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                exec(getch1)
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            exec(getch1)
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