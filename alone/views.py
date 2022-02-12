from django.shortcuts import redirect, render

# Create your views here.
from django import forms
from django.contrib.auth.models import User

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]

def signup(request):
    form = signupform()
    if request.method == "POST":
        form=signupform(request.POST)
        if form.is_valid():
            # form.save() ..................... DIDN'T WORK!!❌⚠😡
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            new_user=User.objects.create_user(username=username,email=email,password=password)
            new_user.save()
            login(request,new_user)
            return redirect("welcome")
            print ("DONE!!!!!!")
    return render(request,"alone/signup.html",{"form":form})

class loginform(forms.Form):
    username = forms.CharField(max_length=150,label="username or email")
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)


from django.db.models import Q
from django.contrib.auth import login,logout
def signin(request):
    form=loginform()
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(Q(username=username)|Q(email=username)).first()
            if user != None:
                if user.check_password(password):
                    msg = "you are signed in"
                    login(request,user)
                    return redirect("welcome")
                else:
                    msg = "Incorrect username or password"
            else:
                msg="user does not exist"
            return render(request,"alone/login.html",{"form":form,"msg":msg})
    return render(request,"alone/login.html",{"form":form})

def welcome(request):
    if request.user.is_authenticated:
        return render(request,"alone/welcome.html")
    else:
        return redirect("login")

def signout(request):
    logout(request)
    return redirect("login")