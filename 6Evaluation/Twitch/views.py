from random import randrange

from flask import Flask, flash, redirect, render_template, \
    request, url_for, session
# from flask_login import LoginManager, logout_user, login_required, \
#     login_user, current_user, UserMixin
import pymongo
# from flask_bootstrap import Bootstrap

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

info = pymongo.MongoClient('localhost', 27017)
db = info['single']
# stream_num = db['search']  # number of collections in Twitch database
category = db['games'].find()# list of name of all types of game
game_list = []
view_list = []
for game in list(category):
    print(game)
    game_list.append(game['name'])
    view_list.append(game['audience'])
print(view_list)
#category = list(category)
# for game in db.list_collection_names():
#     list = db[game].find()  # information of all anchors in one of collections
app = Flask(__name__)
app.debug = True


# Bootstrap(app)
def bar_base() -> Bar:
    c = (
        Bar()
        #init_opts=opts.InitOpts(theme=ThemeType.DARK)
        .add_xaxis([game_list[i] for i in range(10)]) # category is the list of games' names
        #.add_xaxis(["a", "b","c","d","e","f","g","h","i","j"])
        .add_yaxis("Viewers", [x/1000 for x in view_list]) # db is database
        #.add_yaxis("B", [randrange(0, 100) for _ in range(10)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Viewers"))
    )
    return c

@app.route('/')
def index():
    # if request.method == 'GET':
    #     total = stream_num.count()
    return render_template('index.html', verify=0)

@app.route("/rank")
def rank():
    return render_template("plot.html")

@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route('/directory')
def directory():
    list = []
    for name in game_list:
        list.append({name: name.replace(' ', '%20')})
    return render_template('categories.html', categories=list)

@app.route('/search')
@app.route('/search/<item>')
def get_result(item=None):
    keyword = request.args.get("key")
    if(next(db['games'].find({'name': keyword}))):
        return redirect("https://www.twitch.tv/directory/game/"+next(db['games'].find({'name': keyword}))['name'].replace(' ', '%20'))
    elif (next(db['channels'].find({'name': keyword}))):
        return redirect("https://www.twitch.tv/" + next(db['channels'].find({'name': keyword}))['streamername'].lower())
    else:
        return render_template('index.html', verify=1)

# @app.route('/anchor-list')
# def list():
#     channel = request.args.get('uid')
#     cursor = db[channel].find()
#     documents = []
#     for info in cursor:
#         documents.append(info)
#     return render_template('list.html', list=documents)

@app.route('/detail')
def detail():
    return render_template('detail.html')

def bar():
    pass


if __name__ == '__main__':
    app.run(debug=True)
