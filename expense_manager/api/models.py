from django.db import models

class Category:
    def __init__(self, type):
        self.type = type

category = Category(type = "Продукты")
