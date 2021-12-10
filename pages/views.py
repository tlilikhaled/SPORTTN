from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pages.forms import UserForm
from django.contrib.auth.models import User
from .helpers import send_forget_password_mail
from .models import UserInfo
from .admin import UserProfil
from django.contrib.auth.decorators import login_required
from products.models import Product
from cart.models import OrderItem,Order

# Create your views here.

def index(request):
        return render(request,"pages/index.html" )

def loginForm(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                if username and password:
                        user = authenticate(username=username , password=password)

                        if user is not None:
                                login(request, user)
                                return redirect('index')
                        else:
                                messages.error(request, "L'identifiant ou le mot de passe est incorrect") 
                else:
                        messages.error(request, 'Remplissez tous les champs')


        return render(request,"pages/login.html" )

def Register(request):
        
        if request.method == 'POST':
                form = UserForm(data=request.POST)
                if form.is_valid():
                        user = form.save()
                        user.set_password(user.password)
                        user.save()
                        messages.success(request, 'Merci pour ton inscription!')
                        return redirect('login')
                else:
                        print(form.errors)
        else:
                form = UserForm()

       
        return render(request,"pages/Register.html" , { 'form' : form })

def LogoutUser(request):
        logout(request)
        return redirect('login')

@login_required
def profil(request, user_id):
	if (request.user.is_authenticated and request.user.id == user_id):
		user_obj = User.objects.get(id=user_id)
		return render(request, "user_profil/profil.html",{'my_profile': user_obj})

       		

@login_required
def modifprofil(request):
        context = {}
        data = User.objects.get(id=request.user.id)
        context["data"]=data
        if request.method == 'POST':
                fn = request.POST["fname"]
                ln = request.POST["lname"]
                em = request.POST["email"]
                ph = request.POST["phone"]
                ad = request.POST["adress"]
                usr=User.objects.get(id=request.user.id)
                usr.first_name = fn
                usr.last_name = ln
                usr.email = em
                usr.save()
                data.phone = ph
                data.address = ad
                data.save()
                return render(request, "user_profil/profil.html")
                
        return render(request, "user_profil/modifierprofil.html",context) 


@login_required
def detcmd(request , ord_id):
        Cmd = OrderItem.objects.all()
        context = {'Cmd':Cmd,'ordid' : ord_id}
        return render(request,"user_profil/details_commande .html",context)        

@login_required
def hiscmd(request):
        Ord = Order.objects.all()
        #print(request.user.id)
        #print(Ord[1].customer)
        context = {
	'Ord':Ord,
	}

        return render(request, "user_profil/historique_commande.html",context) 


	

