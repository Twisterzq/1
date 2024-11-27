import time
import keyboard as kb
import pyautogui as pg
f1 = open("checkpoint.txt", 'r', encoding="utf-8")
checkpoint = f1.read()
f1.close()
f2 = open("hp.txt", 'r', encoding="utf-8")
hp = f2.read()
f2.close()
f3 = open("damage.txt", 'r',encoding="utf-8")
damage = f3.read()
f3.close()
f4 = open("money.txt", 'r', encoding="utf-8")
money = f4.read()
f4.close
if checkpoint == '0':
    print("Ты шёл домой и увидел на камне:")
    print("Налево пойдешь - сильным станешь")
    print("Прямо пойдёшь - богатым будешь")
    print("Направо пойдёшь - домой придёшь")
    way = input("Куда пойдёшь?Налево, вперёд или направо?")
if way == "Налево" or "налево":
    print("Вы пошли налево и увидели магазин, у вас с собой "+money+" рублей")
    time.sleep(5)
    pg.press('win')
    kb.write('shop1.txt')
    time.sleep(3)
    pg.press('enter')
    item1 = input("Что вы купите?")
if item1 == "Поломанный меч" or "поломанный меч"and money >= 2500:
    money= int(money) - 2500
    damage= int(damage) + 5
    money = str(money)
    damage = str(damage)
    save1 = input("Спасибо за покупку!Хотите сохранить игру?")
if item1 == "Старая броня" or "старая броня" and money >= 3000:
    money = int(money)- 3000
    hp = int(hp)+ 50
    money = str(money)
    hp = str(hp)
    save1 = input("Спасибо за покупку!Хотите сохранить игру?")
if item1 == "Зелье силы" or "зелье силы" and money >= 1000:
    money = int(money)- 1000
    damage = int(damage)+ 50
    money = str(money)
    damage = str(damage)
    save1 = input("Спасибо за покупку!Хотите сохранить игру?")
if (item1 == "Поломанный меч" or "поломанный меч") and money < 2500:
    print("Вам не хватает денег")
if (item1 == "Старая броня" or item1 == "старая броня") and money < 3000:
    print("Вам не хватает денег")
if save1 == "Да" or save1 == "да":
    checkpoint = str(1)
    f1 = open("checkpoint.txt", 'w', encoding="utf-8")
    f1.write(checkpoint)
    f1.close()
    f4 = open("money.txt", 'w', encoding="utf-8")
    f4.write(money)
    f4.close()
    f3 = open("damage.txt", 'w',encoding="utf-8")
    f3.write(damage)
    f3.close()
if way == "Направо" or "направо":
    print ("Вы пришли домой")