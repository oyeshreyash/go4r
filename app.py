from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Jo link diya hai vahi jao bey!'

@app.route('/😂')
def test():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
