
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dic = {'user_first_name': 'Ganesh'}
    return render(request, 'index.html', my_dic)
