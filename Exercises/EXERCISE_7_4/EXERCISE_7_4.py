## EXERCISE_7_4.py
from flask import Flask, render_template
from csv import reader

app = Flask(__name__)

@app.route('/')
def index():
    data = [['Full name', 'Screen name', 'Identity']]
    with open('../resources/people.txt') as f:
        r = reader(f)
        for i in r:
            data.append(i)
            #What is diff between full name and screen name???
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run()