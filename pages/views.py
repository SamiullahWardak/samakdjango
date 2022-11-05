from django.shortcuts import render

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world!!</h1>")
    return render(request, "home.html")

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html")

def social_view(request, *args, **kwargs):
    return render(request, "social.html")

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us!",
        "my_number": 123,
        "my_list": ['s', 'sam', 1, 23, 23, 14],
        "my_html": "<h1>My html in h1 tag</h1>"
    }
    return render(request, "about.html", my_context)
