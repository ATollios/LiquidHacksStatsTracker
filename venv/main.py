import requests
import json
import os
from tkinter import *
from tkinter import ttk
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen
import urllib.request
import random
from PIL import Image, ImageTk
firstcycle = False
currGame = ''


def webScrabingTime():
    game = ComboboxGame.get()
    player = ComboboxPlayer.get()
    player = player.replace(" ", '')
    print(player)
    if game == 'rainbowsix' or game == 'leagueoflegends':

        if game == 'rainbowsix':
            try:
                urlR = 'https://r6.tracker.network/profile/pc/'+player
                requestR = urllib.request.Request(urlR, headers={'User-Agent': 'Magic Browser'})
                pageSiege = urllib.request.urlopen(requestR)
                HtmlR = pageSiege.read()
                HtmlR = HtmlR.decode("utf-8")
            except:
                RankLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
                RankLabel.place(x=355, y=390)
                KDLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
                KDLabel.place(x=355, y=390)
        try:
            locKR = HtmlR.find('<div class="trn-defstat__value" data-stat="PVPKDRatio">')
            KDR = HtmlR[locKR + len('<div class="trn-defstat__value" data-stat="PVPKDRatio">'):]
            locKRS = KDR.find('<')
            KDR = KDR[:locKRS]
            try:
                KDRInt = float(KDR)
                KDLabel.config(text=KDR, font="Roboto 22", bg='#79bbeb')
                KDLabel.place(x=335, y=390)
            except:
                KDLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
                KDLabel.place(x=335, y=390)
        except:
            KDLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
            KDLabel.place(x=335, y=390)

        try:
            locR = HtmlR.find('alt="')
            RankR = HtmlR[locR+len('alt="'):]
            locRS = RankR.find('"')
            RankR = RankR[:locRS]

            RankR = RankR.lower()
            RankR = RankR.capitalize()
            print(RankR)
            RankLabel.config(text=RankR, font="Roboto 22", bg='#79bbeb')
            RankLabel.place(x=340, y=470)
        except:
            RankLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
            RankLabel.place(x=340, y=470)

        if game == 'leagueoflegends':
            try:
                urlL = 'https://tracker.gg/lol/profile/riot/NA/'+player+'/overview'
                requestL = urllib.request.Request(urlL, headers = {'User-Agent': 'Magic Browser'})
                pageLeague = urllib.request.urlopen(requestL)
                HtmlL = pageLeague.read()
                HtmlL = HtmlL.decode("utf-8")
                locL = HtmlL.find('KDA</span> <!----> <span class="value" data-v-309b1f1e>')
                KDL = HtmlL[locL+len('KDA</span> <!----> <span class="value" data-v-309b1f1e>'):]
                KDL = KDL[0:4]
                print(KDL)
                try:
                    varKDL = float(KDL)
                    KDLabel.config(text=KDL, font="Roboto 22", bg='#79bbeb')
                    KDLabel.place(x=335, y=390)
                except:
                    KDLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
                    KDLabel.place(x=335, y=390)
            except Exception as e:
                RankLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
                RankLabel.place(x=340, y=470)
        else:
            RankLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
            RankLabel.place(x=340, y=470)
            KDLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
            KDLabel.place(x=335, y=390)
