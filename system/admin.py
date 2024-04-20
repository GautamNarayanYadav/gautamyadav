from django.contrib import admin

from system.models import *


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'name', 'email', 'subject', 'message', 'datetime')
    readonly_fields = ('datetime', )


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('id', 'intro', 'date', 'author')


admin.site.register(Message, MessageAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(MyProfile)


