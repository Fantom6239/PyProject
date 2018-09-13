list = ["Антон","Андрей","Александр","Борис","Валентин","Валерий","Кирилл","Константин","Анастасия","Людмила","Алёна","Валерия","Виктория","Галина","Евгения","Елена"] #Имена
print (list[:])
while True:
    print("\n" + "Это мужское имя?")
    user = input()
    if user == 'Да' or user == 'да':
        print("В имени 5 букв?")
        user = input()
        if user == 'Да' or user == 'да':
            print("Имя начинается с буквы А?")
            user = input()
            if user == 'Да' or user == 'да':
                print(list[0]) #Антон
            else:
                print(list[3]) #Борис
        else:
            print("Имя имеет женский аналог?")
            user = input()
            if user == 'Да' or user == 'да':
                print("Имя начинается с буквы А?")
                user = input()
                if user == 'Да' or user == 'да':
                    print(list[2]) #Александр
                else:
                    print("Связано ли это имя с Днём влюблённых?")
                    user = input()
                    if user == 'Да' or user == 'да':
                        print(list[4]) #Валентин
                    else:
                        print(list[5]) #Валерий
            else:
                print("Имя начинается с буквы К?")
                user = input()
                if user == 'Да' or user == 'да':
                    print("В имени больше 7 букв?")
                    user = input()
                    if user == 'Да' or user == 'да':
                        print(list[7]) #Константин
                    else:
                        print(list[6]) #Кирилл
                else:
                    print(list[1]) #Андрей
    else:
        print("Имя имеет мужской аналог?")
        user = input()
        if user == 'Да' or user == 'да':
            print("Имя начинается с буквы В?")
            user = input()
            if user == 'Да' or user == 'да':
                print("Имя означает 'Победа'?")
                user = input()
                if user == 'Да' or user == 'да':
                    print(list[12]) #Виктория
                else:
                    print(list[11]) #Валерия
            else:
                print(list[14]) #Евгения
        else:
            print("Имя начинается на гласную букву?")
            user = input()
            if user == 'Да' or user == 'да':
                print("Имя начинается на букву А?")
                user = input()
                if user == 'Да' or user == 'да':
                    print("В имени больше 5 букв?")
                    user = input()
                    if user == 'Да' or user == 'да':
                        print(list[8]) #Анастасия
                    else:
                        print(list[10]) #Алёна
                else:
                    print(list[15]) #Елена
            else:
                print("В имени больше 6 букв?")
                user = input()
                if user == 'Да' or user == 'да':
                    print(list[9]) #Людмила
                else:
                    print(list[13]) #Галина


























        
