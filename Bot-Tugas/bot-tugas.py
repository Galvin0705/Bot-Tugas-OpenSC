from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from art import *
import time

tprint("Bot-Tugas", font='bulbhead')
logo = """[+]======================[+]\nCode ini di open oleh iFanpS\nPada tanggal 15 agustus/2021\n[+]======================[+]\n"""
print(logo)
print("1 . bahan_1.jpg berjumlah : 25 baris\n2 . bahan_2.jpg berjumlah : 25 baris\n")
try:
    lembar_kertas = str(input("Pilih Kertas : "))
    if lembar_kertas == "1":
        img = Image.open('bahan_1.jpg')
        cd = ImageDraw.Draw(img)
        print("1 . font1.ttf Berukuran : 50\n2 . font2.ttf Berukuran : 70\n")
        pilih_font = str(input("Pilih Font : "))
        if pilih_font == "1":
            font = ImageFont.truetype('font1.ttf', size=50)
            with open('Tulisan','r') as f:
                tulis = f.read()
            cd.text((335,530), tulis, font=font, fill =(000, 0, 0))
            img.save('hasil.jpg')
            print("Berhasil menulis!\nBanyak kata : {}".format(len(tulis)))
            time.sleep(3)
        elif pilih_font == "2":
            font = ImageFont.truetype('font2.ttf', size=70)
            with open('Tulisan','r') as f:
                tulis = f.read()
            cd.text((335,510), tulis, font=font, fill =(000, 0, 0))
            img.save('hasil.jpg')
            print("Berhasil menulis!\nBanyak kata : {}".format(len(tulis)))
            time.sleep(3)
    elif lembar_kertas == "2":
        img = Image.open('bahan_2.jpg')
        cd = ImageDraw.Draw(img)
        print("1 . font1.ttf Berukuran : 50\n2 . font2.ttf Berukuran : 70\n")
        pilih_font = str(input("Pilih Font : "))
        if pilih_font == "1":
            font = ImageFont.truetype('font1.ttf', size=50)
            with open('Tulisan','r') as f:
                tulis = f.read()
            cd.text((335,550), tulis, font=font, fill =(000, 0, 0))
            img.save('hasil.jpg')
            print("Berhasil menulis!\nBanyak kata : {}".format(len(tulis)))
            time.sleep(3)
        elif pilih_font == "2":
            font = ImageFont.truetype('font2.ttf', size=70)
            with open('Tulisan','r') as f:
                tulis = f.read()
            cd.text((335,520), tulis, font=font, fill =(000, 0, 0))
            img.save('hasil.jpg')
            print("Berhasil menulis!\nBanyak kata : {}".format(len(tulis)))
            time.sleep(3)
except FileNotFoundError:
    print("[ERROR] Bahan tidak di temukan!")
