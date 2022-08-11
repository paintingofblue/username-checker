import os
import platform
import requests
import datetime
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By



operatingsys = platform.system()
if operatingsys == "Windows":
    import msvcrt
    clear = "cls"
    getchinput = "msvcrt.getch()"
    mainfunc = "page1()"
elif operatingsys == "Linux" or "Darwin":
    from getch import getch # type:ignore
    clear = "clear"
    getchinput = "getch()"
    mainfunc = "page1()"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

notdone = "This site isnt done.\n\nPress any key to return to the main menu."

class style():
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

def makedirs():
    sites = "Behance EpicGames Github Hotmail Twitch Krunker OGUsers LastFM Linktree Minecraft Pastebin Reddit Rentry Snapchat Solo.to Soundcloud Steam Tellonym Tiktok Tumblr Twitter WeHeartIt Xbox Yahoo txti.es".split()
    if os.path.isdir("results"):
        pass
    elif os.path.isdir("results") == False:
        os.system("mkdir results")
        for items in sites:
            path = os.path.join("results/", items)
            os.mkdir(path)
    if os.path.isdir("wordlists"):
        pass
    elif os.path.isdir("wordlists") == False:
        os.system("mkdir wordlists")

def checker(website, resultsdir):
    global good
    global bad
    global count
    good = 0
    bad = 0
    count = 0
    currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
    userinput()
    menu()
    with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
        for line in wordlistfile:
            global username
            count = count + 1
            username = line.strip()
            sess = requests.Session()
            req = sess.get(f"https://{website}{username}", headers=HEADERS)

            if req.status_code == 200:
                bad = bad + 1
                print(f"{style.RESET}https://{website}{username}")
                print(f"{style.RED}[-] {style.RESET} Username not available\n")

            elif req.status_code == 404:
                good = good + 1
                print(f"{style.RESET}https://{website}{username}")
                print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                with open(f"results/{resultsdir}/{currentdate}.txt", "a") as results:
                    results.write(f"https://{website}{username}\n")
            time.sleep(interval)

def userinput():
    while True:
        global wordlistname
        global interval
        global pagenumber
        pagenumber = ""
        menu()
        wordlistname = str(input("What is the name of the wordlist you want to use?\n(Note that the program automatically appends .txt to your input.)\n"))
        try:
            open(f"wordlists/{wordlistname}.txt", "r")
            pass
        except:
            menu()
            print("The file you entered either doesnt exist or was incorrectly entered.\nPlease try again.\n\nPress any key to continue.")
            exec(getchinput)
            exec(mainfunc)
            break
        menu()
        interval = float(input("What delay do you want to have inbetween checks?\n(This is helpful to avoid ratelimiting & anti-spam measures on some sites.)\n"))
        break

def soundcloud():
    while True:
        checker("soundcloud.com/", "Soundcloud")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def twitter():
    while True:
        global good
        global bad
        global count
        global pagenumber
        pagenumber = ""
        good = 0
        bad = 0
        count = 0
        menu()
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        userinput()
        menu()
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://nitter.it/{username}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(f"{style.RESET}https://twitter.com/{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(f"{style.RESET}https://twitter.com/{username}")
                    print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                    with open(f"results/Twitter/{currentdate}.txt", "a") as results:
                        results.write(f"https://twitter.com/{username}\n")
                time.sleep(interval)
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break
    

