# TALIA aka Totally Artificial Language Intelligence Assistant
import pyfiglet
from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import pickle
import sys
import datetime as dt
import os
import threading
import datetime
import requests
import pyjokes
import pyttsx3
import time
import wikipedia
import urllib.request
import re 
import webbrowser
from phue import Bridge
from ph_ip_address import bridge_ip_address
from googletrans import Translator, constants
from pprint import pprint
from requests_html import HTMLSession
from bs4 import BeautifulSoup as soup
import requests
from tqdm import tqdm
import pyautogui
import speedtest
from colorama import Fore, Back, Style
import random
import curses
import pyqrcode
import platform

engine = pyttsx3.init()
engine.setProperty('rate', 220) 

def TALIA_main():
    import time
    #For linux
    #os.chdir("..")
    with open('data/portfolio.pkl', 'rb') as f:#Access the prebuilt portfolio containing APPL & TSLA
        portfolio = pickle.load(f)
        print('\033[1;37m')
        welcome = pyfiglet.figlet_format("Welcome To T.A.L.I.A Messenger!")
        print(welcome)
        engine.say("Welcome To Talia Messenger!")
        import time
        time.sleep(2)
        print(r"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%**========+*#%@@@@@@@@@@@@
@@@@@@@@@@*+=++*********+*+==*%@@@@@@@@@
@@@@@@@%*=+++++##%%%%%%%#+++++++#@@@@@@@
@@@@@@*=+*=+%@@@@@@@@@@@@@@@#=**==@@@@@@
@@@@@+=**=%@@@@@@@@#=@@@@@@@@@==%++@@@@@
@@@@#=*+=%@@@@@@..======@@@@@@@+=*==@@@@
@@@@==*=*@@@@@@@.@@@@@@@@@@@@@@@==*=#@@@
@@@@==#=#@@@@@@@.+######@@@@@@@@==#=#@@@
@@@@==#=#@@@@@@@#######-+@@@@@@@==#=#@@@
@@@@==#=#@@@@@@@@@@@@@@++@@@@@@@==#=#@@@
@@@@*=*==@@@@@@@=======:*@@@@@@*=*++@@@@
@@@@@+=*++@@@@@@@@@#=@@@@@@@@@*+**+%@@@@
@@@@@%*+**+*%@@@@@@@@@@@@@@@%+***+%@@@@@
@@@@@@@%++**++*%@@@@@@@@%*+++*++*@@@@@@@
@@@@@@@@@#++****+++++++++****+*@@@@@@@@@
@@@@@@@@@@@@%*++********++**%@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
        print("-----------------------------------------------------")
        engine.say("Importing all preferences from home interface")
        
        for i in tqdm (range (101), #Update progress bar
               desc="Updating", 
               ascii=False, ncols=75):
            time.sleep(0.05)
        print("\n")
        print(Fore.CYAN +'Version: v2.0.3-public-beta-preview')
        print(Fore.WHITE)
        engine.say("Systems are now fully operational")
        engine.runAndWait()
        print(Fore.WHITE)
        print('Status: '+ Fore.GREEN + 'ONLINE')
        print(Fore.WHITE)
        now = datetime.datetime.now()
        print(now)
        print("\n")
        time.sleep(2)
        engine.say("Hi, How Can I Help?")
        print("Hi, How Can I Help? 💬")
        engine.runAndWait()

        def greeting():
            engine.say("Hi There!")
            print("Hi There! 👋")
            engine.runAndWait()

        def goodbye():
            engine.say("Bye! ")
            print("Bye! 👋")
            engine.runAndWait()
            sys.exit(0)

        def thanks():
            engine.say("You're Welcome")
            print("You're Welcome! 😇")
            engine.runAndWait()

        def name():
            engine.say("I'm TALIA")
            print("I'm TALIA 😇")
            engine.runAndWait()

        def tasp():
            engine.say("T.A.L.I.A stands for: Totally Artificial Language Intelligence System")
            print("T.A.L.I.A stands for: Totally Artificial Language Intelligence System 🙃")
            engine.runAndWait()

        def gettime():#Shows current time to user
            now = datetime.datetime.now()
            engine.say("The Current Time Is")
            print("The Current Time Is ⏰...")
            engine.say(now)
            print(now)
            engine.runAndWait()

        def date():#Shows the current date to user
            now = datetime.datetime.now()
            engine.say("The Date Today Is")
            print("The Date Today Is 📅...")
            engine.say(now)
            print(now)
            engine.runAndWait()

        def weather():#Shows the weather for the user by using https://www.wttr.in/
            engine.say("Which City Would You Like The Weather For?")
            engine.runAndWait()
            location = input("Which City Would You Like The Weather For ☁️?")
            engine.say('This Is The Weather For: ' + location)
            print('This Is The Weather For: ' + location)
            engine.runAndWait()
            url = 'https://wttr.in/{}'.format(location)
            res = requests.get(url)
            print(res.text)
        
        def joke():#Shows a random joke to the user
            engine.say("Here Is A Joke")
            print("Here's A Joke 🤣...")
            new_joke = pyjokes.get_joke(language="en", category="all")
            engine.say(new_joke)
            print(new_joke)
            engine.runAndWait()

        def wiki():#Wikipedia Search
            engine.say("What would you like to wiki search?")
            engine.runAndWait()
            query = input("What would you like to wiki search? 🔍 ")
            print (wikipedia.summary(query))
            engine.say("According to Wikipedia...")
            engine.say (wikipedia.summary(query))
            engine.runAndWait()
            
        def youtube():#YouTube Search
            engine.say("What would you like to YouTube search?")
            engine.runAndWait()
            search_keyword = input("What would you like to YouTube search? 🔍 ")
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            print("Here's what I found on YouTube 🌐...")
            engine.say("Here's what I found on YouTube...")
            print("https://www.youtube.com/watch?v="+video_ids[0])
            engine.runAndWait()

        def play_song():#Plays song through spotify
            import time
            engine.say("What song would you like to play?")
            song = input("What song would you like to play? 🎵 ")
            engine.runAndWait()
            os.system("spotify")
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.write(song, interval = 0.1)
            for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
                time.sleep(2)
                pyautogui.hotkey(key)
            print("Playing "+song+" on Spotify...")
            engine.say("Playing "+song+" on Spotify!")
            engine.runAndWait()
            

        def app():#NEED TO FIX!!!
            engine.say("What would you like to open?")
            response = input("What would you like to open? 🖥️ ")
            engine.say("Sorry Open Command is unavailable at the moment!")
            print(Fore.RED + 'Sorry Open Command is unavailable atm 😥!')
            print(Fore.WHITE)
            #if "youtube" or "yt" or "YouTube" or "you tube" or "You Tube" in response:
            #    engine.say("Opening YouTube...")
            #    webbrowser.open("youtube.com")
            #elif "google" in response:
            #    engine.say("Opening Google...")
            #    webbrowser.open("google.com")
            # "stackoverflow" or "stack overflow" in response:
            #engine.say("Opening Stackoverflow...")
            #    webbrowser.open("stackoverflow.com") 
            #elif "github" or "GitHub" in response:
            #    engine.say("Opening GitHub...")
            #    webbrowser.open("github.com")
            #elif "duckduckgo" in response:
            #    engine.say("Opening Duckduckgo...")
            #    webbrowser == ("duckduckgo.com")
            #else:
            #    engine.say("Sorry I don't understand!")
            #    print("Sorry I don't understand!")
            engine.runAndWait()
      
        def access_lights(bridge_ip_address):
            b = Bridge(bridge_ip_address)
            light_names_list = b.get_light_objects('name')
            return light_names_list

        def philips_hue():#Controls Philips Hue Lights
            b = Bridge(bridge_ip_address)
            b.connect()
            print("Here are the current lights you can control 💡:")
            engine.say("Here are the current lights you can control:")
            engine.runAndWait()
            lights = b.lights
            for l in lights:
                print(l.name)#Lists all available lights to control
                engine.say(l.name)
            engine.say("What would you like to do?")
            engine.runAndWait()
            response = input("What would you like to do 💬?")
            if response in ['turn off all lights', 'turn off', 'turn off light']:#Turns off lights
                lights = access_lights(bridge_ip_address)
                for light in lights:
                    lights[light].on = False
                print("Turning off all the light")
                engine.say("Turning off all the light")
                engine.runAndWait()
            elif response in ['turn on all lights', 'turn on', 'turn on light']:#Turns on lights
                lights = access_lights(bridge_ip_address)
                for light in lights:
                    lights[light].on = True
                print("Turning on all the light")
                engine.say("Turning on all the light")
                engine.runAndWait()
            else:
                engine.say("Sorry only turning on and off commands are avaliable at the moment!")
                print("Sorry only turning on and off commands are available atm 😥!")
            engine.runAndWait()
            
        def translate():#Translates given text to another language
            translator = Translator()
            engine.say("What langauge would you like to translate to?")
            engine.runAndWait()
            language = input("What language would you like to translate to 🌍?")
            engine.say("Type the phrase you would like to translate: ")
            engine.runAndWait()
            response = input("Type the phrase you would like to translate: ")
            translation = translator.translate((response), dest=(language))
            engine.say(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
            engine.runAndWait()
            print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
            
        def news():#NEED TO FIX!!!
            from requests_html import HTMLSession
            session = HTMLSession()
            url = 'https://news.google.com/topstories'#Shows news from Google News
            r = session.get(url)
            r.html.render(sleep=1, scrolldown=2)
            articles = r.html.find('article')
            newslist = []
            for item in articles:
                try:
                    newsitem = item.find('h3', first=True)
                    newsarticle = {
                    'title' : newsitem.text,
                    'link': newsitem.absolute_links
                    }
                    newslist.append(newsarticle)
                except:
                    pass
            print("Here's the latest news...")
            engine.say("Here is the latest news")
            engine.runAndWait()
            print(newslist)

        def covid():#Shows covid-19 data to user
            url = "https://www.worldometers.info/coronavirus/"
            r = requests.get(url)
            s = soup(r.text, "html.parser")
            data = s.find_all("div", class_="maincounter-number")
            status = s.find_all("div", class_="number-table-main")
            active = s.find_all("span", class_="number-table")
            per = s.find_all("strong")
            country = s.find_all("td")
            cou=[]

            for a in country:
                cou.append(a.text)
            print("Please Enter Country Name 😷:")
            time.sleep(1)
            c=input().title()
            if c=="":
                c="World"
            b=cou.index(c)
            print("Showing Covid-19 Data for "+c)
            engine.say("Showing Covid-19 Data for"+c)
            print(cou[b].upper()+" Total Number Of Cases:"+cou[b+1]+"   New Number Of Cases:"+cou[b+2]+"   Total Number Of Deaths:"+cou[b+3]+"   New Number Of Deaths:"+cou[b+4]+" Number Of People Recovered:"+cou[b+5]+"   Active Number Of Cases:"+cou[b+6]+"   Serious Number Of Cases:"+cou[b+7]+"   cases/1Mpop:"+cou[b+8]+"   deaths/1Mpop:"+cou[b+9]+"   tests:"+cou[b+10]+"  tests/1Mpop:"+cou[b+11])
            print("\nGlobal Results")
            print("Total Number Of Cases: " + data[0].text.strip())
            print("Total Number Of Deaths: " + data[1].text.strip())
            print("Total Number Of Recovered: " + data[2].text.strip())
            print("Active Number Of Cases: " + status[0].text.strip() + "\t\t--Mild: " + active[0].text.strip() + " (" + per[
                2].text.strip() + "%)\t\t--Critical: " + active[1].text.strip() + " (" + per[3].text.strip() + "%)")
            print("Closed Cases: " + status[1].text.strip() + "\t\t--Discharged: " + active[2].text.strip() + " (" + per[
                4].text.strip() + "%)\t--Deaths: " + active[3].text.strip() + " (" + per[5].text.strip() + "%)\n")
            time.sleep(2)
            engine.say("The Data Used Is From: https://www.worldometers.info/coronavirus/")
            engine.say("For More Information On Covid-19, Please Visit: https://www.nhs.uk/conditions/coronavirus-covid-19/")
            print("The Data Used Is From: https://www.worldometers.info/coronavirus/")
            print("For More Information On Covid-19, Please Visit: https://www.nhs.uk/conditions/coronavirus-covid-19/")
            engine.runAndWait()

        def speed_test():#Speed test
            engine.say("Sped test currently offline")
            print('Speed test currently' +Fore.WHITE+ 'OFFLINE')
            print(Fore.WHITE)
            engine.runAndWait()
        #    test = speedtest.Speedtest()
        #    engine.say("Getting server list")
        #    print("Getting server list...")
        #    test.get_servers()#Gets current list of servers that can be tested
        #    engine.say("Choosing best server")
        #    print("Choosing best server to test...")
        #    best = test.get_best_server()#Gets the best server to test
        #    print(f"Found: {best['host']} loacted in {best['country']}")
        #    print("Perfoming speed test...")
        #    download_result = test.download()
        #    upload_result = test.upload()
        #   ping_result = test.results.ping_result
        #    engine.say(f"Download speed: {download_result/1024/1024:.2f} Mbit/s")
        #    engine.say(f"Upload speed: {upload_result/1024/1024:.2f} Mbit/s")
        #    engine.say(f"Ping: {ping_result:.2f} ms")
        #    print(f"Download speed: {download_result/1024/1024:.2f} Mbit/s")
        #print(f"Upload speed: {upload_result/1024/1024:.2f} Mbit/s")
        #    print(f"Ping: {ping_result:.2f} ms")
        #   engine.runAndWait()

        def help():#Shows help commands to user
            print("Here are some commands you can ask me 😃: ")
            engine.say("Here are some commands you can ask me ")
            engine.runAndWait()
            commands = ["time", "date", "weather", "clear", "joke", "wiki", "app", "youtube", "song", "lights", "translate", "wordle", "news", "covid", "plot chart", "add stock", "remove stock", "portfolio value", "stock value"]
            print('\n'.join(commands))
            engine.say('\n'.join(commands))
            engine.runAndWait()

        def version():
            print(Fore.CYAN)
            print("About Talia")
            print(Fore.WHITE)
            text = pyqrcode.create('https://github.com/T-Kalv/Tasp-Talia-')
            print(text.terminal(module_color='white', background='black'))
            time.sleep(1)
            my_system = platform.uname()
            print()
            print(f"OS: {my_system.system}")
            print(f"Device Name: {my_system.node}")
            print(f"Machine: {my_system.machine}")
            print(f"Processor: {my_system.processor}\n")
            print(Fore.YELLOW)
            print("Software Version Number: v2.0.3-public-beta-preview")
            print("Software Type: Public-Beta-Preview")
            print(Fore.GREEN)
            print("Last Update: 07/10/2022")
            print(Fore.WHITE)
            

        def wordle():

            def checkwordle(theAnswer, theGuess):
                position = 0
                hint = ""
                colours = []
                for letter in theGuess:
                    if letter == theAnswer[position]:
                        hint += "G"
                        colours.append(Fore.GREEN)
                    elif letter in theAnswer:
                        hint += "Y"
                        colours.append(Fore.YELLOW)
                    else:
                        hint += "#"
                        colours.append(Fore.WHITE)
                    position +=1
                print(
                    colours[0]+theGuess[0]+Fore.RESET+
                    colours[1]+theGuess[1]+Fore.RESET+
                    colours[2]+theGuess[2]+Fore.RESET+
                    colours[3]+theGuess[3]+Fore.RESET+
                    colours[4]+theGuess[4]+Fore.RESET
                    )
                return hint == "GGGGG"


            wordle_list = []
            wordle_file = open("wordle_words.txt")
            for word in wordle_file:
                wordle_list.append(word.strip())
            answer = random.choice(wordle_list)
            number_of_guess = 0
            correct_guess = False
            print(Fore.WHITE)
            while number_of_guess < 6 and not correct_guess:
                guess = input("Enter a 5 letter word: ")
                engine.say("Enter a 5 letter word")
                print("\n")
                number_of_guess +=1
                correct_guess = checkwordle(answer, guess)
                print("\n")
            if correct_guess:
                engine.say("let's goooooooo! you correctly guessed the word in "+str(number_of_guess)+" tries")
                print("Let's goooooooooooo! You correctly guessed the word in "+str(number_of_guess)+" tries!")
            else:
                engine.say("Unfortunately, you have used up all of your guesses. The correct word to guess was "+answer)
                print("Unfortunately, you have used up all of your guesses. The correct word to guess was "+answer)
            engine.runAndWait()


        def snake():
            print("Add snake cli code!")

        def games():
            engine.say("Here are the games you can play")
            print("Here are the games you can play:")
            engine.say("wordle")
            print("wordle")
            engine.runAndWait()


        def qrcode():
            engine.say("Enter url or text to generate qr code")
            print("Enter URL or text to generate QR CODE: ")
            code = input()
            time.sleep(1)
            text = pyqrcode.create(code)
            engine.say("Here is your generated qr code")
            print(text.terminal(module_color='white', background='black'))
            engine.runAndWait()



        def clear():
            response = input("Would you like to clear the termial/cli 🥺 [Y/n]?")
            if response in ['y', 'Y']:
                if os.name == "nt":
                    os.system('cls')
                else:
                    os.system("clear")
                welcome = pyfiglet.figlet_format("Welcome To T.A.L.I.A Messenger!")
                print(welcome)
                print(r"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%**========+*#%@@@@@@@@@@@@
@@@@@@@@@@*+=++*********+*+==*%@@@@@@@@@
@@@@@@@%*=+++++##%%%%%%%#+++++++#@@@@@@@
@@@@@@*=+*=+%@@@@@@@@@@@@@@@#=**==@@@@@@
@@@@@+=**=%@@@@@@@@#=@@@@@@@@@==%++@@@@@
@@@@#=*+=%@@@@@@..======@@@@@@@+=*==@@@@
@@@@==*=*@@@@@@@.@@@@@@@@@@@@@@@==*=#@@@
@@@@==#=#@@@@@@@.+######@@@@@@@@==#=#@@@
@@@@==#=#@@@@@@@#######-+@@@@@@@==#=#@@@
@@@@==#=#@@@@@@@@@@@@@@++@@@@@@@==#=#@@@
@@@@*=*==@@@@@@@=======:*@@@@@@*=*++@@@@
@@@@@+=*++@@@@@@@@@#=@@@@@@@@@*+**+%@@@@
@@@@@%*+**+*%@@@@@@@@@@@@@@@%+***+%@@@@@
@@@@@@@%++**++*%@@@@@@@@%*+++*++*@@@@@@@
@@@@@@@@@#++****+++++++++****+*@@@@@@@@@
@@@@@@@@@@@@%*++********++**%@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
                print("-----------------------------------------------------")
                print("\n")
                print(Fore.WHITE)
                print('Status: '+ Fore.GREEN + 'ONLINE')
                print(Fore.WHITE)
                print("\n")
                now = datetime.datetime.now()
                print(now)
                print("\n")
                engine.say("Hi, How Can I Help?")
                print("Hi, How Can I Help? 💬")
                engine.runAndWait()
            elif response in ['n', 'N']:
                print("Ok 😌")
                engine.say("Ok")
                engine.runAndWait()
            else:
                print("Sorry I don't understand 😥")
                engine.say("Sorry I don't understand")
                engine.runAndWait()    

        def save_portfolio():
            with open('data/portfolio.pkl', 'wb') as f:
                pickle.dump(portfolio, f)
                          
        def update_portfolio():#Updates user stock portfolio
            print('\033[1;37m')
            engine.say("Which stock would you like to have")
            symbol = input("Which stock would you like to have 📈: ")#Stock/ticker
            engine.say("How many shares would you like to have")
            quantity = input("How many shares would you like to have: ")
            engine.runAndWait()
            if symbol in portfolio.keys():
                portfolio[symbol] += int(quantity)
            else:
                portfolio[symbol] = int(quantity)
                save_portfolio()

        def remove_portfolio():#Removes shares/stock from user stock portfolio
            print('\033[1;37m')
            engine.say("Which stock would you like to sell")
            symbol = input("Which stock would you like to sell 📉: ")
            engine.say("How many shares would you like to sell")
            quantity = input("How many shares would you like to sell: ")
            engine.runAndWait()
            if symbol in portfolio.keys():
                if int(quantity) <= portfolio[symbol]:
                    portfolio[symbol] -= int(quantity)
                    save_portfolio()
                else:
                    print(f"You don't own enough shares for {symbol}")
            else:
                print(f"You don't own any shares in {symbol}")
            
        def view_portfolio():#Shows stock portfolio to user
            print('\033[1;37m')
            engine.say("This is your current portfolio")
            print("This is you current portfolio: ")
            engine.runAndWait()
            for symbol in portfolio.keys():
                print(f"You currently own {portfolio[symbol]} shares in {symbol}")
            
        def chart_plot():#Shows stock chart to user
            print('\033[1;37m')
            engine.say("Enter a stock symbol")
            symbol = input("Enter a stock symbol: ")
            engine.say("Enter a start date in the DD/MM/YYYY format")
            begin_str = input("Enter a start date in the DD/MM/YYYY format 📅: ")
            engine.runAndWait()
            plt.style.use('dark_background')
            begin = dt.datetime.strptime(begin_str, "%d/%m/%Y")
            finish = dt.datetime.now()
            data = web.DataReader(symbol, 'yahoo', begin, finish)
            colors = mpf.make_marketcolors(up='#00ff00', down='#ff0000', wick='inherit', edge='inherit', volume='in')
            mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
            chart_proc = threading.Thread(target=open_graph,args=[data,mpf_style],daemon=True)
            chart_proc.start()

        def portfolio_value():#Shows value of stock portfolio to user
            print('\033[1;37m')
            sum = 0
            for symbol in portfolio.keys():
                data = web.DataReader(symbol, 'yahoo')
                price = data['Close'].iloc[-1]
                sum += price
            print(f"Your current portfolio is valued at 💲{sum} USD")
            
        def portfolio_gains():#Shows stock gains
            print('\033[1;37m')
            engine.say("Please enter the starting date in the YYYY-MM-DD format")
            start_date = input("Please enter the starting date in the YYYY-MM-DD format 📅: ")
            engine.runAndWait()
            try:
                for symbol in portfolio.keys():
                    data = web.DataReader(symbol, 'yahoo')
                    current_price = data['Close'].iloc[-1]
                    start_price = data.loc[data.index == start_date]['Close'].values[0]
                    current_sum += current_price
                    start_sum += start_price
                print(f"Your portfolio gains are: 💲{current_sum-start_sum} USD")
            except IndexError:
                engine.say("ERROR No Trades On This Date!")
                print("ERROR No Trades On This Date! 😥")

        def understand():
            engine.say("Sorry I don't understand!")
            print("Sorry I don't understand! 😥")
            engine.runAndWait()
        
        mappings = {
            'greeting': greeting,
            'goodbye': goodbye,
            'thanks': thanks,
            'help': help,
            'name': name,
            'tasp': tasp,
            'time': gettime,
            'date': date,
            'joke': joke,
            'getweather': weather,
            'wiki': wiki,
            'youtube': youtube,
            'play_song': play_song,
            'app': app,
            'version': version,
            'philips_hue': philips_hue,
            'translate': translate,
            'news': news,
            'covid': covid,
            'speed_test': speed_test,
            'wordle': wordle,
            'snake': snake,
            'games': games,
            'qrcode': qrcode,
            'clear': clear,
            'understand': understand,
            'chart_plot': chart_plot,
            'update_portfolio': update_portfolio,
            'remove_portfolio': remove_portfolio,
            'view_portfolio': view_portfolio,
            'portfolio_gains': portfolio_gains,
            "portfolio_value": portfolio_value
        }
        tasp = GenericAssistant('data/intents.json', mappings, "TALIA_Messenger_Model")#Uses the pre-trained TALIA model to enable AI-like messaging using TALIA
        os.chdir("data")
        tasp.load_model()
        os.chdir("..")
        #For re-training TALIA model below!
        #tasp.train_model()
        #tasp.save_model()
        while True:
            text = input("")
            tasp.request(text)

    def open_graph(data, mpf_style):
        mpf.plot(data, type='candle', style=mpf_style, volume=True)