def getStats(e):
    player = ComboboxPlayer.get()
    wiki = ComboboxGame.get()
    apiUrl = "https://api.liquipedia.net/api/v2/player"
    headers = {
        'authorization': 'Apikey 0NTexa4EtfeEFuBq6CGjvs8SaTs4ST18K3VRBCbNWBoBxa3G7Ma5zc5E4C2iuulucvjUVV6bX5H5pe9H3GlcKutmSiiNqJTnu5cmdjpIaLteas8tI2Cz91hKHW0aeOLz'}
    params = {'wiki': wiki, 'conditions': '[[pagename::'+player+']]','query': 'name, earnings, birthdate,status, extradata',  'limit': '10000000',}
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
    CharHolder = data
    RoleHolder = data
    ###Status Stuff#
    StatusBeg = StatusHolder.find('status:')
    StatusEnd = StatusHolder.find(', extra')
    StatusHolder= StatusHolder[StatusBeg + 8 :StatusEnd]
    if StatusHolder != '' and StatusHolder != ' ' and StatusHolder != None and 'u0' not in StatusHolder:
        StatusLabel.config(text=StatusHolder, font = "Roboto 22", bg= '#79bbeb')
        StatusLabel.place(x=355, y=545)
    else:
        StatusLabel.config(text='Data Not Found', font = "Roboto 22", bg= '#79bbeb')
        StatusLabel.place(x=355, y=545)

    ###Earnings Stuff#
    EarninsBeg = EarningsHolder.find('earnings:')
    EarningsEnd = EarningsHolder.find(', birthdate')
    EarningsHolder = EarningsHolder[EarninsBeg + 10:EarningsEnd]
    if EarningsHolder != '' and EarningsHolder != ' ' and EarningsHolder != None and 'u0' not in EarningsHolder:
        EarningsLabel.config(text='$' + EarningsHolder, font = "Roboto 22", bg= '#79bbeb')
        EarningsLabel.place(x=370, y=619)
    else:
        EarningsLabel.config(text='Data Not Found', font = "Roboto 22", bg= '#79bbeb')
        EarningsLabel.place(x=370, y = 619)



    ###Birthday Stuff#
    BirthdayBeg = BirthdayHolder.find('birthdate:')
    BirthdayEnd = BirthdayHolder.find(', status')
    BirthdayHolder= BirthdayHolder[BirthdayBeg + 11 :BirthdayEnd]

    if BirthdayHolder != '' and BirthdayHolder != ' ' and BirthdayHolder != None and 'u0' not in BirthdayHolder and BirthdayHolder != '1970-01-01':
        BirthdayLabel.config(text=BirthdayHolder, font = "Roboto 22", bg= '#79bbeb')
        BirthdayLabel.place(x=365, y=687)
    else:
        BirthdayLabel.config(text='Data Not Found', font = "Roboto 22", bg= '#79bbeb')
        BirthdayLabel.place(x=365, y=687)


    ###Name Stuff#
    nameBeg = NameHolder.find('name:')
    nameEnd = NameHolder.find(', earnings')
    NameHolder= NameHolder[nameBeg + 6 :nameEnd]
    if NameHolder != '' and NameHolder != ' ' and NameHolder != None and 'u0' not in NameHolder:
        NameLabel.config(text=NameHolder, font = "Roboto 22", bg= '#79bbeb')
        NameLabel.place(x=345, y=757)
    else:
        NameLabel.config(text='Data Not Found',font = "Roboto 22", bg= '#79bbeb')
        NameLabel.place(x=345, y=757)

