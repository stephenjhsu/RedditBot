from string import ascii_letters
import praw
import time
from random import randint
from graphics import *
r = praw.Reddit('owijaowijaowejgwoeijfoweijf')
r.login('cs61a-1', 'cs61a101814')
dangerous_citizen_review_list = []
dangerous_citizen_list = []



class Data():
#Databases for judging connotation

    complete_data = {}

    red_list = {"department": -0.5, "security": -.5, "dhs": -0.5, "customs": -0.7, "protection": -0.7, "cbp": -0.7, "border": -0.6, 
                     "patrol": -0.7, "secret": -1, "usss": -1, "noc": -0.8, "defense": -0.8, "cia": -1, "investigation": -0.6, "fbi": -1, 
                     "firearms": -0.5, "emergency": -0.9, "federal": -0.6, "tsa": -0.9, "faa": -0.8, "guard": -0.5, "assassination": -1, 
                     "attack": -1, "security": -0.6, "dndo": -1, "nuclear": -1, "mitigation": -0.8, "bomb": -1, "militia": -0.9, "shooting": -0.9,
                     "deaths": -0.6, "hostage": -1, "explosion": -0.8, "explosives": -0.9, "dmat": -0.5, "gangs": -0.5, "ebola": -0.8, "cdc": -0.7,
                     "debt": -0.5, "crime": -0.5, "radiation": -0.9, "radioactive": -0.7, "infection": -0.7, "epidemic": -1, "anthrax": -1, 
                     "nerve": -0.5, "ricin": -1, "sarin": -1, "korea": -1, "outbreak": -1, "contamination": -0.7, "virus": -0.5, 
                     "evacuation": -0.5, "bacteria": -0.5, "recall": -0.5, "poisoning": -0.6, "avian": -0.8, "plague": -0.8, "influenza": -0.7, 
                     "fda": -0.6, "tuberculosis": -0.6, "listeria": -0.7, "mutation": -0.9, "resistant": -0.8, "pandemic": -1, "infection": -0.7,
                     "swine": -0.6, "quarantine": -0.8, "infrastructure": -0.9, "norvo": -0.6, "hemorrhagic": -0.8, "coli": -0.5, 
                     "collapse": -0.5, "telecommunications": -0.6, "wmata": -0.8, "cikr": -1, "nbic": -1, "decapitated": -0.8, "army": -0.6, 
                     "execution": -0.7, "gunfight": -0.7, "kidnap": -0.5, "qaeda": -1, "afghanistan": -1, "iran": -1, "pakistan": -1, 
                     "egypt": -1, "hamas": -1, "farc": -1, "ira": -1, "eta": -1, "basque": -1, "seperatists": -1, "hezbollah": -1, "tamil": -1,
                     "tigers": -1, "plf": -1, "plo": -1, "jihad": -1, "taliban": -1, "suicide": -0.8, "aqap": -1, "aqim": -1, "ttp": -1, 
                     "yemen": -0.7, "pirates": -0.8, "extremism": -0.9, "somalia": -0.7, "nigeria": -0.6, "radicals": -0.6, "nationalist": -0.5, 
                     "recruitment": -0.5, "fundamentalism": -0.7, "islamist": -1, "magnitude": -0.6, "warning": -0.5, "botnet": -0.8, 
                     "ddos": -0.9, "malware": -0.7, "trojan": -0.6, "hacker": -0.9, "china": -0.7, "worm": -0.7, "scammers": -0.8}

    yellow_list = {"agency": -0.3, "fema": -0.3, "coast": -0.1, "immigration": -0.3, "enforcement": -0.1, "ice": -0.1, "agent": -0.1, 
                        "force": -0.3, "dea": -0.3, "sbi": -0.2, "drug": -0.4, "immigration": -0.2, "atf": -0.4, "cis": -0.3, "fams": -0.2, 
                        "domestic": -0.3, "drill": -0.2, "exercise": -0.2, "cops": -0.1, "law": -0.2, "enforcement": -0.3, "authorities": -0.4, 
                        "disaster": -0.4, "prepardness": -0.2, "dirty": -0.3, "mda": -0.2, "shots": -0.2, "fired": -0.2, "evacuation": -0.3, 
                        "breach": -0.4, "threat": -0.3, "swat": -0.4, "screening": -0.3, "lockdown": -0.4, "crash": -0.1, "looting": -0.4, 
                        "riot": -0.4, "incident": -0.2, "hazmat": -0.3, "chemical": -0.2, "suspicious": -0.2, "toxic": -0.1, "labratory": -0.2, 
                        "plume": -0.1, "hazardous": -0.2, "agent": -0.4, "exposure": -0.4, "flu": -0.1, "salmonella": -0.3, "pox": -0.4, 
                        "public": -0.1, "terror": -0.4, "symptoms": -0.2, "antiviral": -0.3, "strain": -0.1, "vaccine": 0, "tamiflu": -0.3, 
                        "airport": -0.2, "amtrak": -0.2, "metro": -0.2, "bart": -0.2, "grid":-0.1, "power": -0.1, "narcotics": -0.3, 
                        "cocaine": -0.3, "marijuana": -0.2, "heroin": -0.3, "mexico": -0.4, "cartel": -0.4, "southwest": -0.3, "juarez": -0.4, 
                        "methamphetamine": -0.3, "shootout": -0.4, "trafficking": -0.2, "meth": -0.3, "illegal": -0.4, "smuggling": -0.4, 
                        "smugglers": -0.4, "weapon": -0.3, "enriched": -0.3, "ied": -0.4, "keylogger": -0.3, "spammer": -0.3, "phishing": -0.4, 
                        "rootkit": -0.4, "phreaking": -0.4, "cain": -0.2, "abel": -0.2, "brute": -0.3, "forcing": -0.4, "injection": -0.3, 
                        "cyber": -0.3}

    databases = [red_list, yellow_list]
    for base in databases:
        complete_data.update(base)

    def single_data(database):
        if database == "red":
            return red_list
        elif database == "yellow":
            return yellow_list

    def all_data():
        databases = [Data.red_list, Data.yellow_list]
        for base in databases:
            Data.complete_data.update(base)
        return Data.complete_data

