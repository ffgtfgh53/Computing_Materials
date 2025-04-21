from flask import Flask, render_template, request
app = Flask(__name__)

from pathlib import Path
csv_input = Path(__file__).with_name('log_ex8.csv')
template = Path(__file__).with_name('log_ex8.csv')

import csv

@app.route('/')
def homepage():
    with csv_input.open('r',encoding='utf-8') as f:
        header, *data = [i[:-1] for i in csv.reader(f)]
    return render_template('template.html', 
                           header=header, data=data)

if __name__ == "__main__":
    app.run()