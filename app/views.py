from flask import Flask, render_template, request, redirect, url_for, abort 
import models
from app import app, post_store, member_store


@app.route("/")
@app.route("/index/")
def home():
	return render_template("index.html", posts = post_store.get_all())


@app.route("/topic/add/", methods = ["GET", "POST"])
def topic_add():
	if request.method == "POST":
		new_post = models.Post(request.form["title"], request.form["content"])
		post_store.add(new_post)
		return redirect(url_for("home"))
	else:
		return render_template("topic_add.html")


@app.route("/topic/edit/<int:id>", methods = ["GET", "POST"])
def topic_update(id):
	post = post_store.get_by_id(id)
	if request.method == "POST":
		post.title = request.form["title"]
		post.content = request.form["content"]
		post_store.update(post)
		result = redirect(url_for("home"))
	elif request.method == "GET":
		result = render_template("topic_update.html", post= post_store.get_by_id(id))
	return result


@app.route("/topic/show/<int:id>")
def topic_show(id):
	post = post_store.get_by_id(id)
	return render_template("topic_show.html", post= post)


@app.route("/topic/delete/<int:id>")
def topic_delete(id):
	post_store.delete(id)
	return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", message=error.description)


