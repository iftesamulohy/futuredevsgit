from django.http import HttpResponse
from django.shortcuts import render

from statickwork.models import Posts

# Create your views here.
def index(request):
    context = {
        "text":"its working",
        "navelements":[
            {
                "name":"home",
                "link":"#home"
            },
            {
                "name":"about",
                "link":"#about"
            },
            {
                "name":"pricing",
                "link":"#pricing"
            },
            {
                "name":"contact",
                "link":"#contact"
            },
            {
                "name":"support",
                "link":"#contact"
            }

        ],
        "posts":[
         {
            "category":"Cooking",
            "title":"I love Pasta",
            "duration":"30 min",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard",
            "btnText":"More",
            "date": "Oct 20",
            "image":"https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/pasta.jpg",
            "comments":[
               {
                  "name": "ifte",
                  "text":"nice post"
               },
               {
                  "name": "Samul",
                  "text":"good post"
               },
               {
                  "name": "Ohy",
                  "text":"well done"
               },
            ]
            
         },
          {
            "category":"Gaming",
            "title":"I hate Pubg",
            "duration":"30 min",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard",
            "btnText":"More",
            "date": "Oct 20",
            "image":"https://images.unsplash.com/photo-1494976388531-d1058494cdd8?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2Fyc3xlbnwwfHwwfHx8MA%3D%3D"
         },
          {
            "category":"Sports",
            "title":"I love Football",
            "duration":"30 min",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard",
            "btnText":"More",
            "date": "Oct 20",
            "image":"https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/pasta.jpg"
         },
          {
            "category":"Movies",
            "title":"I love Avengers",
            "duration":"30 min",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard",
            "btnText":"More",
            "date": "Oct 20",
            "image":"https://s3.eu-central-1.amazonaws.com/bootstrapbaymisc/blog/24_days_bootstrap/pasta.jpg",
          }

      ]
    }
    return render(request,'statickwork/index.html',context)

def about(request):
    post = Posts.objects.all()
    context={
        "posts":post
    }
    return render(request,'statickwork/index.html',context)