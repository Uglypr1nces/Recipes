from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User, Recipe

def index(request):
    return render(request, "login_signup.html")

def login_or_signup(request):
    return render(request, "login_signup.html")

def recipes(request):
    return render(request, "recipes.html")

def add_recipe(request):
    return render(request, "add_recipe.html")

def edit_recipe(request):
    return render(request, "edit_recipe.html")

def view_recipe(request):
    return render(request, "view_recipe.html")


@csrf_exempt
def sign_up(request):
     if request.method == "POST":
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name=first,
            last_name=last,
            email=email,
            password=password  
        )

        return HttpResponse("Signed up")

@csrf_exempt
def log_in(request):
     if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')


        try:
            user = User.objects.filter(email=email, password=password).first()
            
            if user:
                return HttpResponse(f"{user.first_name}")
            else:
                return HttpResponse("Couldn't find user")

        except:
            return HttpResponse("Couldnt find user")

     return HttpResponse("Tried Log In")

        

@csrf_exempt
def create_recipe(request):
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        description = request.POST.get('description')
        instructions = request.POST.get('instructions')
        time_required = request.POST.get('time_required')

        under_30 = time_required == "under-30"

        user = request.POST.get('first_name')

        Recipe.objects.create(
            name=recipe_name,
            under_30_minute=under_30,
            posted_by=user,
            description=description,
            instruction=instructions,
        )
    return HttpResponse("success")

@csrf_exempt
def get_recipes(request):
    if request.method == "GET":
        recipes = Recipe.objects.all().values()  
        return JsonResponse(list(recipes), safe=False)