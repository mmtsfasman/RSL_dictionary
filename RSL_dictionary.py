from flask import Flask, render_template, request, url_for
import re
import csv
from model import *
#import model
import pickle

app = Flask (__name__)

with open('database.pickle', 'rb') as datafile:
    data = pickle.load(datafile)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',  methods=['get'])
def search():
    #text = request.form['text']
    with open('data.csv', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
        results = []
        results_num = 0
        for row in data:
            #??????
            if row != None and request.values['request'] in row.homograph[0].lexical_unit[0].translation or request.values['request'] in row.sign[0].hamnosys:
                results.append(row)
                results_num += 1
    return render_template('search.html', results = results, results_num = results_num)

@app.route('/word/<int:word_n>')
def word(word_n):
    entry = data[word_n]
    return render_template('word_pickle.html', entry = entry)

@app.route('/test/<page>')
def testpage(page):
    return render_template(page)


if __name__ == '__main__':
    app.run(debug = True)

