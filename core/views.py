from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User, Sight

def index(request):
    return render(request, "login_signup.html")

def login_or_signup(request):
    return render(request, "login_signup.html")

def dashboard(request):
    return render(request, "dashboard.html")

def add_sight(request):
    return render(request, "add_sight.html")

def edit_sight(request):
    return render(request, "edit_sight.html")

def view_sight(request):
    return render(request, "view_sight.html")


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

        print(f"User: {first} signed up!")
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
def import_sight(request):
    if request.method == "POST":
        location = request.POST.get('location')
        date = request.POST.get('date')
        sas_amount = request.POST.get('sas_amount')
        description = request.POST.get('description')
        made_by = request.POST.get('made_by')

        print(location,date,sas_amount,description,made_by)
        sight = Sight.objects.create(
            location = location,
            posted_by = made_by,
            date = date,
            sas_amount = sas_amount,
            description = description
        )

    return HttpResponse("success")

@csrf_exempt
def get_sights(request):
    if request.method == "GET":
        sights = list(Sight.objects.all().values())  
        return JsonResponse(sights, safe=False)
    



@csrf_exempt
def get_specific_sight(request):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            sight = Sight.objects.filter(id=id).values().first()
            if sight:
                return JsonResponse(sight, safe=False)
            else:
                return HttpResponse("Sight not found", status=404)
        except Exception as e:
            return HttpResponse("Error retrieving sight", status=500)


@csrf_exempt
def delete_sight(request):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            sight = Sight.objects.filter(id=id).first()
            if sight:
                sight.delete()
                return HttpResponse("Sight deleted")
            else:
                return HttpResponse("Sight not found", status=404)

        except Exception as e:
            print(e)