##Char Stuff#
    try:
        CharBeg = CharHolder.find('signature')
        print(CharBeg)
        CharHolder = CharHolder[CharBeg:]
        CharStart = CharHolder.find(":")
        CharEnd = CharHolder.find(",")
        print(CharHolder)
        CharHolder = CharHolder[CharStart+2:CharEnd]

        if CharHolder != '' and CharHolder != ' ' and CharHolder != None and 'u0' not in CharHolder:
            CharHolder = CharHolder.capitalize()
            CharLabel.config(text=CharHolder, font="Roboto 22", bg='#79bbeb')
            CharLabel.place(x=365, y=832)

        else:
            CharLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
            CharLabel.place(x=365, y=832)
    except Exception:
        CharLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
        CharLabel.place(x=365, y=832)
    ##Role Stuff#
    try:
        RoleBeg = RoleHolder.find('role:')
        RoleHolder = RoleHolder[RoleBeg + len('role:'):]
        RoleEnd = RoleHolder.find(",")
        print(RoleHolder)
        RoleHolder = RoleHolder[:RoleEnd]

        if RoleHolder != '' and RoleHolder != ' ' and RoleHolder != None and 'u0' not in RoleHolder:
            RoleHolder = RoleHolder.capitalize()
            RoleLabel.config(text=RoleHolder, font="Roboto 22", bg='#79bbeb')
            RoleLabel.place(x=325, y=902)

        else:
            RoleLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
            RoleLabel.place(x=325, y=902)
    except Exception:
         RoleLabel.config(text='Data Not Found', font="Roboto 22", bg='#79bbeb')
         RoleLabel.place(x=325, y=902)

    if player == 'none':
        KDLabel.place_forget()
        RankLabel.place_forget()
        StatusLabel.place_forget()
        EarningsLabel.place_forget()
        BirthdayLabel.place_forget()
        NameLabel.place_forget()
        CharLabel.place_forget()
        RoleLabel.place_forget()

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
        CharLabel.place_forget()
        RoleLabel.place_forget()


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
        CharLabel.place_forget()
        RoleLabel.place_forget()
#/////////////////////////// GUI CODE //////////////////////////



window = Tk()
window.title('Statsify')
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
    82, 61, 82+910, 61+880,
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
    277.5, 142.5,
    text = "Game:",
    fill = "#000000",
    font = ("None", int(48.0)))

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
    277.5, 242.5,
    text = "Team:",
    fill = "#000000",
    font = ("None", int(48.0)))

canvas.create_text(
    282.5, 410.5,
    text = "KD:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    1309.5, 925.0,
    text = "Outcome:",
    fill = "#000000",
    font = ("None", int(48.0)))

canvas.create_text(
    1318.0, 612.0,
    text = "Team (Attk):",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    1469.0, 548.5,
    text = "Game:",
    fill = "#000000",
    font = ("None", int(30.0)))

canvas.create_text(
    1645.5, 616.0,
    text = "Team (Def):",
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
    282.5, 486.5,
    text = "Rank:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    282.5, 561.5,
    text = "Status:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    282.5, 636.5,
    text = "Earnings:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    282.5, 703.5,
    text = "Birthday:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    282.5, 774.5,
    text = "Name:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    282.5, 850.5,
    text = "Character:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    282.5, 920.5,
    text = "Role:",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    277.5, 342.5,
    text = "Player:",
    fill = "#000000",
    font = ("None", int(48.0)))

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
CharLabel = Label(window)
RoleLabel = Label(window)
DropdownGame = ["none","ageofempires","apexlegends","arenafps","arenaofvalor","artifact","battalion","battlerite","brawlstars", "callofduty","clashroyale","counterstrike","criticalops","crossfire",
                "dota2","fifa","fighters","fornite","freefire","halo","hearthstone","heroes","leagueoflegends","magic","overwatch",
                "palaidns","pokemon","pubg","rainbowsix","valorant"]

#DropdownGameClicked = StringVar()
#DropdownGameClicked.set(DropdownGame[0])

#Dropdowngamemenu = OptionMenu(window, DropdownGameClicked, *DropdownGame, command=getPlayers)
#currGame = DropdownGameClicked
#Dropdowngamemenu.place(x=100,y=100)

ComboboxGame = ttk.Combobox(window, state="readonly", values = DropdownGame, width = 20, font = "Roboto 20")
ComboboxGame.place(x=400, y =125)
ComboboxGame.current(0)
ComboboxGame.bind("<<ComboboxSelected>>",getTeams)

ComboboxTeam = ttk.Combobox(window, state="readonly", values=['none'], width = 20, font = "Roboto 20")
ComboboxTeam.current(0)
ComboboxTeam.place(x=400, y =225)
ComboboxTeam.bind("<<ComboboxSelected>>",getPlayers)


ComboboxPlayer = ttk.Combobox(window, state="readonly", values=['none'], width = 20, font = "Roboto 20")
ComboboxPlayer.current(0)
ComboboxPlayer.place(x=400, y =325)
ComboboxPlayer.bind("<<ComboboxSelected>>",getStats)




