from tkinter import *


def btn_clicked():
    print("Button Clicked")


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
    1472.0, 462.5,
    text = "Clutch Simulator",
    fill = "#000000",
    font = ("None", int(60.0)))

canvas.create_text(
    1472.0, 511.5,
    text = "*note only for R6, Valorant and CSGO",
    fill = "#000000",
    font = ("None", int(24.0)))

window.resizable(False, False)
window.mainloop()
