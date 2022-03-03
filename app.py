from flask import Flask, Blueprint, render_template, send_from_directory
from functions import PostsManager

# импортируем блюпринт
from loader.views_loader import loader_blueprint
from main.views_main import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


# # доступ к папке uploads, чтобы внешний клиент видел
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

