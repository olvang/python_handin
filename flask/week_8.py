from flask import Flask, jsonify, abort, request
import mysql.connector as mysql

app = Flask(__name__)
connection = mysql.connect(
    host="localhost", user="root", passwd="toortoor", db="python_week8")
cursor = connection.cursor(prepared=True)


@app.route('/joke', methods=['POST'])
def add_joke():
    joke = request.json
    query = "insert into jokes (value) values (%s)"
    cursor.execute(query, (joke["value"],))
    connection.commit()
    joke["id"] = cursor.lastrowid

    return jsonify(joke)


@app.route('/joke', methods=['GET'])
def get_all_jokes():
    query = "select * from jokes"
    cursor.execute(query)
    result = cursor.fetchall()

    jokes = []
    for joke in result:
        jokes.append({"id": joke[0], "text": "Random Joke", "value": joke[1]})

    return jsonify(jokes)


if __name__ == '__main__':
    app.run(debug=True)
