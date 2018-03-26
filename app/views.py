from flask import render_template, request, redirect, url_for, abort, jsonify
from app import app, post_store, models


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=enumerate(post_store.get_all()))


@app.route("/topic/add", methods=["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_add.html")


@app.route("/topic/edit/<int:post_id>", methods=["GET", "POST"])
def topic_edit(post_id):
    post_to_edit = post_store.get_by_id(post_id)
    if post_to_edit is None:
        abort(404)	
    
    if request.method == "POST":
        post_to_edit.title = request.form["title"]
        post_to_edit.content = request.form["content"]
        return redirect(url_for("home"))
    else:
        title = post_to_edit.title
        content = post_to_edit.content
        return render_template("topic_update.html", title=title, content=content, post_id=post_id)
	

@app.route("/topic/show/<int:post_id>")
def topic_show(post_id):
    post_to_show = post_store.get_by_id(post_id)
    title = post_to_show.title
    content = post_to_show.content
    return render_template("topic_show.html", title=title, content=content)


@app.route("/topic/delete/<int:post_id>")
def topic_delete(post_id):
    post_store.delete(post_id)
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', message = error.description)


