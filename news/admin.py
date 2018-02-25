from django.contrib import admin


from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'is_published',
        'id',
        'title',
        'date_created',
        'date_updated'
    ]
    ordering = ['-date_updated']


admin.site.register(News, NewsAdmin)