#/////////////////////////// END GUI CODE //////////////////////////



#///////////////////////////CLUTCH SIM STUFF, WELL MOST OF IT //////////////////////////

Games = ["none","counterstrike","rainbowsix","valorant"]

def CustMmr():

    counterA = 5
    counterB = 5
    PlayerA1Stats = getStats(ComboboxPlayer1A)
    PlayerA2Stats = getStats(ComboboxPlayer2A)
    PlayerA3Stats = getStats(ComboboxPlayer3A)
    PlayerA4Stats = getStats(ComboboxPlayer4A)
    PlayerA5Stats = getStats(ComboboxPlayer5A)


    PlayerD1Stats = getStats(ComboboxPlayer1D)
    PlayerD2Stats = getStats(ComboboxPlayer2D)
    PlayerD3Stats = getStats(ComboboxPlayer3D)
    PlayerD4Stats = getStats(ComboboxPlayer4D)
    PlayerD5Stats = getStats(ComboboxPlayer5D)

    if ComboboxPlayer1A.get() == 'none':
       counterA -=1
    if ComboboxPlayer2A.get() == 'none':
       counterA -=1
    if ComboboxPlayer3A.get() == 'none':
       counterA -=1
    if ComboboxPlayer4A.get() == 'none':
       counterA -=1
    if ComboboxPlayer5A.get() == 'none':
       counterA -=1
    if ComboboxPlayer1D.get() == 'none':
       counterB-=1
    if ComboboxPlayer2D.get() == 'none':
       counterB -=1
    if ComboboxPlayer3D.get() == 'none':
       counterB -=1
    if ComboboxPlayer4D.get() == 'none':
       counterB -=1
    if ComboboxPlayer5D.get() == 'none':
       counterB -=1

    if len(str(PlayerA1Stats)) == 1 or PlayerA1Stats == 'none':
        PlayerA1Stats = 1
    elif len(str(PlayerA1Stats))  == 2 and PlayerA1Stats != 'none':
        PlayerA1Stats = 2
    elif len(str(PlayerA1Stats))  == 3 and PlayerA1Stats != 'none':
        PlayerA1Stats = 3
    elif len(str(PlayerA1Stats))  == 4 and PlayerA1Stats != 'none':
        PlayerA1Stats = 4
    elif len(str(PlayerA1Stats))  == 5 and PlayerA1Stats != 'none':
        PlayerA1Stats = 5
    elif len(str(PlayerA1Stats))  == 6 and PlayerA1Stats != 'none':
        PlayerA1Stats = 6
    else:
        PlayerA1Stats = 1

    if len(str(PlayerA2Stats)) == 1 or PlayerA2Stats != 'none':
        PlayerA2Stats = 1
    elif len(str(PlayerA2Stats))  == 2 and PlayerA2Stats != 'none':
        PlayerA2Stats = 2
    elif len(str(PlayerA2Stats))  == 3 and PlayerA2Stats != 'none':
        PlayerA2Stats = 3
    elif len(str(PlayerA2Stats))  == 4 and PlayerA2Stats != 'none':
        PlayerA2Stats = 4
    elif len(str(PlayerA2Stats))  == 5  and PlayerA2Stats != 'none':
        PlayerA2Stats = 5
    elif len(str(PlayerA2Stats))  == 6 and PlayerA2Stats != 'none':
        PlayerA2Stats = 6
    else:
        PlayerA2Stats = 1



    if len(str(PlayerA3Stats)) == 1 or PlayerA3Stats == 'none':
        PlayerA3Stats = 1
    elif len(str(PlayerA3Stats))  == 2 and PlayerA3Stats != 'none':
        PlayerA3Stats = 2
    elif len(str(PlayerA3Stats))  == 3 and PlayerA3Stats != 'none':
        PlayerA3Stats = 3
    elif len(str(PlayerA3Stats))  == 4 and PlayerA3Stats != 'none':
        PlayerA3Stats = 4
    elif len(str(PlayerA3Stats))  == 5 and PlayerA3Stats != 'none':
        PlayerA3Stats = 5
    elif len(str(PlayerA3Stats))  == 6 and PlayerA3Stats != 'none':
        PlayerA3Stats = 6
    else:
        PlayerA3Stats = 1

    if len(str(PlayerA4Stats)) == 1 or PlayerA4Stats == 'none':
        PlayerA4Stats = 1
    elif len(str(PlayerA4Stats))  == 2 and PlayerA4Stats != 'none':
        PlayerA4Stats = 2
    elif len(str(PlayerA4Stats))  == 3 and PlayerA4Stats != 'none':
        PlayerA4Stats = 3
    elif len(str(PlayerA4Stats))  == 4 and PlayerA4Stats != 'none':
        PlayerA4Stats = 4
    elif len(str(PlayerA4Stats))  == 5 and PlayerA4Stats != 'none':
        PlayerA4Stats = 5
    elif len(str(PlayerA4Stats))  == 6 and PlayerA4Stats != 'none':
        PlayerA4Stats = 6
    else:
        PlayerA4Stats = 1


    if len(str(PlayerA5Stats)) == 1 or PlayerA5Stats == 'none':
        PlayerA5Stats = 1
    elif len(str(PlayerA5Stats))  == 2 and PlayerA5Stats != 'none':
        PlayerA5Stats = 2
    elif len(str(PlayerA5Stats))  == 3 and PlayerA5Stats != 'none':
        PlayerA5Stats = 3
    elif len(str(PlayerA5Stats))  == 4 and PlayerA5Stats != 'none':
        PlayerA5Stats = 4
    elif len(str(PlayerA5Stats))  == 5 and PlayerA5Stats != 'none':
        PlayerA5Stats = 5
    elif len(str(PlayerA5Stats))  == 6 and PlayerA5Stats != 'none':
        PlayerA5Stats = 6
    else:
        PlayerA5Stats = 1


    if len(str(PlayerD1Stats)) == 1 or PlayerD1Stats == 'none':
        PlayerD1Stats = 1
    elif len(str(PlayerD1Stats)) == 2 and PlayerD1Stats != 'none':
        PlayerD1Stats = 2
    elif len(str(PlayerD1Stats)) == 3 and PlayerD1Stats != 'none':
        PlayerD1Stats = 3
    elif len(str(PlayerD1Stats)) == 4 and PlayerD1Stats != 'none':
        PlayerD1Stats = 4
    elif len(str(PlayerD1Stats)) == 5 and PlayerD1Stats != 'none':
        PlayerD1Stats = 5
    elif len(str(PlayerD1Stats))  == 6 and PlayerD1Stats != 'none':
        PlayerD1Stats = 6
    else:
        PlayerD1Stats = 1


    if len(str(PlayerD2Stats)) == 1 or PlayerD2Stats == 'none':
        PlayerD2Stats = 1
    elif len(str(PlayerD2Stats)) == 2 and PlayerD2Stats != 'none':
        PlayerD2Stats = 2
    elif len(str(PlayerD2Stats)) == 3 and PlayerD2Stats != 'none':
        PlayerD2Stats = 3
    elif len(str(PlayerD2Stats)) == 4 and PlayerD2Stats != 'none':
        PlayerD2Stats = 4
    elif len(str(PlayerD2Stats)) == 5 and PlayerD2Stats != 'none':
        PlayerD2Stats = 5

    elif len(str(PlayerD2Stats))  == 6 and PlayerD2Stats != 'none':
        PlayerD2Stats = 6
    else:
        PlayerD2Stats = 1



    if len(str(PlayerD3Stats)) == 1 or PlayerD3Stats == 'none':
        PlayerD3Stats = 1
    elif len(str(PlayerD3Stats)) == 2 and PlayerD3Stats != 'none':
        PlayerD3Stats = 2
    elif len(str(PlayerD3Stats)) == 3 and PlayerD3Stats != 'none':
        PlayerD3Stats = 3
    elif len(str(PlayerD3Stats)) == 4 and PlayerD3Stats != 'none':
        PlayerD3Stats = 4
    elif len(str(PlayerD3Stats)) == 5 and PlayerD3Stats != 'none':
        PlayerD3Stats = 5


    elif len(str(PlayerD3Stats))  == 6 and PlayerD3Stats != 'none':
        PlayerD3Stats = 6
    else:
        PlayerD3Stats = 1



    if len(str(PlayerD4Stats)) == 1 or PlayerD4Stats == 'none':
        PlayerD4Stats = 1
    elif len(str(PlayerD4Stats)) == 2 and PlayerD4Stats != 'none':
        PlayerD4Stats = 2
    elif len(str(PlayerD4Stats)) == 3 and PlayerD4Stats != 'none':
        PlayerD4Stats = 3
    elif len(str(PlayerD4Stats)) == 4 and PlayerD4Stats != 'none':
        PlayerD4Stats = 4
    elif len(str(PlayerD4Stats)) == 5 and PlayerD4Stats != 'none':
        PlayerD4Stats = 5
    elif len(str(PlayerD4Stats))  == 6 and PlayerD4Stats != 'none':
        PlayerD4Stats = 6
    else:
        PlayerD4Stats = 1




    if len(str(PlayerD5Stats)) == 1 or PlayerD3Stats == 'none':
        PlayerD5Stats = 1
    elif len(str(PlayerD5Stats)) == 2 and PlayerD5Stats != 'none':
        PlayerD5Stats = 2
    elif len(str(PlayerD5Stats)) == 3 and PlayerD5Stats != 'none' :
        PlayerD5Stats = 3
    elif len(str(PlayerD5Stats)) == 4 and PlayerD5Stats != 'none':
        PlayerD5Stats = 4
    elif len(str(PlayerD5Stats)) == 5 and PlayerD5Stats != 'none':
        PlayerD5Stats = 5

    elif len(str(PlayerD5Stats))  == 6 and PlayerD5Stats != 'none':
        PlayerD5Stats = 6
    else:
        PlayerD5Stats = 1



    if counterA < 1:
        counterA = 1
    if counterB < 1:
        counterB = 1
    AvgofA = (float(PlayerA1Stats)+float(PlayerA2Stats)+float(PlayerA3Stats)+float(PlayerA4Stats)+float(PlayerA5Stats))/float(counterA)
    AvgofD = (float(PlayerD1Stats) + float(PlayerD2Stats) + float(PlayerD3Stats) + float(PlayerD4Stats) + float(PlayerD5Stats))/float(counterB)
    AHasAdav = False
    Playerdiff = counterA-counterB

    if Playerdiff <= 0:
        Playerdiff = abs(Playerdiff)
        AHasAdav = False
    else:
        AHasAdvan = True



    if AHasAdav == True:
        AWeight = Playerdiff*AvgofA-1
        DWeight = Playerdiff+AvgofD

        WeightDiff = abs(float(AWeight/DWeight))
        print('WeightDiffAAdv' + str(WeightDiff))
        Rand = random.uniform(0, 1)
        if Rand > WeightDiff:
            WinnerLabel.config(text="Attackers Clutch It!")
        else:
            WinnerLabel.config(text="Defense Win!")

    if AHasAdav == False:


        AWeight = Playerdiff*AvgofA-2
        DWeight = Playerdiff+AvgofD+2

        WeightDiff = abs(float(AWeight/DWeight))
        print('WeightDiffDAdv'+str(WeightDiff))
        print(Playerdiff)
        print(AvgofD)
        print(AvgofA)
        print(AWeight, DWeight)
        print(counterB,counterA)
        Rand = random.uniform(0, 1)

        if Rand < WeightDiff:
            WinnerLabel.config(text="Defense Clutch It!")
        else:
            WinnerLabel.config(text="Attacker Win!")

