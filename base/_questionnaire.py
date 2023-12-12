QUESTIONS = {
    'имя': 'Как тебя зовут?',
    'пол': 'Твой пол? [м/ж]',
    'возраст': 'Сколько тебе лет?',
    'учёба': 'Где ты учи{}?',
    'работа': 'Где ты {}?',
    'хобби': 'Чем тебе интересно заниматься в свободное время?',
    'навыки': 'Что у тебя получается лучше всего?',
}
answers = dict.fromkeys(QUESTIONS)

strs_study_sex = ('лся', 'лась')
strs_study_age = 'шься'
strs_job_age = ('хочешь работать', 'работаешь')

for key, question in QUESTIONS.items():
    if key == 'учёба':
        insert = strs_study_sex[answers['пол'] == 'ж']
        insert = (strs_study_age, insert)[answers['возраст'] > 23]
    elif key == 'работа':
        insert = strs_job_age[answers['возраст'] > 23]
    else:
        insert = ''
            
    answer = input(f'\n{question.format(insert)}\n  ')
    
    answers[key] = answer if not answer.isdecimal() else int(answer)
