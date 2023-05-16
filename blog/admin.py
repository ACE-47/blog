from django.contrib import admin
from .models import Auther,Tag,Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter=('auther','tag','date')
    list_display =('title','date','auther')

    prepopulated_fields={'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=('user_name','post')

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Auther)
admin.site.register(Comment,CommentAdmin)
