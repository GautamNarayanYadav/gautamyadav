from django.contrib import admin

from system.models import *


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'name', 'email', 'subject', 'message', 'datetime')
    readonly_fields = ('datetime', )


admin.site.register(Message, MessageAdmin)
admin.site.register(MyProfile)
admin.site.register(Visit)


