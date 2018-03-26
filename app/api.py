from flask import jsonify, request, abort
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all/", methods= ["GET", "POST"])
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts) 


@app.route("/api/topic/show/<int:post_id>", methods= ["GET"])
def topic_show_api(post_id):
    post_to_show = post_store.get_by_id(post_id)
    try:
        result = jsonify(post_to_show.as_dict())
    except AttributeError:
        result = abort(404, "topic with id: {post_id} doesn't exist ")
    return result


@app.route("/api/topic/delete/<int:post_id>", methods= ["DELETE"])
def topic_delete_api(post_id):
    try:
        post_store.delete(post_id)
        result = jsonify({"message": "Deleted item successfully !"})
    except ValueError:
        result = abort(404, "topic with id: {post_id} doesn't exist")
    return result


@app.route("/api/topic/add", methods= ["POST"])
def topic_add_api():
    request_data = request.get_json()
    try:        
        new_post = models.Post(request_data["title"], request_data["content"])
        post_store.add(new_post)
        result =  jsonify(new_post.__dict__())
    except KeyError:
        result = abort(404, "couldn't parse the request data !")
    return result


@app.route("/api/topic/update/<int:post_id>", methods= ["put"])
def topic_update_api(post_id):
    request_data = request.get_json()
    post_to_update = post_store.get_by_id(post_id)
    try:
        post_to_update.title = request_data["title"]
        post_to_update.content = request_data["content"]
        post_store.update(post_to_update)
        result = jsonify(post_to_update.__dict__())
    except AttributeError:
        result = abort(404, "topic with id: {post_id} doesn't exist")
    return result


@app.errorhandler(404)
def bad_request(error):
    return jsonify(message = error.description)