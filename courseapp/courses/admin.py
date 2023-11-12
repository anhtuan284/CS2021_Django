from ckeditor_uploader import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path

from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


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
    form = LessonForm

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }
        js = ('/static/js/script.js', )


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'iSuccess'

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html')


admin_site = CourseAppAdminSite(name='myapp')

admin_site.register(Course, CourseAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag)
