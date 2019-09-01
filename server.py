import math

import pymongo
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_paginate import get_page_parameter, Pagination

app = Flask(__name__)
CORS(app)
db_english = pymongo.MongoClient("127.0.0.1", 27017)["english"]
col = db_english['danci']
PER_PAGE = 13


def insert_mongo(query):
    args = query.get('args')
    res = col.find_one({'args': args})
    try:
        res.get('_id')
    except Exception as e:
        col.insert(query)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # page = int(request.args.get('page') or 1)
        page = request.args.get(get_page_parameter(), type=int, default=1)
        start = (page - 1) * PER_PAGE
        pagination = Pagination(bs_version=3, page=page, total=col.count(), per_page_parameter=PER_PAGE)
        result = list(col.find().sort('_id', 1).skip(start).limit(PER_PAGE))
        return render_template('index.html', result=result, page=pagination)
    elif request.method == 'POST':
        args = request.form['ci'].strip()
        if args:
            result = [col.find_one({'args': args})]
            if result:
                return render_template('index.html', args=args, result=result)
            else:
                print(args)
                url = "http://dict.youdao.com/w/" + args + "/"
                soup = BeautifulSoup(requests.get(url).text, features="html.parser")
                trans = soup.find('div', {'id': 'phrsListTab'}).find_all("ul", limit=1)[0]
                if trans:
                    trans = trans.text.strip('\n').split('\n')

                pronounce = soup.find('div', {'id': 'phrsListTab'}).find("div", {"class": "baav"})
                if pronounce:
                    pronounce = pronounce.text.strip('\n')

                additional = soup.find('div', {'id': 'phrsListTab'}).find("p", {"class": "additional"})
                if additional:
                    additional = additional.text
                query = {"args": args, "trans": trans, "pronounce": pronounce, "additional": additional}
                insert_mongo(query)

                return render_template('index.html', result=query)
        else:
            result = list(col.find().sort('_id', 1).limit(PER_PAGE))
            pagination = Pagination(bs_version=3, page=1, total=col.count())
            return render_template('index.html', result=result, page=pagination)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