def getStats(currPlayer):
    currPlayer = currPlayer.get()
    if currPlayer == 'none':
        return ('none')
    wiki = ComboboxPlayerClutchGame.get()
    apiUrl = "https://api.liquipedia.net/api/v2/player"
    headers = {
        'authorization': 'Apikey 0NTexa4EtfeEFuBq6CGjvs8SaTs4ST18K3VRBCbNWBoBxa3G7Ma5zc5E4C2iuulucvjUVV6bX5H5pe9H3GlcKutmSiiNqJTnu5cmdjpIaLteas8tI2Cz91hKHW0aeOLz'}
    params = {'wiki': wiki, 'conditions': '[[pagename::'+currPlayer+']]','query': 'name, earnings, birthdate,status, extradata',  'limit': '10000000',}
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
    EarningsHolder = data
    EarninsBeg = EarningsHolder.find('earnings:')
    EarningsEnd = EarningsHolder.find(', birthdate')
    EarningsHolder = EarningsHolder[EarninsBeg + 10:EarningsEnd]
    try:
        temptest = float(EarningsHolder)
        return(EarningsHolder)
    except:
        return('none')

def getPlayersClutchD(e):
    wiki = ComboboxPlayerClutchGame.get()
    currentTeam = ComboboxPlayerClutchD.get()
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
    ComboboxPlayer1D.config(value = finalNameList)
    ComboboxPlayer2D.config(value=finalNameList)
    ComboboxPlayer3D.config(value=finalNameList)
    ComboboxPlayer4D.config(value=finalNameList)
    ComboboxPlayer5D.config(value=finalNameList)


