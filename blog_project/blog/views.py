from django.shortcuts import render
from .models import Posts
posts= [
    {
        'author':"Vanaja",
        'title':"One happy day",
        'content':"How did that day go!!!!!!!!",
        'date_posted':'May,24 2020'
    },

    {
        'author': "Shreya",
        'title': "Second happy day",
        'content': "How did that day go!!!!!!!!",
        'date_posted': 'May,25 2020'
    }
]

# Create your views here.
def home(request):
    context={
        'posts':Posts.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':"About"})
