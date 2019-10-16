from django.shortcuts import render, HttpResponse


def post_list(request):
    return render(request, 'blog/post_list.html')
