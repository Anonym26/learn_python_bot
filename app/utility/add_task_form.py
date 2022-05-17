import requests


# функция отправки задания по установленной форме


def add_task_form(title: str, description: str, start_code: str, comment: int):
    """Принимает в качестве параметров: название, описание, код, коментарий и отправляет на сайт imsr.su,
    и возвращает результат отправки"""
    session = requests.session()
    url = 'https://api.imsr.su/add_request'
    form_task = {'title': title, 'description': description, 'start_code': start_code, 'comment': comment}
    return session.post(url, data=form_task)
