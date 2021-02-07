from random import randrange

from flask import Flask, flash, redirect, render_template, \
    request, url_for, session
from flask_login import LoginManager, logout_user, login_required, \
    login_user, current_user, UserMixin
import pymongo
from flask_bootstrap import Bootstrap

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

info = pymongo.MongoClient('localhost', 27017)
db = info['series']
stream_num = db['search']  # number of collections in Twitch database
category = db.list_collection_names()  # list of name of all types of game
for game in db.list_collection_names():
    list = db[game].find()  # information of all anchors in one of collections
app = Flask(__name__)
app.debug = True

# Bootstrap(app)
def bar_base() -> Bar:
    c = (
        Bar()
        #init_opts=opts.InitOpts(theme=ThemeType.DARK)
        .add_xaxis([category[0], category[1], category[2], category[3], category[4], category[5]]) # category is the list of games' names
        .add_yaxis("Viewers", [db[game_name]["viewer"] for game_name in category]) # db is database
        # .add_yaxis("B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Viewers"))
    )
    return c

@app.route('/')
def index():
    if request.method == 'GET':
        total = stream_num.count()
    return render_template('index.html')

@app.route("/rank")
def rank():
    return render_template("plot.html")

@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route('/directory')
def directory():
    return render_template('categories.html', categories=category)

@app.route('/anchor-list')
def list():
    channel = request.args.get('uid')
    cursor = db[channel].find()
    documents = []
    for info in cursor:
        documents.append(info)
    return render_template('list.html', list=documents)

@app.route('/detail')
def detail():
    return render_template('detail.html')

def bar():
    pass


if __name__ == '__main__':
    app.run(debug=True)
