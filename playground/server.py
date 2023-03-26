
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'PLAYGROUND' #Renders nothing but a title.

@app.route('/play')
def play():
    return render_template('index.html', color='#9FC5F8') #Renders default blue 3 box.

@app.route('/play/<int:num>')
def box_times(num):
    return render_template('index.html', num=num, color='#9FC5F8') #Renders blue boxes x times.

@app.route('/play/<int:num>/<string:color>')
def color_of_boxes(num, color='blue'):
    return render_template('index.html', num=num, color=color) #Renders x boxes in color of choice.

if __name__ == '__main__':
    app.run(debug=True)