def Reset():
    ComboboxPlayer1A.current(0)
    ComboboxPlayer2A.current(0)
    ComboboxPlayer3A.current(0)
    ComboboxPlayer4A.current(0)
    ComboboxPlayer5A.current(0)
    ComboboxPlayer1D.current(0)
    ComboboxPlayer2D.current(0)
    ComboboxPlayer3D.current(0)
    ComboboxPlayer4D.current(0)
    ComboboxPlayer5D.current(0)
    ComboboxPlayerClutchA.current(0)
    ComboboxPlayerClutchD.current(0)
    ComboboxPlayerClutchGame.current(0)
    WinnerLabel.config(text = '')
def getPlayersClutchA(e):
    wiki = ComboboxPlayerClutchGame.get()
    currentTeam = ComboboxPlayerClutchA.get()
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
    ComboboxPlayer1A.config(value = finalNameList)
    ComboboxPlayer2A.config(value=finalNameList)
    ComboboxPlayer3A.config(value=finalNameList)
    ComboboxPlayer4A.config(value=finalNameList)
    ComboboxPlayer5A.config(value=finalNameList)


    ComboboxPlayer1A.current(0)
    ComboboxPlayer2A.current(0)
    ComboboxPlayer3A.current(0)
    ComboboxPlayer4A.current(0)
    ComboboxPlayer5A.current(0)
    ComboboxPlayer1D.current(0)
    ComboboxPlayer2D.current(0)
    ComboboxPlayer3D.current(0)
    ComboboxPlayer4D.current(0)
    ComboboxPlayer5D.current(0)

