import os
import platform
import requests
import datetime
import time

operatingsys = platform.system()
if operatingsys == 'Windows':
    import msvcrt
    clear = 'cls'
    getch1 = 'msvcrt.getch()'
elif operatingsys == 'Linux' or 'Darwin':
    from getch import getch # type:ignore
    clear = 'clear'
    getch1 = 'getch()'

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
    sites = "Behance EpicGames Github Hotmail Twitch Krunker LastFM Linktree Minecraft Pastebin Reddit Rentry Roblox Snapchat Solo.to Soundcloud Steam Tellonym Tiktok Tumblr Twitter WeHeartIt Xbox Yahoo txti.es".split()
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
    global wordlist1
    global interval
    global i
    i = ""
    menu()
    wordlist1 = str(input("What is the name of the wordlist you want to use?\n"))
    menu()
    interval = float(input("What delay do you want to have inbetween checks?\n(This is helpful to avoid ratelimiting & anti-spam measures on some sites.)\n"))

def soundcloud():
    checker("soundcloud.com/", "Soundcloud")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def twitter(): # not done
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
                print(style.RESET + "https://twitter.com"f"{stripped_line}")
                print(style.GREEN + "[+] " + style.RESET + " Username available" + "\n")
                with open("results/Twitter/" + time1 + ".txt", "a") as results:
                    results.write("https://twitter.com"f"{stripped_line}" + "\n")
            time.sleep(interval)
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def weheartit():
    checker("weheartit.com/", "WeHeartIt")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def tiktok(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def twitch(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def reddit(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def behance():
    checker("behance.net/", "Behance")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def soloto(): 
    checker("solo.to/", "Solo.to")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def linktree():
    checker("linktr.ee/", "Linktree")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def snapchat(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def github():
    checker("github.com/", "Github")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def hotmail(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def yahoo(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def pastebin():
    checker("pastebin.com/u/", "Pastebin")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def steam(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def tumblr():
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

def epicgames(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def lastfm(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def xbox(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def roblox(): # not done
    menu()
    print(notdone)
    #print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def minecraft(): # not done
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

def txties():
    checker("txti.es/", "txti.es")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def tellonym():
    checker("tellonym.me/", "Tellonym")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def krunker():
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

def rentry():
    checker("rentry.co/", "Rentry")
    menu()
    print("Checked " + str(count) + " users.\n\n" + style.GREEN + str(good) + style.RESET + " available.\n" + style.RED + str(bad) + style.RESET + " unavailable.\n\nPress any key to return to the main menu.")
    exec(getch1)

def main():
    while True:
        makedirs()
        os.system(clear)
        global i
        i = "                                                          page 1/4"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Soundcloud\n(2) Twitter\n(3) WeHeartIt\n(4) Rentry\n(5) Tiktok - not done\n(6) Tellonym\n(7) Reddit - not done\n(8) Twitch - not done\n(9) Go to the next page\n(10) Quit\nChoice: "))
            if choice==1:
                soundcloud()
                continue
            elif choice==2:
                twitter()
            elif choice==3:
                weheartit()
            elif choice==4:
                rentry()
            elif choice==5:
                tiktok()
            elif choice==6:
                tellonym()
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
            choice=int(input("Choose an option:\n(1) Behance\n(2) Solo.to\n(3) Linktree\n(4) Snapchat - not done\n(5) Github\n(6) Hotmail - not done\n(7) Yahoo - not done\n(8) Pastebin\n(9) Go to the next page\n(10) Go to the previous page\nChoice: "))
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
            choice=int(input("Choose an option:\n(1) Steam - not done\n(2) Tumblr\n(3) Epic Games - not done\n(4) LastFM - not done\n(5) Xbox - not done\n(6) Roblox - not done\n(7) Minecraft\n(8) txti.es\n(9) Go to the next page\n(10) Go to the previous page\nChoice: "))
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
            choice=int(input("Choose an option:\n(1) Krunker\n(2) Go to the previous page\nChoice: "))
            if choice==1:
                krunker()
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