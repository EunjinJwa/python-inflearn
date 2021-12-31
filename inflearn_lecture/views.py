from django.shortcuts import render
from.models import MyText


# Create your views here.

def home_list(request) :
    texts = MyText.objects.filter()
    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})

