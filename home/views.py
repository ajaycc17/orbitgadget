import json
import urllib
import math
from blog.models import BlogPost, Topic
from home.models import Contact
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings


def home(request):
    categories = Topic.objects.all()[:6]
    count = []
    for cat in categories:
        count.append((cat.title, BlogPost.objects.all().filter(
            category=cat, publish=True).count()))
    postCount = dict(count)
    allPosts = BlogPost.objects.all().filter(
        publish=True).order_by('-timeStamp')[:6]
    context = {'allPosts': allPosts,
               'postCount': postCount, 'topics': categories}
    return render(request, 'home/home.html', context)


def aboutPage(request):
    return render(request, 'home/about.html')


def contribute(request):
    return render(request, 'home/contribute.html')


def disclosure(request):
    return render(request, 'home/disclosure.html')


def privacyPolicy(request):
    return render(request, 'home/privacy-policy.html')


def siteTerms(request):
    return render(request, 'home/site-terms.html')


def contactPage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if len(name) < 2 and len(phone) < 10:
            messages.warning(request, 'Please fill the details correctly')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=message)

            # Begin reCAPTCHA validation
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                contact.save()
                messages.success(request, 'Your message has been delivered.')
            else:
                messages.warning(
                    request, 'Invalid reCAPTCHA. Please try again.')

    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query')

    if query is None or query == '' or len(query) > 200:
        query = 'No Results'
        context = {'query': query}
        return render(request, 'home/search.html', context)

    else:
        topics = Topic.objects.all()
        allPostsTitle = BlogPost.objects.filter(publish=True).filter(
            title__icontains=query)
        allPostsContent = BlogPost.objects.filter(publish=True).filter(
            content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        total = allPosts.count()

        postCount1 = len(allPosts)
        no_of_posts = 12
        page = request.GET.get('page')
        if page is None:
            page = 1
        else:
            page = int(page)

        if page > 1:
            prev = page - 1
        else:
            prev = None

        postCount2 = math.ceil(postCount1/no_of_posts)

        if page < postCount2:
            nxt = page + 1
        else:
            nxt = None

    allPosts = allPosts.order_by(
        '-timeStamp')[(page-1)*no_of_posts:page*no_of_posts]
    params = {'allPosts': allPosts, 'query': query,
              'prev': prev, 'nxt': nxt, 'total': total, 'topics': topics}
    return render(request, 'home/search.html', params)