def TeamSelClutch(sortedTeams):
    listofTeams = []
    for i in sortedTeams:
        listofTeams.append(i)
    listofTeams.insert(0,'none')
    ComboboxPlayerClutchA.config(value = listofTeams)
    ComboboxPlayerClutchA.current(0)
    ComboboxPlayer1A.current(0)
    ComboboxPlayer2A.current(0)
    ComboboxPlayer3A.current(0)
    ComboboxPlayer4A.current(0)
    ComboboxPlayer5A.current(0)

    ComboboxPlayerClutchD.config(value = listofTeams)
    ComboboxPlayerClutchD.current(0)
    ComboboxPlayer1D.current(0)
    ComboboxPlayer2D.current(0)
    ComboboxPlayer3D.current(0)
    ComboboxPlayer4D.current(0)
    ComboboxPlayer5D.current(0)



def getTeamsClutch(e):
    wiki = ComboboxPlayerClutchGame.get()
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
    newf = open("sortedDataA.txt", "w")
    newf.write(data)

    finalfileIds = open("sortedDataA.txt", "r")
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

    TeamSelClutch(sortedTeams)



ComboboxPlayer1A = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer1A.place(x=1310, y =683)
ComboboxPlayer1A.current(0)
ComboboxPlayer1A.bind("<<ComboboxSelected>>")

