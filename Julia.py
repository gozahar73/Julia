import random
# настроения: радостное грустное никакое 
# команды: help movies communities dialog news

'''
1 - Рекомендовать фильмы по настроению пользователя.
2 - Рекомендовать тематические сообщества по интересам.
3 - Поддерживать беседу и рассказывать шутки.
4 - Рассказывать последние новости.
5 - Предлагать покупку фирменного мерча.
'''

START_PROMT = 'Введите команду(off - остановить, help - команды):'
OFF = 'off'
OFF_TRANSLATE = 'щаа'
QUESTION_MOOD = 'Какое у тебя настроение?'
MOOD_JOY = 'радостное'
MOOD_SAD = 'грустное'
MOOD_NO = 'никакое'
HELP = 'help'
MOVIES = 'фильм'
MOVIES2 = 'кино'
COMMUNITIES = 'сообществ'
DIALOG = 'бесед'
NEWS = 'новост'
DONT_UNDER = 'Извини. Я тебя не понимаю.'
SKILLS = 'Я могу порекомендовать фильм, порекомендовать сообщества, поддержать беседу, рассказать последние новости.'
INTEREST = 'Какое у вас хобби?'
INTEREST_SPORT = 'спорт'
INTEREST_MUSIC = 'музыка'
INTEREST_GAMES = 'игры'
JOKE = 'Хочешь шутку?'
YES = 'да'
YES2 = 'хочу'
NEWS_VARIANTS = ['Солнце взорвалось', 'Я сегодня смотрела как бегает собака', 'Сегодня холоднее чем вчера', 'Завтра погода может измениться']
AD = '\nРекомендую наш мерч!'
AD_RANDOM =  random.choice([AD, '']) 

answer = input(START_PROMT).lower()
while answer != OFF and answer != OFF_TRANSLATE:
    if answer == HELP:
        print(SKILLS)
    
    elif answer.find(MOVIES) >= 0 or answer.find(MOVIES2) >= 0:
        mood = input(QUESTION_MOOD).lower()
        if mood == MOOD_JOY:
            print('Рекомендую фильм - Лило и стич', AD_RANDOM)
        elif mood == MOOD_SAD:
            print('Рекомендую фильм - Драйв', AD_RANDOM)
        elif mood == MOOD_NO:
            print('Рекомендую фильм - Тупой и ещё тупее', AD_RANDOM)
    
    elif answer.find(COMMUNITIES) >= 0:
        interest = input(INTEREST)
        if interest == INTEREST_SPORT:
            print('Рекомендую Большой футбол', AD_RANDOM)
        elif interest == INTEREST_MUSIC:
            print('Рекомендую Филармония каждый день', AD_RANDOM)
        elif interest == INTEREST_GAMES:
            print('Рекомендую Пекарня', AD_RANDOM)
        
    elif answer.find(DIALOG) >= 0:
        answer_joke = input(JOKE)
        if answer_joke == 'не хочу' or answer_joke == 'нет':
            print('Не хочешь, как хочешь!', AD_RANDOM)
        elif answer_joke.find(YES) >= 0 or answer_joke.find(YES2) >= 0:
            print('А она тебя не хочет!', AD_RANDOM)
        else:
            print('Ответь как-то иначе', AD_RANDOM)

    elif answer.find(NEWS) >= 0:
        print(random.choice(NEWS_VARIANTS), AD_RANDOM)

    else:
        print(DONT_UNDER)
    answer = input(START_PROMT).lower()

    

print('Пока!')
