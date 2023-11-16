from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home2.html')

@app.route('/rome')
def page2():
    return render_template('rome1.html')

@app.route('/japan')
def page3():
    return render_template('JAPAN.html')

if __name__ == '__main__':
    app.run(debug=True)
