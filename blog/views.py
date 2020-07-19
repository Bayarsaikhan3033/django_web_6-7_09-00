from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def post(request):    
    posts = [
        {
            'title': 'Post1',
            'text': 'bla bla bla...',
            'created': '2020-07-19 10:30'
        },{
            'title': 'Post2',
            'text': 'gahahahahahaahah aaaaaaa',
            'created': '2020-07-10 15:36'
        },{
            'title': 'Post3',
            'text': 'python is best',
            'created': '2020-07-18 02:01'
        }
    ]

    return render(request, 'post.html', { 'data': posts })

def about(request):
    return render(request, 'about.html')

def comment(request):    
    return HttpResponse('comment')