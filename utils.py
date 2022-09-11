import json

import data


def get_posts_all():
    """Функция возвращает посты"""
    with open("data/posts.json", "r", encoding="utf8") as json_file:
       return json.load(json_file)

#print(get_posts_all())

def get_posts_by_user(user_name):
    """Функция возвращает посты определенного пользователя"""
    posts = get_posts_all()
    user_posts = []

    for post in posts:

        if post['poster_name'] == user_name:
            user_posts.append(post)
    return user_posts
        # elif user_name == " ":
        #     return []
        # else:
        #     return ValueError

#print(get_posts_by_user("fdf"))

def get_comments_by_post_id(post_id):
    """Функция возвращает комментарии определенного поста"""
    comments = get_comments_all()
    posts_comments = []

    for comm in comments:
        if comm['post_id'] == post_id:
            posts_comments.append(comm)

    return posts_comments

#print(get_comments_by_post_id("здорово"))

def get_comments_all():
    """Функция возвращает список комментариев"""
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        list_of_posts = json.load(file)
        return list_of_posts
#print(get_comments_all())

def search_for_posts(query):
    """Функция возвращает список постов по ключевому слову"""
    dict_list = get_posts_all()
    user_input_lower = query.lower()
    search_list = []

    for dictionary in dict_list:
        post = dictionary['content'].lower()
        if user_input_lower in post:
            search_list.append(dictionary)
            continue
    return search_list

#print(search_for_posts("Квадратная"))

def get_post_by_pk(pk_post):
    """Функция возвращает один пост по его идентификатору"""
    dict_list = get_posts_all()

    for post in dict_list:
        if pk_post == post['pk']:
            return post
#print(get_post_by_pk(6))