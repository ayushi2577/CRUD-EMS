import mysql.connector as ms
from flask import *
import os

app = Flask(__name__)

# ---------- DB SETUP ----------
def get_db():
    return ms.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        passwd=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT"))
    )

# ---------- ROUTES ----------

def init():
    mycon = get_db()
    cursor = mycon.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEES(
    EMP_ID INT PRIMARY KEY AUTO_INCREMENT,
    FNAME VARCHAR(50),
    LNAME VARCHAR(50),
    MOB BIGINT UNIQUE,
    MAIL VARCHAR(80),
    DOJ DATE,
    SALARY INT
    ) AUTO_INCREMENT = 1000
    """)

@app.route('/')
def home():
    return render_template('crud.html')


@app.route('/load')
def load():
    mycon = get_db()
    cursor = mycon.cursor()
    cursor.execute("SELECT * FROM EMPLOYEES")
    data = cursor.fetchall()

    result = {}
    for row in data:
        result[row[0]] = list(map(str, row[1:]))

    return jsonify(result)


@app.route('/add', methods=['POST'])
def add():
    mycon = get_db()
    cursor = mycon.cursor()
    d = request.get_json()

    cursor.execute(
        """INSERT INTO EMPLOYEES
        (FNAME, LNAME, MOB, MAIL, DOJ, SALARY)
        VALUES (%s,%s,%s,%s,%s,%s)""",
        (
            d['fname'],
            d['lname'],
            d['mob'],
            d['mail'],
            d['doj'],
            d['salary']
        )
    )
    mycon.commit()
    return jsonify(success=True)


@app.route('/update', methods=['POST'])
def update():
    mycon = get_db()
    cursor = mycon.cursor()
    up = request.get_json()
    eid = int(up.pop('Eid'))

    allowed = {
        'fname': 'FNAME',
        'lname': 'LNAME',
        'mob': 'MOB',
        'mail': 'MAIL',
        'doj': 'DOJ',
        'salary': 'SALARY'
    }

    for key, val in up.items():
        if key in allowed:
            if key == 'doj':
                cursor.execute(
                    "UPDATE EMPLOYEES SET DOJ=%s WHERE EMP_ID=%s",
                    (val, eid)
                )
            else:
                cursor.execute(
                    f"UPDATE EMPLOYEES SET {allowed[key]}=%s WHERE EMP_ID=%s",
                    (val, eid)
                )

    mycon.commit()
    return jsonify(success=True)


@app.route('/delete', methods=['POST'])
def delete():
    mycon = get_db()
    cursor = mycon.cursor()
    eid = int(request.get_json()['eid'])
    cursor.execute("DELETE FROM EMPLOYEES WHERE EMP_ID=%s", (eid,))
    mycon.commit()
    return jsonify(success=True)


@app.route('/find', methods=['POST'])
def find():
    mycon = get_db()
    cursor = mycon.cursor()
    data = request.get_json()

    n = data.get('name')
    sal = data.get('salary')
    doj = data.get('doj')

    query = "SELECT * FROM EMPLOYEES"
    cond = []

    if n:
        cond.append(f'FNAME LIKE "{n}%"')
    if sal:
        cond.append(f'SALARY >= {sal}')
    if doj:
        cond.append(f'DOJ >= "{doj}"')

    if cond:
        query += " WHERE " + " AND ".join(cond)

    cursor.execute(query)
    data = cursor.fetchall()

    result = {}
    for row in data:
        result[row[0]] = list(map(str, row[1:]))

    return jsonify(result)


@app.route('/clearall')
def clear():
    mycon = get_db()
    cursor = mycon.cursor()
    cursor.execute('DELETE FROM EMPLOYEES')
    mycon.commit()
    return jsonify(success=True)

init()

