import requests


# функция получения и сохранения id последнего задания
def get_id_last_task():
    """Получает id последнего задания. Сравнивает его с предыдущим последним id. Если больше то обновляет значение."""
    link = 'https://api.imsr.su/main/get_tasks'
    responce = requests.get(link).json()
    id_last_task = responce['data'][-1]['id']

    with open('app/utility/id_last_task.txt', 'r', encoding='UTF-8') as file:
        text = file.read()

    if id_last_task > int(text):
        with open('app/utility/id_last_task.txt', 'w', encoding='UTF-8') as file:
            file.write(str(id_last_task))
        return id_last_task
    else:
        return False



