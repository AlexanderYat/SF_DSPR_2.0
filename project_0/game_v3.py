# Угадай число

import numpy as np

def random_predict(number:int=1) -> int:
    """Функция принимает число для угадывания и
    возвращает количество попыток, предпринятых для завершения угадывания.
    Используем двоичный поиск, чтобы угадать число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 1
    low_limit = 1
    high_limit = 100
    predict_number = low_limit + (high_limit - low_limit) // 2

    while number != predict_number:
        count += 1
        if number > predict_number:
            low_limit = predict_number + 1
        elif number < predict_number:
            high_limit = predict_number - 1
        predict_number = low_limit + (high_limit - low_limit) // 2

    return(count)
    
#print(random_predict(10))

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости результата
    random_array = np.random.randint(1,101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

    
score_game(random_predict)