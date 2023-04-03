from flask import Flask, render_template, redirect
import os


app = Flask(__name__)
app.secret_key = 'mourex'

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)