def weheartit():
    while True:
        checker("weheartit.com/", "WeHeartIt")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def tiktok():
    while True:
        global pagenumber
        good = 0
        bad = 0
        count = 0
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        pagenumber = ""
        userinput()
        menu()
        
        options = uc.ChromeOptions()
        options.headless=True
        options.add_argument('--headless')
        driver = uc.Chrome(options=options)
        
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                driver.get(f'https://tiktok.com/@{username}')
                try:
                    if driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/main/div/p[1]').text == "Couldn't find this account":
                        good = good + 1
                        print(f"{style.RESET}https://tiktok.com/@{username}")
                        print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                        with open(f"results/Tiktok/{currentdate}.txt", "a") as results:
                            results.write(f"https://tiktok.com/@{username}\n")
                except:
                    bad = bad + 1
                    print(f"{style.RESET}https://tiktok.com/@{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")
                time.sleep(interval)   
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def twitch():
    while True:
        global good
        global bad
        global count
        global pagenumber
        pagenumber = ""
        good = 0
        bad = 0
        count = 0
        menu()
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        userinput()
        menu()
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://twitchtracker.com/{username}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(f"{style.RESET}https://twitch.tv/{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(f"{style.RESET}https://twitch.tv/{username}")
                    print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                    with open(f"results/Twitch/{currentdate}.txt", "a") as results:
                        results.write(f"https://twitch.tv/{username}\n")
                time.sleep(interval)
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def reddit():
    while True:
        global good
        global bad
        global count
        global pagenumber
        pagenumber = ""
        good = 0
        bad = 0
        count = 0
        menu()
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        userinput()
        menu()
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://libredd.it/user/{username}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(f"{style.RESET}https://www.reddit.com/u/{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(f"{style.RESET}https://www.reddit.com/u/{username}")
                    print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                    with open(f"results/Reddit/{currentdate}.txt", "a") as results:
                        results.write(f"https://www.reddit.com/u/{username}\n")
                time.sleep(interval)
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def behance():
    while True:
        checker("behance.net/", "Behance")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def soloto(): 
    while True:
        checker("solo.to/", "Solo.to")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def linktree():
    while True:
        checker("linktr.ee/", "Linktree")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def snapchat(): # not done
    while True:
        menu()
        print(notdone)
        #print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def github():
    while True:
        checker("github.com/", "Github")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def hotmail(): # not done
    while True:
        menu()
        print(notdone)
        #print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def yahoo(): # not done
    while True:
        menu()
        print(notdone)
        #print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def pastebin():
    while True:
        checker("pastebin.com/u/", "Pastebin")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def steam(): 
    while True:
        global good
        global bad
        global count
        global pagenumber
        pagenumber = ""
        good = 0
        bad = 0
        count = 0
        menu()
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        userinput()
        menu()
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://steamid.io/lookup/{username}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(f"{style.RESET}https://steamcommunity.com/id/{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(f"{style.RESET}https://steamcommunity.com/id/{username}")
                    print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                    with open(f"results/Steam/{currentdate}.txt", "a") as results:
                        results.write(f"https://steamcommunity.com/id/{username}\n")
                time.sleep(interval)
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def tumblr():
    while True:
        userinput()
        menu()
        good = 0
        bad = 0
        count = 0
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://{username}.tumblr.com", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(f"{style.RESET}https://{username}.tumblr.com")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(f"{style.RESET}https://{username}.tumblr.com")
                    print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                    with open(f"results/Tumblr/{currentdate}.txt", "a") as results:
                        results.write(f"https://{username}.tumblr.com\n")
                time.sleep(interval)
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def epicgames(): # not done
    while True:
        menu()
        print(notdone)
        #print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def lastfm():
    while True:
        checker("last.fm/user/", "LastFM")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def xbox(): 
    while True:
        userinput()
        menu()
        good = 0
        bad = 0
        count = 0
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                sess = requests.Session()
                req = sess.get(f"https://xboxgamertag.com/search/{username}", headers=HEADERS)

                if req.status_code == 200:
                    bad = bad + 1
                    print(f"{style.RESET}{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif req.status_code == 404:
                    good = good + 1
                    print(f"{style.RESET}{username}")
                    print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                    with open(f"results/Xbox/{currentdate}.txt", "a") as results:
                        results.write(f"{username}\n")
                time.sleep(interval)
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def minecraft():
    while True:
        global pagenumber
        good = 0
        bad = 0
        count = 0
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        pagenumber = ""
        userinput()
        menu()
        makedirs()
        minecraft = "Available-Later Available".split()
        if os.path.isdir("results/Minecraft/Available-Later") and os.path.isdir("results/Minecraft/Available"):
            pass
        elif os.path.isdir("results/Minecraft/Available-Later") == False and os.path.isdir("results/Minecraft/Available") == False:
            for items in minecraft:
                path = os.path.join("results/Minecraft/", items)
                os.mkdir(path)
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                url = f"https://faav-namemc-api.herokuapp.com/status/{username}"
                r = requests.get(url)
                if r.json()["success"] == True and r.json()["status"] == "unavailable":
                    bad = bad + 1
                    print(f"{style.RESET}{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif r.json()["success"] == True:
                    if r.json()["status"] == "available":
                        good = good + 1
                        print(f"{style.RESET}{username}")
                        print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                        with open(f"results/Minecraft/Available/{currentdate}.txt", "a") as results:
                            results.write(f"{username}\n")
                    elif r.json()["status"] == "available_later":
                        good = good + 1
                        print(f"{style.RESET}{username}")
                        print(f"{style.GREEN}[+] {style.RESET} Username available soon\n")
                        with open(f"results/Minecraft/Available-Later/{currentdate}.txt", "a") as results:
                            results.write(f"{username} - Available on " + str(datetime.datetime.fromtimestamp(r.json()["unix"] / 1000)) + "\n")
                time.sleep(interval)   
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def txties():
    while True:
        checker("txti.es/", "txti.es")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def tellonym():
    while True:
        checker("tellonym.me/", "Tellonym")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def krunker():
    while True:
        global pagenumber
        good = 0
        bad = 0
        count = 0
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        pagenumber = ""
        userinput()
        menu()
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                url = f"https://kr.vercel.app/api/profile?username={username}&raw=false"
                website = "krunker.io/social.html?p=profile&q="
                r = requests.get(url)
                if r.text == "Internal Server Error" or len(username) <= 2:
                    bad = bad + 1
                    print(f"{style.RESET}https://{website}{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")

                elif r.json()["success"] == False:
                    if r.json()["error"] == "Player not found":
                        good = good + 1
                        print(f"{style.RESET}https://{website}{username}")
                        print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                        with open(f"results/Krunker/{currentdate}.txt", "a") as results:
                            results.write(f"https://{website}{username}\n")
                
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break
 
def rentry():
    while True:
        checker("rentry.co/", "Rentry")
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def ogusers():
    while True:
        global pagenumber
        good = 0
        bad = 0
        count = 0
        currentdate = str(datetime.datetime.now()).split(".")[0].replace(":", "-")
        pagenumber = ""
        userinput()
        menu()
        
        options = uc.ChromeOptions()
        options.headless=True
        options.add_argument('--headless')
        driver = uc.Chrome(options=options)
        
        with open(f"wordlists/{wordlistname}.txt", "r") as wordlistfile:
            for line in wordlistfile:
                global username
                count = count + 1
                username = line.strip()
                driver.get(f'https://ogu.gg/{username}')
                if "The member you specified is either invalid or doesn't exist." in driver.page_source:
                    good = good + 1
                    print(f"{style.RESET}https://ogu.gg/{username}")
                    print(f"{style.GREEN}[+] {style.RESET} Username available\n")
                    with open(f"results/OGUsers/{currentdate}.txt", "a") as results:
                        results.write(f"https://ogu.gg/{username}\n")
                else:
                    bad = bad + 1
                    print(f"{style.RESET}https://ogu.gg/{username}")
                    print(f"{style.RED}[-] {style.RESET} Username not available\n")
                time.sleep(interval)   
        menu()
        print(f"Checked {str(count)} users.\n\n{style.GREEN}{str(good)}{style.RESET} available.\n{style.RED}{str(bad)}{style.RESET} unavailable.\n\nPress any key to return to the main menu.")
        exec(getchinput)
        exec(mainfunc)
        break

def page1():
    while True:
        makedirs()
        os.system(clear)
        global pagenumber
        pagenumber = "                                                          page 1/3"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Soundcloud\n(2) Twitter\n(3) WeHeartIt\n(4) Rentry\n(5) Tiktok\n(6) Tellonym\n(7) Reddit\n(8) Twitch\n(9) Go to the next page\n(10) Quit\nChoice: "))
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
                page2()
                break
            elif choice==10:
                os.system(clear)
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                exec(getchinput)
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            exec(getchinput)
            continue

def page2():
    while True:
        makedirs()
        os.system(clear)
        global pagenumber
        pagenumber = "                                                          page 2/3"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Behance\n(2) Solo.to\n(3) Linktree\n(4) Snapchat - not done\n(5) Github\n(8) txti.es\n(9) OGU\n(8) Pastebin\n(9) Go to the next page\n(10) Go to the previous page\nChoice: "))
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
                txties()
                break
            elif choice==7:
                ogusers()
                break
            elif choice==8:
                pastebin()
                break
            elif choice==9:
                page3()
                break
            elif choice==10:
                os.system(clear)
                page1()
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                exec(getchinput)
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            exec(getchinput)
            continue

def page3():
    while True:
        makedirs()
        os.system(clear)
        global pagenumber
        pagenumber = "                                                          page 3/3"
        menu()
        try:
            choice=int(input("Choose an option:\n(1) Steam\n(2) Tumblr\n(3) Epic Games - not done\n(4) LastFM\n(5) Xbox\n(6) Krunker\n(7) Minecraft\n(8) Go to the previous page\nChoice: "))
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
                page2()
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                exec(getchinput)
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            exec(getchinput)
            continue

def menu():
    global pagenumber
    os.system(clear)
    print(f"""
  _    _  _____ ______ _____  _   _          __  __ ______  _____ 
 | |  | |/ ____|  ____|  __ \| \ | |   /\   |  \/  |  ____|/ ____|
 | |  | | (___ | |__  | |__) |  \| |  /  \  | \  / | |__  | (___  
 | |  | |\___ \|  __| |  _  /| . ` | / /\ \ | |\/| |  __|  \___ \ 
 | |__| |____) | |____| | \ \| |\  |/ ____ \| |  | | |____ ____) |
  \____/|_____/|______|_|  \_\_| \_/_/    \_\_|  |_|______|_____/ 
                                                                  
                                 made by github.com/paintingofblue
{pagenumber}
__________________________________________________________________
""")
    pagenumber = ""

if __name__ == "__main__":
    page1()