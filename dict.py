from flask import Flask, render_template, request, url_for
import re
import sqlite3
from datetime import datetime

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',  methods=['post'])
def search():
    #text = request.form['text'] #
    data = open('data.csv','r', encoding = 'UTF-8').read()
    conn = sqlite3.connect('data.csv')
    results = {}
    results_num = 0
    for l in data:
        if request.values['request'] in l:
            results.append(l)
            results_num += 1
    return render_template('search.html', results = results, results_num = results_num)

@app.route('/word/<word>')
def signpage():
    data = open('data.csv','r', encoding = 'UTF-8')
    for l in data:
        if request.values['RSL_word'] in l:
            results.append(l)
    return render_template('word.html', results = results, word = id_word)


if __name__ == '__main__':
    app.run(debug = True)

