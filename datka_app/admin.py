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



class JobsAdminForm(forms.ModelForm):

    content_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Требования на русском')
    content_kg = forms.CharField(widget=CKEditorUploadingWidget(), label='Требования на кыргзыском')

    class Meta:
        model = Jobs
        fields = '__all__'


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    form = JobsAdminForm



class EarthAdminForm(forms.ModelForm):

    requirement_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание земельного участка на русском')
    requirement_kg = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание земельного участка на кыргзыском')

    content_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание земельного участка на русском')
    content_kg = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание земельного участка на кыргзыском')

    class Meta:
        model = Earth
        fields = '__all__'


@admin.register(Earth)
class EarthAdmin(admin.ModelAdmin):
    form = EarthAdminForm


class AgriculturalAdminForm(forms.ModelForm):

    description_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание на русском')
    description_kg = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание на кыргзыском')

    class Meta:
        model = Agricultural
        fields = '__all__'


@admin.register(Agricultural)
class AgriculturalAdmin(admin.ModelAdmin):
    form = AgriculturalAdminForm



class StateLandAdminForm(forms.ModelForm):
    

    description_ru = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание на русском')
    description_kg = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание на кыргзыском')

    class Meta:
        model = StateLand
        fields = '__all__'


@admin.register(StateLand)
class StateLandAdmin(admin.ModelAdmin):
    form = StateLandAdminForm



class ResolutionFileStackedInline(admin.TabularInline):

    model = File
    extra = 1

@admin.register(Resolution)
class ResolutionAdmin(admin.ModelAdmin):
    form = ResolutionFileStackedInline



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
admin.site.register(Admins)
admin.site.register(Glava)


# Register your models here.
