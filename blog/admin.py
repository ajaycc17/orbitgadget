from django.contrib import admin
from blog.models import BlogComment, BlogPost, Topic

admin.site.register((BlogComment))
admin.site.register((Topic))
admin.site.register((BlogPost))