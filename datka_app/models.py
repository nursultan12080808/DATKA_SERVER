from django.db import models
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import User

class News(models.Model):

    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
        ('archived', 'Архивировано'),
    ]

    title = models.CharField(max_length=200, verbose_name='Заголовок')  # Заголовок новости
    content = models.TextField(verbose_name='Текст новости')  # Текст новости
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')  # Дата публикации
    category = models.ForeignKey("datka_app.Category", on_delete=models.CASCADE, related_name="news", verbose_name="Категория")  # Категория новости
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автор')  # Автор
    source_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Ссылка на источник')  # Ссылка на источник
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')  # Статус
    tags = models.ManyToManyField('Tag', related_name='news_articles', blank=True, verbose_name='Теги')  # Теги
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')  # Дата последнего обновления

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

class Tag(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Название тега')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Category(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Images(models.Model):

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображении"

    news = models.ForeignKey("datka_app.News", related_name="images", on_delete=models.CASCADE, verbose_name="Новость")
    image = models.ImageField(verbose_name="Изображение", upload_to="news_images/")

class Adminstration(models.Model):

    class Meta: 
        verbose_name = "Администрация"
        verbose_name_plural = "Администрация"
    
    glava = models.BooleanField(verbose_name="Руководитель?", default=False)
    image = models.ImageField(verbose_name="Фото персонала", upload_to="admin_images")
    surname = models.CharField(verbose_name="Фамилия", max_length=20)
    name = models.CharField(verbose_name="Имя", max_length=20)
    middle_name = models.CharField(verbose_name="Отчество", max_length=20)
    job = models.CharField(verbose_name="Должность", max_length=100)
    phone = models.CharField(verbose_name="Номер",max_length=13)

class Jobs(models.Model):

    class Meta:
        verbose_name = "Конкурс кадров"
        verbose_name_plural = "Конкурс кадров"
    
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')  
    job = models.CharField(verbose_name="Должность", max_length=100)
    content = models.TextField(verbose_name="Требование")
    phone = models.CharField(max_length=13, verbose_name="номер телефона")

    def __str__(self) -> str:
        return f"{self.job}  {self.phone}"

class Earth(models.Model):

    class Meta:
        verbose_name = "Конкурс на землю"
        verbose_name_plural = "Конкурс на землю"

    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')  
    content = models.TextField(verbose_name="Описание земельного участка")
    requirement = models.TextField(verbose_name="Требование условия")
    phone = models.CharField(max_length=13, verbose_name="номер телефона")
    

class Agricultural(models.Model):

    class Meta:
        verbose_name = "Сельхоз назначения"
        verbose_name_plural = "Сельхоз назначения"

    name = models.CharField(max_length=255, verbose_name="Название участка")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(
        max_length=50, 
        choices=[
            ('available', 'Доступно'),
            ('rented', 'Сдано в аренду'),
            ('sold', 'Продано'),
            ('reserved', 'Забронировано'),
        ],
        default='available',
        verbose_name="Статус"
    )
    price_per_year = models.DecimalField(
        max_digits=10, decimal_places=2, 
        null=True, blank=True, 
        verbose_name="Цена аренды в год (в сомах)"
    )
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    phone = models.CharField(max_length=13, verbose_name="номер телефона")

    def __str__(self):
        return f"{self.name}"
    

class StateLand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название участка")
    description = models.TextField(verbose_name="Описание")
    purpose = models.CharField(max_length=255, verbose_name="Цель использования")
    ownership_status = models.CharField(
        max_length=50,
        choices=[
            ('state', 'Государственная'),
            ('municipal', 'Муниципальная'),
            ('private', 'Частная'),
        ],
        default='state',
        verbose_name="Статус собственности"
    )
    usage_status = models.CharField(
        max_length=50,
        choices=[
            ('available', 'Доступно'),
            ('reserved', 'Забронировано'),
            ('in_use', 'Используется'),
            ('under_construction', 'Строительство'),
            ('sold', 'Продано'),
        ],
        default='available',
        verbose_name="Статус использования"
    )
    rental_price_per_year = models.DecimalField(
        max_digits=10, decimal_places=2, 
        null=True, blank=True, 
        verbose_name="Цена аренды в год (в рублях)"
    )
    cadastral_number = models.CharField(max_length=50, blank=True, verbose_name="Кадастровый номер")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    access_type = models.CharField(
        max_length=100, blank=True, verbose_name="Тип доступа"
    )
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Государственная земля"
        verbose_name_plural = "Государственные земля"



from django.db import models

class Resolution(models.Model):
    resolution_number = models.CharField(max_length=50, verbose_name="Номер постановления")
    resolution_date = models.DateField(verbose_name="Дата постановления")
    title = models.CharField(max_length=255, verbose_name="Заголовок постановления")
    content = models.TextField(verbose_name="Содержание постановления")
    responsible_person = models.CharField(max_length=255, verbose_name="Ответственное лицо или орган", blank=True)
    execution_status = models.CharField(
        max_length=50, 
        choices=[
            ('in_progress', 'В процессе'),
            ('completed', 'Выполнено'),
            ('cancelled', 'Отменено'),
        ],
        default='in_progress',
        verbose_name="Статус выполнения"
    )
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    notes = models.TextField(blank=True, verbose_name="Примечания")
    def __str__(self):
        return f"Постановление {self.resolution_number} от {self.resolution_date}"
    
    class Meta:
        verbose_name = "Постановление айыл окмота"
        verbose_name_plural = "Постановления айыл окмота"
        ordering = ['-resolution_date']  # Сортировка по дате постановления, от нового к старому
