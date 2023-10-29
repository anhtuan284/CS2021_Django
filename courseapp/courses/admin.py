from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    readonly_fields = ['avatar']

    def avatar(self, Course):
        if Course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'\
            .format(url=Course.image.name)
        )


class LessonAdmin(admin.ModelAdmin):

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }
        js = ('/static/js/script.js', )


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
