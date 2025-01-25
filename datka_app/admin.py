from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class NewsAdminForm(forms.ModelForm):

    content_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание новости на русском')
    content_kg = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание новости на кыргзыском')

    class Meta:
        model = News
        fields = '__all__'


class NewsImageStackedInline(admin.TabularInline):

    model = Images
    extra = 1

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title_ru','get_image')
    list_display_links = ('id','title_ru',)
    readonly_fields = ('published_date', 'get_big_image')
    search_fields = ('title_ru',)
    list_filter = ('published_date',)
    inlines = [NewsImageStackedInline,]
    form = NewsAdminForm


    @admin.display(description='Изображение')
    def get_image(self, item):
        if item.images.first():
            return mark_safe(f'<img src="{item.images.first().image.url}" width="100px">')
        return '-'
    
    @admin.display(description='Изображение')
    def get_big_image(self, item):
        if item.images.first():
            return mark_safe(f'<img src="{item.images.first().image.url}" width="100%">')
        return '-'


admin.site.register(Adminstration)
admin.site.register(Jobs)
admin.site.register(Admins)
admin.site.register(Earth)
admin.site.register(Glava)
admin.site.register(Agricultural)
admin.site.register(StateLand)
admin.site.register(Resolution)


# Register your models here.
