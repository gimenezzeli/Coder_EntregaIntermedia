from django.urls import path
from recipes.views import create_recipes, list_recipes, course

urlpatterns = [
    path('list-recipes/', list_recipes),
    path('create-recipes/', create_recipes),

    path('our-course/', course)
]