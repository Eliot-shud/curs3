import posts as posts
from flask import Blueprint, jsonify

import logger
import utils

api_bp = Blueprint('api',__name__, url_prefix='/api')
log = logger.get_logger('api')

@api_bp.route("/post/")
def api_post():
    post = utils.load_post()
    log.info(f"api_posts - > {len(posts)}")
    return jsonify(post)

@api_bp.route("/post/<int:pk>")
def api_post(pk):
    post = utils.load_post(pk)
    log.info(f"api_posts - > {pk}")
    return jsonify(post)
