import time
import keyboard as kb
import pyautogui as pg
save2 = 1
way 13 = 1
item2 = 1
save12 = 1
way12 = 1
way21 = 1
way11 = 1
fight = False
way = 1
item1 = 1
save1 = 1
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
if way == "Прямо" or way == "прямо":
    print ("Ты пошёл вперёд и увидел ящик")
    way21 = input("Откроешь ли ты этот ящик?")
if way21 == "Да" or way21 == "да":
    money = int(money)
    print("В ящике лежало 3000 рублей")
    money = money + 3000
    money = str(money)
    print ("Теперь у вас "+money+" рублей")
    checkpoint = str(21)
    save1 = input("Хотите сохранить игру?")
if checkpoint == '21':
    print ("Вы пошли дальше и увидели магазин")
    time.sleep(3)
    pg.press('win')
    time.sleep(1)
    kb.write('shop2.txt')
    time.sleep(3)
    pg.press('enter')
    item2 = input("Что вы хотите купить?")
if (item2 == "Новый меч" or item2 == "новый меч") and int(money) < 5500:
    print("Вам не хватило денег")
if (item2 == "Новую броню" or item2 == "новую броню") and int(money) < 6000:
    print("Вам не хватило денег")
if (item2 == "Копьё" or item2 == "копьё") and int(money) < 2500:
    print("Вам не хватило денег")
if (item2 == "Новый меч" or item2 == "новый меч") and int(money) >= 5500:
    money = int(money) - 5500
    damage = int(damage) + 10
    checkpoint = str(22)
    print ("Поздравляем с покупкой!")
    save12 = input("Хотите сохранить игру?")
if (item2 == "Новую броню" or item2 == "новую броню") and int(money) >= 6000:
    money = int(money) - 6000
    hp = int(hp) + 100
    checkpoint = str(22)
    print ("Поздравляем с покупкой!")
    save12 = input("Хотите сохранить игру?")
if (item2 == "Копьё" or item2 == "копьё") and int(money) >= 2500:
    money = int(money) - 2500
    damage = int(damage) + 5
    checkpoint = str(22)
    print ("Поздравляем с покупкой!")
    save12 = input("Хотите сохранить игру?")
if save12 == "Да" or save12 == "да":
    money = str(money)
    damage = str(damage)
    hp = str(hp)
    f1 = open("checkpoint.txt", 'w', encoding="utf-8")
    f1.write(checkpoint)
    f1.close()
    f4 = open("money.txt", 'w', encoding="utf-8")
    f4.write(money)
    f4.close()
    f3 = open("damage.txt", 'w',encoding="utf-8")
    f3.write(damage)
    f3.close()
    print ("Игра сохранена")
if int(checkpoint) == 22:
    print ("Вы пошли дальше и увидели много крокодилов")
    way13 = input ("Вы будете атаковать по 1 или сразу всех?")
if way13 == ("По 1" or way13 == "по 1") and (hp >= 170 or damage >= 20):
    print ("Поздравляю! Вы победили всех крокодилов")
    
    
    
if way == "Налево" or way == "налево":
    print("Вы пошли налево и увидели магазин, у вас с собой "+money+" рублей")
    time.sleep(3)
    pg.press('win')
    time.sleep(1)
    kb.write('shop1.txt')
    time.sleep(3)
    pg.press('enter')
    item1 = input("Что вы купите?")
money = int(money)
if (item1 == "Поломанный меч" or item1 == "поломанный меч") and money < 2500:
    print("Вам не хватает денег")
if (item1 == "Старая броня" or item1 == "старая броня") and money < 3000:
    print("Вам не хватает денег")
if (item1 == "Зелье силы" or item1 == "зелье силы") and money < 1000:
    print("Вам не хватает денег")
if (item1 == "Поломанный меч" or item1 == "поломанный меч")and money >= 2500:
    money= int(money) - 2500
    damage= int(damage) + 5
    money = str(money)
    damage = str(damage)
    save1 = input("Спасибо за покупку!Хотите сохранить игру?")
    checkpoint = str(1)
if (item1 == "Старую броню" or item1 == "старую броню") and money >= 3000:
    money = int(money)- 3000
    hp = int(hp)+ 50
    money = str(money)
    hp = str(hp)
    save1 = input("Спасибо за покупку!Хотите сохранить игру?")
    checkpoint = str(1)
if (item1 == "Зелье силы" or item1 == "зелье силы") and money >= 1000:
    money = int(money)- 1000
    damage = int(damage)+ 2
    money = str(money)
    damage = str(damage)
    save1 = input("Спасибо за покупку!Хотите сохранить игру?")
    checkpoint = str(1)
if save1 == "Да" or save1 == "да":
    money = str(money)
    damage = str(damage)
    hp = str(hp)
    f1 = open("checkpoint.txt", 'w', encoding="utf-8")
    f1.write(checkpoint)
    f1.close()
    f4 = open("money.txt", 'w', encoding="utf-8")
    f4.write(money)
    f4.close()
    f3 = open("damage.txt", 'w',encoding="utf-8")
    f3.write(damage)
    f3.close()
    print ("Игра сохранена")
if checkpoint == '1':
    print("Вы пошли дальше и увидели дракона который полетел на вас")
    way12 = input("Вы будете нападать или стараться защищаться?")
if (int(hp) > 100 or int(damage) > 12) and (way12 == "Нападать" or way12 == "нападать"):
    print ("Вы сразились с ним и выиграли в бою!")
    print ("Пошли дальше и увидели зелье которое сильно светилось")
    way11 = input("Вы выпьете это зелье?")
if (int(hp) <= 100 or int(damage) <= 12) and (way == "Налево" or way == "налево"):
    print ("Вы сразились с драконом и програли")
    save2 = input("Хотите начать игру заново?")
if way11 == "Да" or way11 == "да":
    print ("Вы получили бесконечную силу!")
    print ("Игра пройдена")
    damage = int(damage) + 9999999999
    hp = int(hp) + 99999999
    save2 = input("Хотите начать игру заново?")
if way11 == "Нет" or way11 == "нет":
    print("Вы прошли мимо и пришли домой")    
    save2 = input("Хотите начать игру заново")
if save2 == "Да" or save2 == "да":
    checkpoint = str(0)
    money = str(5000)
    damage = str(10)
    hp = str(100)
    f1 = open("checkpoint.txt", 'w', encoding="utf-8")
    f1.write(checkpoint)
    f1.close()
    f4 = open("money.txt", 'w', encoding="utf-8")
    f4.write(money)
    f4.close()
    f3 = open("damage.txt", 'w',encoding="utf-8")
    f3.write(damage)
    f3.close()
if way == "Направо" or way == "направо":
    print ("Вы пришли домой")