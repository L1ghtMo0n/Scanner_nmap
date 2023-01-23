k = 0
Mark = 0

tasks = [
    ["Задание #1: Просканируйте в вербальном режиме все TCP порты сервера scanme.nmap.com", "nmap -v scanme.nmap.org"],
    ["Задание #2: Проверить у рандомных 100 хостов наличие на них запущенных веб-серверов. Подсказка: порт 80", "nmap -v -iR 100000 -PN -p 80"],
    ["Задание #3: Напиши команду Nmap, которая будет сканировать IP-адресса из текстового файла 'SLAVES.txt'", "nmap -iL SLAVES.txt"],
    ["Задание #4: Простканируйте порты UDP на IP-адрессе из текстового файла 'SLAVES.txt'", "nmap -sU 192.168.200.1"],
    ["Задание #5: Выполните быстрое сканирование с помощью шаблона T5 сайт rsvpu.ru", "nmap -T5 rsvpu.ru"]
]

def getTask():
    userPrompt = input("$root: " + tasks[k][0] + "\n")
    if userPrompt == tasks[k][1]:
        print("Ответ верный!")
        global Mark
        Mark += 1
        return True
    else:
        print("Ответ неверный!")
        return False

if __name__ == "__main__":
    print("Тренажер: 'Сетевой сканер Nmap'\n")
    while k < len(tasks):
        task = getTask()
        k += 1
        if (task == False):
            break
    print("Спасибо за прохождения теста по командам Nmap. Итоговая оценка:", Mark, "балл(а)")
