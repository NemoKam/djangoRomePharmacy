from django.shortcuts import render,redirect
from .models import Comment
def index(request):
    if request.method == 'GET':
        comms = Comment.objects.all()
        pharmacy = []
        for i in comms:
            if i.pharmacyname not in pharmacy:
                pharmacy.append(i.pharmacyname)
        return render(request,'index.html',{'user':request.user,'comments':comms,'pharmacy':pharmacy})
    if request.method == 'POST':
        pharmacy =request.POST.getlist('pharmacy')
        text = request.POST.get('text')
        if pharmacy == []:
            comms = Comment.objects.filter(text__icontains=text)
        else:
            comms = Comment.objects.filter(pharmacyname__in=pharmacy,text__icontains=text)
        comments = Comment.objects.all()
        pharmacy = []
        for i in comments:
            if i.pharmacyname not in pharmacy:
                pharmacy.append(i.pharmacyname)
        return render(request,'index.html',{'user':request.user,'comments':comms,'pharmacy':pharmacy})