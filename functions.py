import json
from pprint import pprint as pp
from exceptions import DataLoadError


class PostsManager:
    """
    Класс для обработки постов. Загружает для чтения данные из json
    по ссылке (path), ищет посты по части слова
    """
    def __init__(self, path):
        self.path = path

    def load_posts_from_json(self):
        with open(self.path, "r", encoding="utf-8") as file:
            posts_data = json.load(file)

        return posts_data

    def search_posts_by_substring(self, substring):
        substring_lower = substring.lower()
        posts_selected = []

        posts_data = self.load_posts_from_json()
        for post in posts_data:
            search_text = post["content"].lower()
            if substring_lower in search_text:
                posts_selected.append(post)

        return posts_selected

    def overwrite_json_data(self, posts_data):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(posts_data, file, ensure_ascii=False)

    def add_post_to_json_list(self, new_post):
        posts_data = self.load_posts_from_json()
        posts_data.append(new_post)
        self.overwrite_json_data(posts_data)



# проверка на ошибки
# try:
#     POST_PATH = "posts.json"
#     post_manager = PostsManager(POST_PATH)
#     post_manager.load_posts_from_json()
#
# except DataLoadError:
#     print("Проблема с загрузкой файла")

# визуализация данных
# print(post_manager.load_posts_from_json())

# add extra exceptions for substring part -

POST_PATH = "posts.json"
post_manager = PostsManager(POST_PATH)
post_manager.load_posts_from_json()
print(post_manager.load_posts_from_json())
print(len(post_manager.load_posts_from_json()))

# print(post_manager.search_posts_by_substring("пур"))

# test_path = "https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80"
# content = "Пурр-пурр!"
#
new_post = {"pic": "test url", "content": "test content here"}
post_manager.add_post_to_json_list(new_post)
pp(len(post_manager.load_posts_from_json()))

