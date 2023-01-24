from django.shortcuts import render

from recipes.models import Recipes
from recipes.forms import RecipesForm


def create_recipes(request):
    if request.method == 'GET':
        context = {
            'form': RecipesForm()
        }
        return render(request, 'recipes/create_recipes.html', context= context)

    elif request.method == 'POST':
        form = RecipesForm(request.POST)
        if form.is_valid():
            Recipes.objects.create(
                name= form.cleaned_data['name'],
                ingredients= form.cleaned_data['ingredients'],
                recipe = form.cleaned_data['recipe'],
            )
            context={
                'message':'Receta creada exitosamente',
            }
            return render(request, 'recipes/create_recipes.html', context=context)
        else:
            context= {
                'form_errors': form.errors,
                'form': RecipesForm(),
            }
            return render(request, 'recipes/create_recipes.html', context=context)

def list_recipes(request):
    if 'search' in request.GET:
        search= request.GET['search']
        recipes= Recipes.objects.filter(name__icontains=search)
    else:
        recipes= Recipes.objects.all()

    context={
        'recipes': recipes,
    }
    return render(request, 'recipes/recipes.html', context=context)

def course(request):
    return render(request, 'course/course.html', context={})