ComboboxPlayer2A = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer2A.place(x=1310, y =723)
ComboboxPlayer2A.current(0)
ComboboxPlayer2A.bind("<<ComboboxSelected>>")

ComboboxPlayer3A = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer3A.place(x=1310, y =766)
ComboboxPlayer3A.current(0)
ComboboxPlayer3A.bind("<<ComboboxSelected>>")

ComboboxPlayer4A = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer4A.place(x=1310, y =809)
ComboboxPlayer4A.current(0)
ComboboxPlayer4A.bind("<<ComboboxSelected>>")

ComboboxPlayer5A = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer5A.place(x=1310, y =853)
ComboboxPlayer5A.current(0)
ComboboxPlayer5A.bind("<<ComboboxSelected>>")

ComboboxPlayer1D = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer1D.place(x=1655, y =683)
ComboboxPlayer1D.current(0)
ComboboxPlayer1D.bind("<<ComboboxSelected>>")


ComboboxPlayer2D = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer2D.place(x=1655, y =723)
ComboboxPlayer2D.current(0)
ComboboxPlayer2D.bind("<<ComboboxSelected>>")

ComboboxPlayer3D = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer3D.place(x=1655, y =766)
ComboboxPlayer3D.current(0)
ComboboxPlayer3D.bind("<<ComboboxSelected>>")

ComboboxPlayer4D = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer4D.place(x=1655, y =809)
ComboboxPlayer4D.current(0)
ComboboxPlayer4D.bind("<<ComboboxSelected>>")

ComboboxPlayer5D = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayer5D.place(x=1655, y =853)
ComboboxPlayer5D.current(0)
ComboboxPlayer5D.bind("<<ComboboxSelected>>")


ComboboxPlayerClutchA = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayerClutchA.place(x=1250, y =635)
ComboboxPlayerClutchA.current(0)
ComboboxPlayerClutchA.bind("<<ComboboxSelected>>", getPlayersClutchA)

ComboboxPlayerClutchD = ttk.Combobox(window, state="readonly", values = ['none'], width = 10, font = "Roboto 15")
ComboboxPlayerClutchD.place(x=1575, y =635)
ComboboxPlayerClutchD.current(0)
ComboboxPlayerClutchD.bind("<<ComboboxSelected>>",getPlayersClutchD)


ComboboxPlayerClutchGame = ttk.Combobox(window, state="readonly", values = Games, width = 12, font = "Roboto 15")
ComboboxPlayerClutchGame.place(x=1400, y =565)
ComboboxPlayerClutchGame.current(0)
ComboboxPlayerClutchGame.bind("<<ComboboxSelected>>", getTeamsClutch)


WinnerLabel = Label(window, text = '', font = "Roboto 30", bg = "#79bbeb")
WinnerLabel.place(x=1450, y =905)

GoButton = Button(window, text = 'Run Match', command = CustMmr)
GoButton.place(x=1443, y=600)


GoButton = Button(window, text = 'Reset', command = Reset)
GoButton.place(x=1458, y=627)


window.resizable(True, True)
window.mainloop()