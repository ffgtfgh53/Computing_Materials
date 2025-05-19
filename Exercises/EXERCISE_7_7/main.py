from flask import Flask, render_template
from pathlib import Path
app = Flask(__name__)


decompressed = Path(__file__).joinpath('.../images/decompressedimage.txt')

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

@app.route('/')
def index():
    with open('decompressedimage.txt') as f:
        data = f.read().split('\n')
    colour_dict = {'000':'red',
                   '001':'white',
                   '010':'yellow',
                   '011':'blue',
                   '100':'black',
                   '110':'green'}
    data = list(map(lambda a: colour_dict[a], data))
    data = split_list(data, 9)
    return render_template('image.html', data=data)

if __name__ == "__main__":
    app.run()
