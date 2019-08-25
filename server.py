import pymongo
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db_english = pymongo.MongoClient("127.0.0.1", 27017)["english"]


def insert_mongo(collection, query):
    args = query.get('args')
    col = db_english[collection]
    res = col.find_one({'args': args})

    try:
        res.get('_id')
    except Exception as e:
        print(args)
        col.insert(query)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # page = int(request.args.get('page') or 1)
        # query = db_english['danci'].find().skip((page - 1) * 10).limit(10)

        return render_template('index.html')
    elif request.method == 'POST':
        args = request.form['ci'].strip()

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
        query = {"args": args, "trans": trans, "pronounce": pronounce, "additional": additional, "index": args[0].upper()}
        insert_mongo('danci', query)

        return render_template('index.html', args=args, trans=trans, pronounce=pronounce, additional=additional)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
