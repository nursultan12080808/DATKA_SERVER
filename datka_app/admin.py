from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class NewsAdminForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание новости')

    class Meta:
        model = News
        fields = '__all__'


class NewsImageStackedInline(admin.TabularInline):

    model = Images
    extra = 1

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category','get_image')
    list_display_links = ('id','title',)
    readonly_fields = ('published_date', 'get_big_image')
    filter_horizontal = ('tags',)
    search_fields = ('title','tags', 'category')
    list_filter = ('category', 'published_date')
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


@admin.register(Adminstration)
class AdminstrationAdmin(admin.ModelAdmin):
    list_display = ('id','surname', 'name','middle_name', 'job')
    list_display_links = ('id','surname', 'name', 'middle_name')
    readonly_fields = ('get_big_image',)
    search_fields = ('name','surname', 'middle_name')
    list_filter = ('id',)
    
    @admin.display(description='Изображение')
    def get_big_image(self, item):
        if item.image:
            return mark_safe(f'<img src="{item.image.url}" width="100%">')
        return '-'

admin.site.register(Jobs)
admin.site.register(Glava)
admin.site.register(Agricultural)
admin.site.register(StateLand)
admin.site.register(Resolution)
admin.site.register(Tag)
admin.site.register(Category)

# Register your models here.
