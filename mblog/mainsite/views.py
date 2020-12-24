from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime

# Create your views here.


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
    post_lists = list()
    # 遍历数据对象，组合成一个索引
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) +"<hr>")
        post_lists.append("<small>" + str(post.body.encode('utf-8'))\
                          +"</small><br><br>")
    return HttpResponse(post_lists)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
