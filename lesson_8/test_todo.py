import pytest
from TodoMain import Task

zadacha = Task()

def test_todo():
    list = zadacha.get_list()
    assert list.status_code == 200

    params = {"title": "Автоматизация", "completed": 'false'}
    task = zadacha.create (params)
    assert task is not None
    
    params = {f"title": "Автоматизация - сильно"}
    renamed_task = zadacha.rename(task, params)
    assert renamed_task.json()['title'] == "Автоматизация - сильно"

    info = zadacha.info(task)
    assert info.json()['title'] == "Автоматизация - сильно"
    assert info.json()['id'] == task

    params = {"complited", 'true'}
    status_true = zadacha.change_status(task, params)
    assert status_true == True

    params = {"complited", 'false'}
    status_false = zadacha.change_status(task, params)
    assert status_false == False

    deleting = zadacha.delete(task)
    assert deleting == 204
