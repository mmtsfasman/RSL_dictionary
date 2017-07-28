from flask import Flask, render_template, request, url_for
import re
import sqlite3
import csv


app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',  methods=['get'])
def search():
    #text = request.form['text']
    data = open('data.csv','r', encoding = 'UTF-8')
    #conn = sqlite3.connect('data.csv')
    results = []
    results_num = 0
    for l in data:
        if request.values['request'] in l:
            attr = l.split(';')
            word_info = []
            for info in attr:
                word_info.append(info)
            results.append(word_info)
            results_num += 1
    return render_template('search.html', results = results, results_num = results_num)

@app.route('/word/<word>')
def word(word):
    data = open('data.csv','r', encoding = 'UTF-8')
    word_info = []
    for l in data:
        if word in l:
            word_info = l.split(';')
    return render_template('word.html', results = word_info)


if __name__ == '__main__':
    app.run(debug = True)

