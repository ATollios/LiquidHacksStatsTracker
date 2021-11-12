import requests
import json
import os
from tkinter import *
from tkinter import ttk
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen
import urllib.request

firstcycle = False
currGame = ''


def webScrabingTime():
    game = ComboboxGame.get()
    player = ComboboxPlayer.get()
    player = player.replace(" ", '')
    print(player)
    if game == 'apexlegends' or game == 'fortnite' or game == 'valorant' or game == 'rainbowsix' or game == 'leagueoflegends':
        if game == 'apexlegends':
            urlA = ('https://tracker.gg/apex/profile/origin/'+player+'/overview')
            pageApex = urlopen(url)
            HtmlA = pageApex.read()
            Htmla = HtmlA.decode("utf-8")
        if game == 'fortnite':
            urlF = 'https://fortnitetracker.com/profile/all/'+player
            pageFornite = urlopen(urlF)
            HtmlF = pageFornite.read()
            HtmlF = HtmlF.decode("utf-8")
        if game == 'valorant':
            pass
        if game == 'rainbowsix':
            urlR = 'https://r6.tracker.network/profile/pc/KrispyxChris'
            pageSiege = urlopen(urlRl)
            HtmlS = pageSiege.read()
            HtmlS = HtmlS.decode("utf-8")
        if game == 'leagueoflegends':
            try:

                urlL = 'https://tracker.gg/lol/profile/riot/NA/'+player+'/overview'
                requestL = urllib.request.Request(urlL, headers = {'User-Agent': 'Magic Browser'})
                pageLeague = urllib.request.urlopen(requestL)
                HtmlL = pageLeague.read()
                #HtmlL = HtmlL.decode("utf-8")
                print(HtmlL)
            except Exception as e:
                print(str(e))
