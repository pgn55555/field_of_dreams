from random import randint
from time import sleep

goings = ['Назовите букву', 'Назовите букву', 'Назовите букву', 'Назовите букву', 'Назовите букву', 'Назовите букву', 'Можно открыть любую букву', 'Можно открыть любую букву','Можно открыть любую букву','Назовите букву', 'Назовите букву']

while True:
    word = list(input('Введите слово: '))
    print("\033[H\033[J")
    detected = [False for i in range(1, len(word) + 1)]
    
    game_go = True
    while game_go:
        for i in range(len(word)):
            if detected[i]:
                print(word[i] + ' ', end='')
            else:
                print(str(i + 1) + ' ', end='')
        
        print()
        print(goings[randint(0, 10)])
        ans = input()

        if ans.isnumeric():
            for i in range(len(word)):
                if word[i] == word[int(ans) - 1]:
                    detected[i] = True
        else:
            if ans in word:
                for i in range(len(word)):
                    if word[i] == ans:
                        detected[i] = True
            else:
                print('Такой буквы нет')
                sleep(3)
        
        print("\033[H\033[J")
