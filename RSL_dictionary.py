from flask import Flask, render_template, request, url_for
import re
import csv
from model import *
#import model
import pickle
from wtf_edit import EntryForm

app = Flask (__name__)

app.config['SECRET_KEY'] = 'd3f4 4703 d962 a98c 9d7b 9dd9 9410 4d5c'

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

@app.route('/edit', methods=['POST', 'GET'])
@app.route('/edit/<int:word_n>', methods=['POST', 'GET'])
def edit(word_n):
    if word_n:
        entry = data[word_n]
        entry = EntryForm(obj=entry)
    #if entry valid:
    #data.append
    #write to pickle
    return render_template('edit.html', entry = entry)

'''@app.route('/save', methods=['post'])
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

