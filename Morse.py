# -*- coding: utf-8 -*-

try:

    # Уточение типа файла для работи с ним
    def type(form):
        if form == "y" or form == "Y" or form == "д" or form == "Д":
            old = open(u'Normal text.txt',"r")
            new_file = open(u'New text.txt' , 'w')

        elif form == "n" or form == "N" or form == "н" or form == "Н":
            old = open(u'Normal text',"r")
            new_file = open(u'New text' , 'w')

        else:
            print("")
            print("НЕ КОРРЕКТНАЯ КОМАНДА")

        return old,new_file

    form = input("Учитывать тип файла (.txt) при работе? y/n (д/н): ")
    old, new_file = type(form)


    Old = old.read() # Откритие файла для чтения
    new = Old.upper() # Перевод все букв в заглавные(Большие)

    # Конвентирование текста в азбуку морзе
    def modern(new):
        new = new.replace("«", '"')
        new = new.replace("»", '"')
        new = new.replace("А","· −")
        new = new.replace("Б","− · · ·")
        new = new.replace("В","· − −")
        new = new.replace("Г","− − ·")
        new = new.replace("Д","− · ·")
        new = new.replace("Е","·")
        new = new.replace("Ё","·")
        new = new.replace("Ж","· · · −")
        new = new.replace("З","− − · ·")
        new = new.replace("И","· ·")
        new = new.replace("Й","· − − −")
        new = new.replace("К","− · −")
        new = new.replace("Л","	· − · ·")
        new = new.replace("М","− −")
        new = new.replace("Н","− ·")
        new = new.replace("О","	− − −")
        new = new.replace("П","· − − ·	")
        new = new.replace("Р","· − ·")
        new = new.replace("С","· · ·")
        new = new.replace("Т","−")
        new = new.replace("У","· · −")
        new = new.replace("Ф","· · − ·")
        new = new.replace("Х","· · · ·")
        new = new.replace("Ц","− · − ·")
        new = new.replace("Ч","− − − ·")
        new = new.replace("Ш","− − − −")
        new = new.replace("Щ","− − · −	")
        new = new.replace("Ъ","− · · −")
        new = new.replace("Ы","− · − −")
        new = new.replace("Ь","− · · −")
        new = new.replace("Э","· · − · ·")
        new = new.replace("Ю","· · − −")
        new = new.replace("Я","· − · −")
        new = new.replace("1","· − − − −")
        new = new.replace("2","· · − − −")
        new = new.replace("3","	· · · − −")
        new = new.replace("4","· · · · −")
        new = new.replace("5","· · · · ·")
        new = new.replace("6","− · · · ·")
        new = new.replace("7","− − · · ·")
        new = new.replace("8","− − − · ·")
        new = new.replace("9","− − − − ·")
        new = new.replace("0","− − − − −")
        new = new.replace(".","· · · · · ·")
        new = new.replace(",","· − · − · −")
        new = new.replace(":","− − − · · ·")
        new = new.replace(";","− · − · − ·")
        new = new.replace("(","− · − − ·")
        new = new.replace(")","− · − − · −")
        new = new.replace("'","	· − − − − ·")
        new = new.replace('"',"· − · · − ·")
        new = new.replace("-","− · · · · −")
        new = new.replace("—","− · · · · −")
        new = new.replace("/","− · · − ·")
        new = new.replace("_","· · − − · −")
        new = new.replace("?","· · − − · ·")
        new = new.replace("!","	− − · · − −")
        new = new.replace("+","· − · − ·")
        new = new.replace("@","· − − · − ·")
        new = new.replace("=","− · · · −")

        return new

    new = modern(new)

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
    print("")
