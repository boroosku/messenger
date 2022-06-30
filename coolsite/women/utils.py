from .models import *

menu = [
        {'title': "Главная", 'url_name': 'home'},
        {'title': "Добавить пост", 'url_name': 'add_page'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context[menu] = menu
        return context