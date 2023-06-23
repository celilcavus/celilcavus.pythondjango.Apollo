from django.shortcuts import render
import django.http as x;
from . import models
# Create your views here.

def index(request):
    dataA = models.ApolloModelA.objects.last()
    dataP = models.ApolloModelP.objects.last()
    if dataA != None:
        model = {
            'index_dataA':dataA,
            'index_dataP':dataP
        }
        return render(request,'pages/index.html',model)
    else:
        return x.Http404().add_note("Sayfa Yüklenemedi..")
    
def contact(requst):
    if requst.method == "POST":
            mail = requst.POST["mail"]
            subject = requst.POST["subject"]
            message = requst.POST["message"]

            models.ApolloModelO2.objects.create(mail = mail,subject = subject,message = message)
            # models.ApolloModelO2.objects.
            return render(requst,'pages/index.html')