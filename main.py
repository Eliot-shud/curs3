from flask import Flask, render_template, jsonify, request

import utils
from api.api import api_bp

app = Flask(__name__)

""" смотреть посты """


@app.route("/")
def view_posts():
    posts = utils.load_posts()
    return render_template('index.html', posts=posts)


""" видеть пост """


@app.route("/post/<int:pk>")
def view_post(pk):
    post = utils.load_post(pk)
    comments = utils.load_comments(pk)
    return render_template('post.html', post=post, comments=comments)


"""найти пользователя по имени или постам"""


@app.route("/user/<user_name>")
def search_post_by_user_name(user_name):
    posts = utils.load_posts(user_name=user_name)
    return render_template('index.html', posts=posts)


""" найти посты """


@app.route("/search/")
def search_post():
    word = request.args.get('s', '').lower()
    posts = utils.load_posts(search_word=word)
    return render_template('index.html', posts=posts)


""" сообщения из айпи """


@app.route("/api/")
def api_posts():
    posts = utils.load_posts()
    return jsonify(posts)


""" ответ из айпи """


@app.route("/api/post/<int:pk>")
def api_post(pk):
    post = utils.load_post(pk)
    return jsonify(post)


@app.errorhandler(500)
def server_error(e):
    return "500, Приносим извинения сервер не отвечает запросу .Попробуйте войти позже."


@app.errorhandler(404)
def not_found(e):
    return "404, Приносим извинения сервер не отвечает запросу .Попробуйте войти позже."


app.register_blueprint(api_bp)
app.run(debug=True)
