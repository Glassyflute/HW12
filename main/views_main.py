from flask import Blueprint, render_template, request

from functions import PostsManager
POST_PATH = "posts.json"

# создаем блюпринт и называем его
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

# создаем вьюшки из блюпринт на разные страницы
@main_blueprint.route("/")
def page_index():
    return render_template("index.html")

# страница с результатами поиска по части слова, отображает список публикаций
@main_blueprint.route("/list")
def page_search():
    s = request.args.get("s")
    post_manager = PostsManager(POST_PATH)
    search_result = post_manager.search_posts_by_substring(s)

    return render_template("post_list.html", search_result=search_result, s=s)




