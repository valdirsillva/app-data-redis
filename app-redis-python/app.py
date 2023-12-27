import redis
from flask import Flask

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, charset="utf-8", decode_responses=True)

r.set('person', 'Jhon Doe')
r.set('candidate', 'Mark Zukky')
r.set('student','Jhonas Emma')
r.set('Sport','Futebol')


@app.route('/')
def print_value():
    # Obtendo o valor contido em (person)
    get_person = r.get('person')
    print(get_person)

    return get_person

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)