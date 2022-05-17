import requests


# функция отправки ответа на задание по установленной форме


def add_answer_form(first_name: str, last_name: str, answer: str, task_id: int):
    """Принимает в качестве параметров имя, фамилию, номер (id) задания и ответ, отправляет на сайт imsr.su
    и возвращает результат отправки"""
    session = requests.session()
    url = 'https://api.imsr.su/add_answer'
    form_answer = {'first_name': first_name, 'last_name': last_name, 'answer': answer, 'task_id': task_id}
    return session.post(url, data=form_answer)
