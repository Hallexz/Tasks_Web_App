from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template_string('<h1>Welcome to My Web Application!</h1>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
