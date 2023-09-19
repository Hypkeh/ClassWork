from random import randint

#  M = Menu
firstM = [{"Куриный суп": 1200},
          {"Борщ": 1100},
          {"Лагман": 1100},
          {"Окрошка": 1300}]

secondM = [{"Плов": 2100},
           {"Жареная рыба":2500},
           {"Стейк":3700},
           {"Бифштекс":2250}]

drinkM = [{"Чай зеленый": 200},
          {"Чай черный": 250},
          {"Эспрессо": 500},
          {"Латте": 520}]

desertM = [{"Мороженное": 1000},
           {"Коктейль": 1500},
           {"Чизкейк": 800}]

menu = {'first': firstM,
        "second": secondM,
        'desert': desertM,
        'drink': drinkM}

freeTables = []
for i in range(randint(1,10)):
    freeTables.append(randint(1, 15))


def restaurant():
    print("Hello")
    print("Сейчас свободны столы:", freeTables)
    table = input("Какой стол желаете? ")
    print('1) Первые блюда')
    print('2) Вторые блюда')
    print('3) Горячие напитки')
    print('4) Десерт')
    choice = int(input("Выберите: "))
    bill = []
    ordering = True
    while ordering:
        if choice == 1:
            for item in firstM:
                for j in item:
                    print(f"{j} - {item[j]} тенге")
            order = input("Что хотите заказать? ")
            if order == j:
                bill.append(item[j])
        if choice == 2:
            for item in secondM:
                for j in item:
                    print(f"{j} - {item[j]} тенге")
            order = input("Что хотите заказать? ")
            if order == j:
                bill.append(item[j])
        if choice == 3:
            for item in drinkM:
                for j in item:
                    print(f"{j} - {item[j]} тенге")
            order = input("Что хотите заказать? ")
            if order == j:
                bill.append(item[j])
        if choice == 4:
            for item in desertM:
                for j in item:
                    print(f"{j} - {item[j]} тенге")
            order = input("Что хотите заказать? ")
            if order == j:
                bill.append(item[j])
    
        more = input('Желаете заказать что-нибудь еще?')
        if more == 'Нет':
            ordering = False
            for price in bill:
                print('Общая сумма -', price)
            
    print(f"Итого {sum(bill)} тенге")
    
restaurant() 