def getStats(e):
    player = ComboboxPlayer.get()
    wiki = ComboboxGame.get()
    apiUrl = "https://api.liquipedia.net/api/v2/player"
    headers = {
        'authorization': 'Apikey 0NTexa4EtfeEFuBq6CGjvs8SaTs4ST18K3VRBCbNWBoBxa3G7Ma5zc5E4C2iuulucvjUVV6bX5H5pe9H3GlcKutmSiiNqJTnu5cmdjpIaLteas8tI2Cz91hKHW0aeOLz'}
    params = {'wiki': wiki, 'conditions': '[[pagename::'+player+']]','query': 'name, earnings, birthdate,status',  'limit': '10000000',}
    response = requests.get(apiUrl, headers=headers, params=params)
    response.json()
    data = response.text
    data = data.replace('"', "")
    data = data.replace("\\", "")
    data = data.replace("}", "\n")
    data = data.replace("{", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.replace("result:", "")
    data = data.replace(":", ": ")
    data = data.replace(",", ", ")
    print(data)

    KdHolder = data
    RankHolder = data
    StatusHolder = data
    EarningsHolder = data
    BirthdayHolder = data
    NameHolder = data

    ###Status Stuff#
    StatusBeg = StatusHolder.find('status:')
    StatusEnd = StatusHolder.find(', wiki')
    StatusHolder= StatusHolder[StatusBeg + 8 :StatusEnd]
    if StatusHolder != '' and StatusHolder != ' ' and StatusHolder != None and 'u0' not in StatusHolder:
        StatusLabel.config(text=StatusHolder, font = "Roboto 30", bg= '#79bbeb')
        StatusLabel.place(x=370, y=622)
    else:
        StatusLabel.config(text='Data Not Found', font = "Roboto 30", bg= '#79bbeb')
        StatusLabel.place(x=370, y=622)

    ###Earnings Stuff#
    EarninsBeg = EarningsHolder.find('earnings:')
    EarningsEnd = EarningsHolder.find(', birthdate')
    EarningsHolder = EarningsHolder[EarninsBeg + 10:EarningsEnd]
    if EarningsHolder != '' and EarningsHolder != ' ' and EarningsHolder != None and 'u0' not in EarningsHolder:
        EarningsLabel.config(text='$' + EarningsHolder, font = "Roboto 30", bg= '#79bbeb')
        EarningsLabel.place(x=390, y=722)
    else:
        EarningsLabel.config(text='Data Not Found', font = "Roboto 30", bg= '#79bbeb')
        EarningsLabel.place(x=390, y = 722)



    ###Birthday Stuff#
    BirthdayBeg = BirthdayHolder.find('birthdate:')
    BirthdayEnd = BirthdayHolder.find(', status')
    BirthdayHolder= BirthdayHolder[BirthdayBeg + 11 :BirthdayEnd]

    if BirthdayHolder != '' and BirthdayHolder != ' ' and BirthdayHolder != None and 'u0' not in BirthdayHolder or BirthdayHolder != '1970-01-01':
        BirthdayLabel.config(text=BirthdayHolder, font = "Roboto 30", bg= '#79bbeb')
        BirthdayLabel.place(x=385, y=822)
    else:
        BirthdayLabel.config(text='Data Not Found', font = "Roboto 30", bg= '#79bbeb')
        BirthdayLabel.place(x=385, y=822)


    ###Name Stuff#
    nameBeg = KdHolder.find('name:')
    nameEnd = KdHolder.find(', earnings')
    NameHolder= KdHolder[nameBeg + 6 :nameEnd]
    if NameHolder != '' and NameHolder != ' ' and NameHolder != None and 'u0' not in NameHolder:
        NameLabel.config(text=NameHolder, font = "Roboto 30", bg= '#79bbeb')
        NameLabel.place(x=365, y=922)

    else:
        NameLabel.config(text='Data Not Found',font = "Roboto 30", bg= '#79bbeb')
        NameLabel.place(x=365, y=922)

    if player == 'none':
        KDLabel.place_forget()
        RankLabel.place_forget()
        StatusLabel.place_forget()
        EarningsLabel.place_forget()
        BirthdayLabel.place_forget()
        NameLabel.place_forget()
    webScrabingTime()
def getPlayers(e):
    player = ComboboxPlayer.get()
    wiki = ComboboxGame.get()
    currentTeam = ComboboxTeam.get()
    apiUrl = "https://api.liquipedia.net/api/v2/player"
    headers = {
        'authorization': 'Apikey 0NTexa4EtfeEFuBq6CGjvs8SaTs4ST18K3VRBCbNWBoBxa3G7Ma5zc5E4C2iuulucvjUVV6bX5H5pe9H3GlcKutmSiiNqJTnu5cmdjpIaLteas8tI2Cz91hKHW0aeOLz'}
    params = {'wiki': wiki , 'query': 'team,id,name', 'limit': '10000000', 'order': 'team ASC, id ASC, name ASC'}
    response = requests.get(apiUrl, headers=headers, params=params)
    response.json()
    data = response.text
    data = data.replace('"', "")
    data = data.replace("\\", "")
    data = data.replace("}", "\n")
    data = data.replace("{", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.replace("result:", "")
    data = data.replace(":", ": ")
    data = data.replace(",", ", ")
    newf = open("sortedData.txt", "w")
    newf.write(data)

    finalfileIds = open("sortedData.txt", "r")
    idlist = []
    namelisttemp = []
    for line in finalfileIds:
        line = line[line.find(""):]
        slicelocend = line.find('name')
        slicelocbeg = line.find('team: ')
        line = line[slicelocbeg + 6:slicelocend]
        line = line.replace(',', '')
        if currentTeam in line:

            namelisttemp.append(line)
    finalNameList = []

    for name in namelisttemp:
        loc = name.find(':')
        name = name[loc + 2:]
        finalNameList.append(name)

    finalNameList.insert(0,'none')
    ComboboxPlayer.config(value = finalNameList)
    if player == 'none':
        KDLabel.place_forget()
        RankLabel.place_forget()
        StatusLabel.place_forget()
        EarningsLabel.place_forget()
        BirthdayLabel.place_forget()
        NameLabel.place_forget()



def TeamSel(sortedTeams):
    ComboboxPlayer.current(0)
    listofTeams = []
    for i in sortedTeams:
        listofTeams.append(i)
    listofTeams.insert(0,'none')
    ComboboxTeam.config(value = listofTeams)
    ComboboxTeam.current(0)
    ComboboxPlayer.current(0)


def getTeams(e):
    player = ComboboxPlayer.get()
    wiki = ComboboxGame.get()
    apiUrl = "https://api.liquipedia.net/api/v2/player"
    headers = {'authorization':'Apikey 0NTexa4EtfeEFuBq6CGjvs8SaTs4ST18K3VRBCbNWBoBxa3G7Ma5zc5E4C2iuulucvjUVV6bX5H5pe9H3GlcKutmSiiNqJTnu5cmdjpIaLteas8tI2Cz91hKHW0aeOLz'}
    params = {'wiki':wiki,'query':'team,id,name', 'limit':'10000000','order':'team ASC, id ASC, name ASC'}
    response = requests.get(apiUrl,headers=headers,params=params)
    response.json()
    data = response.text
    data = data.replace('"',"")
    data = data.replace("\\","")
    data = data.replace("}","\n")
    data = data.replace("{","")
    data = data.replace("[","")
    data = data.replace("]","")
    data = data.replace("result:","")
    data = data.replace(":",": ")
    data = data.replace(",",", ")
    newf = open("sortedData.txt", "w")
    newf.write(data)

    finalfileIds = open("sortedData.txt", "r")
    idlist = []

    for line in finalfileIds:
        line = line[line.find(":"):]
        sliceloc = line.find('id')
        line = line[:sliceloc]
        line = line.replace(",","")
        idlist.append(line)
    idlist.sort()


    unsortedTeams = []
    for x in idlist:
        x = x.split(':')
        if len(x) > 1:
            x[1] = str.strip(x[1])
            x[0] = str.strip(x[0])
        if len(x) > 1 and x[1] != '':
            unsortedTeams.append(str.strip(x[1]))

    sortedTeams = []
    for i in unsortedTeams:
        if i not in sortedTeams:
            sortedTeams.append((i))
    firstcycle = True
    TeamSel(sortedTeams)
    if player == 'none':
        KDLabel.place_forget()
        RankLabel.place_forget()
        StatusLabel.place_forget()
        EarningsLabel.place_forget()
        BirthdayLabel.place_forget()
        NameLabel.place_forget()
#/////////////////////////// GUI CODE //////////////////////////



window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#373939")
canvas = Canvas(
    window,
    bg = "#373939",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    50, 50, 50+1820, 50+980,
    fill = "#1a2a47",
    outline = "")


canvas.create_rectangle(
    98, 100, 98+910, 100+880,
    fill = "#79bbeb",
    outline = "")


canvas.create_rectangle(
    1107, 421, 1107+710, 421+560,
    fill = "#79bbeb",
    outline = "")

canvas.create_text(
    1447.5, 266.5,
    text = "Statsify",
    fill = "#0f1b1b",
    font = ("None", int(150.0)))

canvas.create_text(
    1438.5, 257.5,
    text = "Statsify",
    fill = "#79bbeb",
    font = ("None", int(150.0)))

canvas.create_text(
    284.5, 159.5,
    text = "Game:",
    fill = "#000000",
    font = ("None", int(64.0)))

canvas.create_text(
    1229.0, 693.5,
    text = "Player-1:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1559.5, 695.0,
    text = "Player-1:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1227.0, 733.5,
    text = "Player-2:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1559.5, 732.0,
    text = "Player-2:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1227.0, 777.0,
    text = "Player-3:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1559.5, 776.0,
    text = "Player-3:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1227.0, 821.0,
    text = "Player-4:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1559.5, 819.5,
    text = "Player-4:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1227.0, 865.0,
    text = "Player-5:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1559.5, 863.0,
    text = "Player-5:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    284.5, 259.5,
    text = "Team:",
    fill = "#000000",
    font = ("None", int(64.0)))

canvas.create_text(
    284.5, 450.5,
    text = "KD:",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    1309.5, 925.0,
    text = "Outcome:",
    fill = "#000000",
    font = ("None", int(48.0)))

canvas.create_text(
    1318.0, 612.0,
    text = "Team (Attk)",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    1469.0, 548.5,
    text = "Game:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1645.5, 616.0,
    text = "Team (Def)",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    584.5, 557.5,
    text = "                  ",
    fill = "#000000",
    font = ("Roboto-Bold", int(64.0)))

canvas.create_text(
    1563.5, 917.5,
    text = "                  ",
    fill = "#000000",
    font = ("None", int(64.0)))

canvas.create_text(
    584.5, 657.5,
    text = "                  ",
    fill = "#000000",
    font = ("Roboto-Bold", int(64.0)))

canvas.create_text(
    584.5, 757.5,
    text = "                  ",
    fill = "#000000",
    font = ("None", int(64.0)))

canvas.create_text(
    584.5, 857.5,
    text = "                  ",
    fill = "#000000",
    font = ("None", int(64.0)))

canvas.create_text(
    284.5, 541.5,
    text = "Rank:",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    284.5, 641.5,
    text = "Status:",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    284.5, 741.5,
    text = "Earnings:",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    284.5, 841.5,
    text = "Birthday:",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    284.5, 941.5,
    text = "Name:",
    fill = "#000000",
    font = ("None", int(36.0)))

canvas.create_text(
    284.5, 359.5,
    text = "Player:",
    fill = "#000000",
    font = ("None", int(64.0)))

canvas.create_text(
    420, 415,
    text = "*KD and ranked stat currently only works "
           "for R6, Val, LOL and Apex",
    fill = "#000000",
    font = ("None", int(15.0)))

canvas.create_text(
    1472.0, 462.5,
    text = "Clutch Simulator",
    fill = "#000000",
    font = ("None", int(60.0)))

canvas.create_text(
    1472.0, 511.5,
    text = "*note only for R6, Valorant and CSGO",
    fill = "#000000",
    font = ("None", int(24.0)))



KDLabel = Label(window)
RankLabel = Label(window)
StatusLabel = Label(window)
EarningsLabel = Label(window)
BirthdayLabel = Label(window)
NameLabel = Label(window)
DropdownGame = ["none","ageofempires","apexlegends","arenafps","arenaofvalor","artifact","autochess","battalion","battlerite","brawlstars", "callofduty","clashroyale","counterstrike","criticalops","crossfire",
                "dota2","fifa","fighters","fornite","freefire","halo","hearthstone","heroes","leagueoflegends","magic","overwatch",
                "palaidns","pokemon","pubg","rainbowsix","valorant"]

#DropdownGameClicked = StringVar()
#DropdownGameClicked.set(DropdownGame[0])

#Dropdowngamemenu = OptionMenu(window, DropdownGameClicked, *DropdownGame, command=getPlayers)
#currGame = DropdownGameClicked
#Dropdowngamemenu.place(x=100,y=100)

ComboboxGame = ttk.Combobox(window, state="readonly", values = DropdownGame, width = 20, font = "Roboto 20")
ComboboxGame.place(x=425, y =150)
ComboboxGame.current(0)
ComboboxGame.bind("<<ComboboxSelected>>",getTeams)

ComboboxTeam = ttk.Combobox(window, state="readonly", values=['none'], width = 20, font = "Roboto 20")
ComboboxTeam.current(0)
ComboboxTeam.place(x=425, y =250)
ComboboxTeam.bind("<<ComboboxSelected>>",getPlayers)


ComboboxPlayer = ttk.Combobox(window, state="readonly", values=['none'], width = 20, font = "Roboto 20")
ComboboxPlayer.current(0)
ComboboxPlayer.place(x=425, y =350)
ComboboxPlayer.bind("<<ComboboxSelected>>",getStats)


window.resizable(True, True)
window.mainloop()

#/////////////////////////// END GUI CODE //////////////////////////


