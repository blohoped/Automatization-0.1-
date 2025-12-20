#модули и переменные
import os, subprocess, time, shutil

#просит пользователя имя для скрипта, и импортирует модули
def start():
    if os.path.exists("Auto"): #проверяет, есть ли вообще папка
        global fileName, filePath #делает глобальным переменные, чтобы их можно было использовать в мененджерах with
        os.system("cls")
        fileName=input("Введите имя для автоматизации: ") + ".py" #совмещает формат файла и название вместе
        filePath=f"Auto/{fileName}" #сохраняет путь, и в пути указывается название переменной
        with open(filePath, "a", encoding="utf-8") as f:
            f.write(f'import os, subprocess, time\n') #имортируются модели

    else: #нет - создаёт её и запускает заново
        os.makedirs("Auto")
        start()

#автоматизации
def auto():
    start()

    while True:
        os.system("cls")
        print("> Напишите команду, которая добавиться в автоматизацию!")
        time.sleep(0.1)
        print("<-------------------->")
        time.sleep(0.1)
        print("Доступные команды:")
        time.sleep(0.1)
        print("- написать <текст>")
        time.sleep(0.1)
        print("- удалить <пересоздаёт автоматизацию>")
        time.sleep(0.1)
        print("- открыть <открывает файл/ссылку, пути к файлу БЕЗ кавычек!>")
        time.sleep(0.1)
        print("- подождать <количество секунд>")
        time.sleep(0.1)
        print("- ввести <команда>")
        time.sleep(0.1)
        print("<-------------------->")
        time.sleep(0.1)
        print("Чтобы остановить работу конструктора, напишите стоп")
        time.sleep(0.1)
        auto=input("> ")

        #записывает команду print в файл, помещает содержимое в команду, и делает уведомление о завершении изменения файла
        if auto.startswith("написать"):
            txt=auto[9:]
            with open(filePath, "a", encoding="utf-8") as f:
                f.write(f'print("{txt}")\n')
            print("Команда добавлена в файл!")
            time.sleep(2)

        #удаляет, и начинает процедуру создания заново
        elif auto.startswith("удалить"):
            os.remove(filePath)
            print("Файл удалён")
            time.sleep(2)
            start() #всё начинает заново

        #записывает команду subprocess.run в файл, помещает содержимое в команду, и делает уведомление о завершении изменения файла
        #r стоит, чтобы python не жаловался на одиночные \
        elif auto.startswith("открыть "):
            txt=auto[8:]
            if not '"' in txt[0] and not '"' in txt[-1]: #проверяет кавычки в начале, и в конце
                with open(filePath, "a", encoding="utf-8") as f:
                    f.write(f'subprocess.Popen(r\'start "" "{txt}"\', shell=True)\n')
                print("Команда добавлена в файл!")
                time.sleep(2)
            else:
                print("БЕЗ КАВЫЧЕК!!")
                time.sleep(2)

        #записывает команду time.sleep в файл, помещает количество секунд в команду, и делает уведомление о завершении изменения файла
        elif auto.startswith("подождать"):
            numbers=auto[10:]
            if numbers.isdigit(): #проверяет, что пользователь вводит именно ЧИСЛО
                with open(filePath, "a", encoding="utf-8") as f:
                    f.write(f'time.sleep({int(numbers)})\n') #в int переводится для того, чтобы python перевёл переменную в число
                    print("Команда добавлена в файл!")
                    time.sleep(2)
            else:
                print("Пожалуйста, напишите ЦИФРУ")
                time.sleep(2)

        #записывает команду subprocess.Popen в файл, которая запускает команды из консоли
        elif auto.startswith("ввести"):
            txt=auto[7:]
            with open(filePath, "a", encoding="utf-8") as f:
                f.write(f'subprocess.Popen("{txt}", shell = True)\n')
            print("Команда добавлена в файл!")
            time.sleep(2)

        #ломает цикл, тем самым завершая работу конструктора
        elif auto.startswith("стоп"):
            os.system("cls")
            print("Поздравляю! Автоматизация создана")
            print("Теперь вы можете запускать сразу несколько задач одним файлом!")
            print("Это окно закроется через 3 секунды")
            time.sleep(2)
            break
        
#менюшка
def menu():
    os.system("cls")
    print("<--------------------------->")
    time.sleep(0.1)
    print("[1] - сделать автоматизацию")
    time.sleep(0.1)
    print("[2] - очистить папку")
    time.sleep(0.1)
    print("[3] - автор")
    time.sleep(0.1)
    print("[0] - выход")
    time.sleep(0.1)
    print("<--------------------------->")
    time.sleep(0.1)
    print("/made by blohoped")
    time.sleep(0.1)
    menu_choice=input("> ")

    #входит в конструктор
    if menu_choice == "1":
        auto()

    #удаляет папку и создаёт её заново
    elif menu_choice == "2":
        if os.path.exists("Auto"):
            os.system("cls")
            shutil.rmtree("Auto") #удаляет папку вместе с файлами
            os.makedirs("Auto") #создаёт её
            print("Папка очищена!")
            time.sleep(2)
            menu()

        else:
            os.makedirs("Auto")
            print("Проверяйте наличие папки!")
            time.sleep(2)
            menu()
    
    #ссылки автора
    elif menu_choice == "3":
        os.system("cls")
        print("Навигация по ссылкам автора:")
        time.sleep(0.1)
        print("<--------------------------->")
        time.sleep(0.1)
        print("[1] - GitHub")
        time.sleep(0.1)
        print("[2] - Донат")
        time.sleep(0.1)
        print("[3] - Telegram канал")
        time.sleep(0.1)
        print("[4] - выход")
        time.sleep(0.1)
        print("<--------------------------->")
        time.sleep(0.1)
        _answerAuthor = input("> ")

        if _answerAuthor == "1":
            os.system("start www.github.com/blohoped")
            menu()
        
        elif _answerAuthor == "2":
            os.system("start www.donationalerts.com/r/bloxoped1")
            menu()
        
        elif _answerAuthor == "3":
            os.system("start www.t.me/bloxoped1")
            menu()
        
        elif _answerAuthor == "4":
            menu()
        
        else:
            menu()

    elif menu_choice == "0":
        print("Выход")
    
    else:
        menu()
menu()