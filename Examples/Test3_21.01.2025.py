# ЗАДАНИЕ: Создание REST API с Flask
# Напишите простое REST API, которое работает со списком задач (TODO).
# Реализуйте следующие эндпоинты:
# - [POST] /tasks — Добавить новую задачу
# - [GET] /tasks — Получить список всех задач
# - [DELETE] /tasks/<id> — Удалить задачу по ID

#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Один',
    },
    {
        'id': 2,
        'title': u'Два',
    }
]

@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	task = filter(lambda t: t['id'] == task_id, tasks)
	task = list(task)
	if len(task) == 0:
		abort(404)
	return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(list(task)) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    return jsonify({'task': task[0]})
    
@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
    
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
