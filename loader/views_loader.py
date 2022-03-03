from flask import Blueprint, render_template, request

from functions import PostsManager
POST_PATH = "posts.json"

# создаем блюпринт и называем его
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


# создаем вьюшки из блюпринт на разные страницы

# страница, куда можно прикреплять файл рисунка с текстовым полем
@loader_blueprint.route("/post")
def page_post_main():
    return render_template("post_form.html")


# как выглядит страница нового поста после добавления поста
@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    content = request.form.get("content")
    picture.save(f"./uploads/images/{picture.filename}")

    if not picture or not content:
        return "Ошибка загрузки"
    # return f"Загружена картинка {picture.filename}, содержимое поста {content}"

    picture_path = f"/uploads/images/{picture.filename}"

    new_post = {"pic": picture_path, "content": content}
    post_manager = PostsManager(POST_PATH)
    new_posts_list = post_manager.add_post_to_json_list(new_post)

    return render_template("post_uploaded.html",
                           content=content, picture_path=picture_path)



