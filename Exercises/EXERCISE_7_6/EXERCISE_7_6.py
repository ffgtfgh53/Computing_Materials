from flask import Flask, render_template, request
from csv import reader
app = Flask(__name__)

from pathlib import Path
print(Path(__file__))

LOAN = Path(__file__).joinpath('../data/LOAN.txt')
BOOK = Path(__file__).joinpath('../data/BOOK.txt')
MEMBER = Path(__file__).joinpath('../data/MEMBER.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loans', methods = ['GET', 'POST'])
def loans():
    uid, data, user = str(request.form['uid']), [], ''
    with MEMBER.open() as f:
        for row in reader(f):
            if row[0] == uid:
                user = ', '.join(row[1:])
    with LOAN.open() as f:
        for row in reader(f):
            if row[1] == uid:
                data.append([row[2],row[3],'On Loan' if row[4] != 'TRUE' else 'Returned'])
    for row in data:
        print(row)
        bookid = row[0]
        with BOOK.open() as f:
            for book_row in reader(f):
                if book_row[0] == bookid:
                    row[0:1] = book_row[1:]
    print(data)        
    return render_template('loans.html',user=user,data=data)

if __name__ == "__main__":
    app.run()
