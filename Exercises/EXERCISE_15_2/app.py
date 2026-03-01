
from flask import Flask, render_template, request
from pymongo import MongoClient;

phone = MongoClient('localhost', port=27017)["jp_mobile"]["phone"]
print(*list(phone.find()), sep='\n')

app = Flask(__name__)

@app.route('/')
def main():
    brand = request.args.get("brand", default='')
    phones = phone.find({'brand': brand})
    return render_template('index.html.jinja', brand=brand, phones=phones)

if __name__ == '__main__':
    app.run(debug=True)
