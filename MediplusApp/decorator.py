from django.shortcuts import render


def is_checkloginorRegister(func):
    def inner(request):
        if request.user.is_authenticated:
            return render(request,"MediplusApp/home.html")
        else:
            return func(request)
    return inner