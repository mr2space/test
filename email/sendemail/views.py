from django.http import HttpResponse
from django.shortcuts import render
from .email import SendEmailThread
def emailSend(request):
    file = request.FILES['img']
    print(file)
    SendEmailThread("ech@themedius.ai",file ).run()
    SendEmailThread("HR@themedius.ai",file ).run()
    return render(request, "success.html")
    
def index(request):
    return render(request, "index.html")