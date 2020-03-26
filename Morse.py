# -*- coding: utf-8 -*-

try:

    konvert = input("Ввести текст в строку (y/д) или использовать текстовый документ (n/н)?: ")
    konvert = konvert.lower() # Перевод полученых значений в нижний регистр для приёма введеных больших букв
    if konvert == "n" or konvert == "н":

        # Уточение типа файла для работи с ним
        def construct(form):
            form = form.lower()
            if form == "y" or form == "д":
                old = open(u'Normal text.txt',"r")
                new_file = open(u'New text.txt' , 'w')

            elif form == "n" or form == "н":
                old = open(u'Normal text',"r")
                new_file = open(u'New text' , 'w')

            else:
                print("")
                print("НЕ КОРРЕКТНАЯ КОМАНДА")

            return old,new_file

        form = input("Учитывать тип файла (.txt) при работе? y/n (д/н): ")
        old, new_file = construct(form)

        Old = old.read() # Откритие файла для чтения
        new = Old.upper() # Перевод всех букв в верхний регистр(Заглавные)


    elif konvert == "y" or konvert == "д":
        print()
        new = input("Ведите текст для конвертации: \n \n" )

    else:
        print("")
        print("НЕ КОРРЕКТНАЯ КОМАНДА")




    new = new.upper() # Перевод всех букв в верхний регистр(Заглавные)

    def modern(new): # Функция превращения текста в азбуку морзе
        new = new.replace("«", '"')
        new = new.replace("»", '"')
        new = new.replace("А","· − ")
        new = new.replace("Б","− · · · ")
        new = new.replace("В","· − − ")
        new = new.replace("Г","− − · ")
        new = new.replace("Д","− · · ")
        new = new.replace("Е","· ")
        new = new.replace("Ё","· ")
        new = new.replace("Ж","· · · − ")
        new = new.replace("З","− − · · ")
        new = new.replace("И","· · ")
        new = new.replace("Й","· − − − ")
        new = new.replace("К","− · − ")
        new = new.replace("Л","· − · · ")
        new = new.replace("М","− − ")
        new = new.replace("Н","− · ")
        new = new.replace("О","− − − ")
        new = new.replace("П","· − − · ")
        new = new.replace("Р","· − · ")
        new = new.replace("С","· · · ")
        new = new.replace("Т","− ")
        new = new.replace("У","· · − ")
        new = new.replace("Ф","· · − · ")
        new = new.replace("Х","· · · · ")
        new = new.replace("Ц","− · − · ")
        new = new.replace("Ч","− − − · ")
        new = new.replace("Ш","− − − − ")
        new = new.replace("Щ","− − · − ")
        new = new.replace("Ъ","− · · − ")
        new = new.replace("Ы","− · − − ")
        new = new.replace("Ь","− · · − ")
        new = new.replace("Э","· · − · · ")
        new = new.replace("Ю","· · − − ")
        new = new.replace("Я","· − · − ")
        new = new.replace("1","· − − − − ")
        new = new.replace("2","· · − − − ")
        new = new.replace("3","	· · · − − ")
        new = new.replace("4","· · · · − ")
        new = new.replace("5","· · · · · ")
        new = new.replace("6","− · · · · ")
        new = new.replace("7","− − · · · ")
        new = new.replace("8","− − − · · ")
        new = new.replace("9","− − − − · ")
        new = new.replace("0","− − − − − ")
        new = new.replace(".","· · · · · · ")
        new = new.replace(",","· − · − · − ")
        new = new.replace(":","− − − · · · ")
        new = new.replace(";","− · − · − · ")
        new = new.replace("(","− · − − · ")
        new = new.replace(")","− · − − · − ")
        new = new.replace("'","	· − − − − · ")
        new = new.replace('"',"· − · · − · ")
        new = new.replace("-","− · · · · − ")
        new = new.replace("—","− · · · · − ")
        new = new.replace("/","− · · − · ")
        new = new.replace("_","· · − − · − ")
        new = new.replace("?","· · − − · · ")
        new = new.replace("!","− − · · − − ")
        new = new.replace("+","· − · − · ")
        new = new.replace("@","· − − · − · ")
        new = new.replace("=","− · · · − ")

        return new

    new = modern(new)

    print()
    Spaces = input("Убрать пробелы?(y/n)(д/н): " )
    Spaces = Spaces.lower() # Перевод полученых значений в нижний регистр для приёма введеных больших букв

    if Spaces == "y" or Spaces == "д" :
        new = new.replace(" ","")

    elif Spaces == "n" or Spaces == "н":
          print()

    else:
        print("")
        print("НЕ КОРРЕКТНАЯ КОМАНДА")

    if konvert == "y" or konvert == "д":
        print()
        print("Результат: \n " + new)

    elif konvert == "n" or konvert == "н":
        new_file.write(new) # Запись текста в виде азбуки морзе в новый файл

        # Закрытие текстовых файлов
        new_file.close()
        old.close()


    print("")
    print("---------------------------------------------------")
    print("|                Текст конвентирован              |")
    print("---------------------------------------------------")
    print("")



# Происходит если не было найдено файла с начальным текстом
except FileNotFoundError:
    print("")
    print("НЕ НАЙДЕНО ФАЙЛА С НАЧАЛЬНЫМ ТЕКСТОМ")
    print("")
    print("ВОЗМОЖНЫЕ ПРОБЛЕМЫ: ")
    print("")
    print('    - ОТСУТСТВИЕ ФАЙЛА С ИМЕНЕМ "Normal text" В ОДНОЙ ПАПКЕ С ИСПОЛНЯЕМЫМ ФАЙЛОМ')
    print("    - НЕ ВЕРНО УКАЗАН ТИП ФАЙЛА")
    print("")

# Убирает оповещение о NameError если было введено не корректное значение в вопросе с учитиванием типа файла
except NameError:
    print()
