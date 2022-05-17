import requests


def search_task_for_id(id_task):
    """Принимает номер задания и возвращает текст задания либо False"""
    response = requests.get('https://api.imsr.su/main/get_tasks').json()
    for i in response['data']:
        if i['id'] == int(id_task):
            return i['description']
    return False

