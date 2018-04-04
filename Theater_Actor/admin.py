from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


class CommentInline(admin.TabularInline):
    model = models.Comment

# attaching commment stack to theater_actor


class theater_actorAdmin(admin.ModelAdmin):
        inlines = [CommentInline]

# calling in admin panel


admin.site.register(models.theater_actor, theater_actorAdmin)
admin.site.register(models.Comment)
