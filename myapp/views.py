from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # context={
    #     'name': "emma"
    #     'age': 65,
    #     'nationality':'kenyan'
    # }
    # name= ' annie'
    return render( request, 'index.html')

# def counter(request):
#     Words= request.GET['text']
#     amount_of_words= len(text.split())
#     return render(request," counter.html",{'amount':amount_of_words})
def counter(request):
     return render(request,'counter.html')