from django.contrib import admin
from newsroom.models import Category, Post,Comment,Tag,Contact,UserProfile,Newsletter

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Newsletter)