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
    results = {}
    results_num = 0
    for n, entry in enumerate(data):        
        if entry != None and (request.values['query'] in (' '.join([[lu.translation for lu in homograph.lexical_units] for homograph in entry.homographs][0])) or request.values['query'] in (' '.join([sign.hamnosys for sign in entry.signs]))):
            results[n] = entry
            results_num += 1
    return render_template('search.html', results = results, results_num = results_num, query = request.values['query'] )

'''@app.route('/edit', methods=['post'])

@app.route('/save', methods=['post'])
def save():
    
    
    return redirect'''

@app.route('/word/<int:word_n>')
def word(word_n):
    entry = data[word_n]
    return render_template('word_pickle.html', entry = entry)

@app.route('/test/<page>')
def testpage(page):
    return render_template(page)


if __name__ == '__main__':
    app.run(debug = True)