def master_function():
    #print(r.is_logged_in())
    previous = []
    while True:
        this_set = get_new_posts(previous)      
        previous = this_set + previous
        print('new posts are gotten')
        n = 0
        for each in this_set:
            action(each)
            
            print(n)
            n += 1
        print('dangerous review=',dangerous_citizen_review_list)
        print('dangerous list=',dangerous_citizen_list)
        largest = [0,0]
        for each in dangerous_citizen_list:
            if each[1] > largest[1]:
                largest = each
        gui_graphics(len(dangerous_citizen_list), len(dangerous_citizen_review_list), largest[0].name)
#        time.sleep(90)


#---------------------------------------------------------

def get_new_posts(previous):
    #r = praw.Reddit(user_agent='my_cool_application')

    submissions = list(r.get_new(limit = 1000))

    if previous != []:
        for item in submissions[::-1]:
            if item in previous:
                submissions.remove(item)
            else:
                break
    return submissions
  
#---------------------------------------------------------


def extract(titles):
    """Extract and make lowercase all the words of the Reddit title.
    >>> t = ["GO #Bears!"]
    >>> extract(t)
    ['go', 'bears']
    """
    t = []
    for title in titles:
        for i in title:
            if i not in ascii_letters:
                title = title.replace(i, ' ')
        t += title.lower().split()
    return t


#---------------------------------------------------------
def get_color(title):
    d, lst, dictionary = 0, [], Data.all_data()
    for word in title:
        if word in dictionary:
            d += dictionary[word]
            lst.append(word)
    if len(lst) == 0:
        return 'green'
    lst_avg = d / len(lst)
    if lst_avg <= -.5:
        return 'red'
    if lst_avg > -.5 and lst_avg < 0:
        return 'yellow'
    return 'green' 

#---------------------------------------------------------

def action(submission):
    color = get_color(extract([submission.title]))
    if color == 'yellow':
        submission.downvote()
        
    elif color == 'red':
        submission.downvote()
        dangerous_citizen_review_list.append(submission.author)
        nam, num, dont = is_dangerous_citizen(submission.author)
        if nam:
            dangerous_citizen_list.append([num, dont])
            print('send to Gitmo')

def is_dangerous_citizen(redditor):
    submissions = list(redditor.get_submitted())
    dangerous_citizenic_count = 0
    for submission in submissions:
        if get_color(extract([submission.title])) == 'red':
            dangerous_citizenic_count += 1
    return (dangerous_citizenic_count > 1, submission.author, dangerous_citizenic_count)

#--------------------------------------------------------------
  
  
def gui_graphics(amount_red, amount_yellow, most_wanted):
    # func gui_graphics creates a windowed bar graph of the data
    win = GraphWin("Data Display", 750, 750)
    win.setBackground("black")
    win.setCoords(0, 0, 10, amount_yellow * 1.5)
    welcome_text = Text(Point(5, amount_yellow * 1.35), "Watchlist")
    welcome_text.setFill("green")
    welcome_text.setSize(36)
    most_wanted_textstr = Text(Point(2.75, amount_yellow), "Most Wanted:")
    most_wanted_textstr.setFill("pink")
    most_wanted_textstr.setSize(30)
    most_wanted_display = Text(Point(2.75, amount_yellow * .85), most_wanted)
    most_wanted_display.setFill("pink")
    most_wanted_display.setSize(30)
    start = amount_yellow * 0.15
    red_text = Text(Point(3.25, start - amount_yellow * 0.1), str(amount_red))
    red_text.setFill("red")
    red_text.setSize(20)
    red_box = Rectangle(Point(2, start), Point(4.5, (amount_red) + start))
    red_box.setFill("red")
    red_box.setOutline("white")
    yellow_text = Text(Point(6.75, start - amount_yellow * 0.1), str(amount_yellow))
    yellow_text.setFill("yellow")
    yellow_text.setSize(20)
    yellow_box = Rectangle(Point(5.5, start), Point(8, (amount_yellow) + start))
    yellow_box.setFill("yellow")
    yellow_box.setOutline("white")

    welcome_text.draw(win)
    most_wanted_textstr.draw(win)
    most_wanted_display.draw(win)
    red_text.draw(win)
    red_box.draw(win)
    yellow_text.draw(win)
    yellow_box.draw(win)
    win.getMouse()
    win.close()

def main():
    master_function()
    
main()
