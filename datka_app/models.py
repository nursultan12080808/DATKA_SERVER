from django.db import models
from django.contrib.auth.models import User

class News(models.Model):

    STATUS_CHOICES = [
        ('draft', 'Черновик / Каражат'),
        ('published', 'Опубликовано / Жарыяланды'),
        ('archived', 'Архивировано / Архивге сакталды'),
    ]

    title_ru = models.CharField(max_length=150, verbose_name='Заголовок (рус)')
    title_kg = models.CharField(max_length=150, verbose_name='Заголовок (кырг)')
    content_ru = models.TextField(verbose_name='Текст новости (рус)')
    content_kg = models.TextField(verbose_name='Текст новости (кырг)')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    source_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Ссылка на источник')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='Статус')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']


class Images(models.Model):
    news = models.ForeignKey("News", related_name="images", on_delete=models.CASCADE, verbose_name="Новость")
    image = models.ImageField(verbose_name="Изображение", upload_to="news_images/")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

class Adminstration(models.Model):
    surname_kg = models.CharField(verbose_name="Фамилия (кырг)", max_length=20)
    name_kg = models.CharField(verbose_name="Имя (кырг)", max_length=20)
    middle_name_kg = models.CharField(verbose_name="Отчество (кырг)", max_length=20)
    job_ru = models.CharField(verbose_name="Должность (рус)", max_length=100)
    job_kg = models.CharField(verbose_name="Должность (кырг)", max_length=100)
    phone = models.CharField(verbose_name="Номер телефона", max_length=13)

    def __str__(self):
        return self.name_kg

    class Meta:
        verbose_name = "Администрация"
        verbose_name_plural = "Администрация"

class Jobs(models.Model):
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    job_ru = models.CharField(verbose_name="Должность (рус)", max_length=100)
    job_kg = models.CharField(verbose_name="Должность (кырг)", max_length=100)
    content_ru = models.TextField(verbose_name="Требования (рус)")
    content_kg = models.TextField(verbose_name="Требования (кырг)")
    phone = models.CharField(max_length=13, verbose_name="Номер телефона")

    def __str__(self):
        return self.job_ru

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Earth(models.Model):
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content_ru = models.TextField(verbose_name="Описание земельного участка (рус)")
    content_kg = models.TextField(verbose_name="Описание земельного участка (кырг)")
    requirement_ru = models.TextField(verbose_name="Требования (рус)")
    requirement_kg = models.TextField(verbose_name="Требования (кырг)")
    phone = models.CharField(max_length=13, verbose_name="Номер телефона")

    def __str__(self):
        return self.published_date

    class Meta:
        verbose_name = "Земельный участок"
        verbose_name_plural = "Земельные участки"

class Agricultural(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступно / Бар'),
        ('rented', 'Сдано в аренду / Арендада'),
        ('sold', 'Продано / Сатылды'),
        ('reserved', 'Забронировано / Броньдо'),
    ]

    name_ru = models.CharField(max_length=255, verbose_name="Название участка (рус)")
    name_kg = models.CharField(max_length=255, verbose_name="Название участка (кырг)")
    description_ru = models.TextField(verbose_name="Описание (рус)")
    description_kg = models.TextField(verbose_name="Описание (кырг)")
    status = models.CharField(
        max_length=50, 
        choices=STATUS_CHOICES,
        default='available',
        verbose_name="Статус"
    )
    price_per_year = models.DecimalField(
        max_digits=10, decimal_places=2, 
        null=True, blank=True, 
        verbose_name="Цена аренды в год (сом)")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    phone = models.CharField(max_length=13, verbose_name="Номер телефона")

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Сельхоз участок"
        verbose_name_plural = "Сельхоз участки"


class StateLand(models.Model):
    OWNERSHIP_STATUS_CHOICES = [
        ('state', 'Государственная / Мамлекеттик'),
        ('municipal', 'Муниципальная / Муниципалдык'),
        ('private', 'Частная / Жеке менчик'),
    ]

    USAGE_STATUS_CHOICES = [
        ('available', 'Доступно / Бар'),
        ('reserved', 'Забронировано / Броньда'),
        ('in_use', 'Используется / Колдонууда'),
        ('under_construction', 'Строительство / Курулушта'),
        ('sold', 'Продано / Сатылды'),
    ]

    name_ru = models.CharField(max_length=255, verbose_name="Название участка (рус)")
    name_kg = models.CharField(max_length=255, verbose_name="Название участка (кырг)")
    description_ru = models.TextField(verbose_name="Описание (рус)")
    description_kg = models.TextField(verbose_name="Описание (кырг)")
    purpose_ru = models.CharField(max_length=255, verbose_name="Цель использования (рус)")
    purpose_kg = models.CharField(max_length=255, verbose_name="Цель использования (кырг)")
    ownership_status = models.CharField(
        max_length=50,
        choices=OWNERSHIP_STATUS_CHOICES,
        default='state',
        verbose_name="Статус собственности"
    )
    usage_status = models.CharField(
        max_length=50,
        choices=USAGE_STATUS_CHOICES,
        default='available',
        verbose_name="Статус использования"
    )
    rental_price_per_year = models.DecimalField(
        max_digits=10, decimal_places=2, 
        null=True, blank=True, 
        verbose_name="Цена аренды в год (сом)")
    cadastral_number = models.CharField(max_length=50, blank=True, verbose_name="Кадастровый номер")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    access_type_ru = models.CharField(max_length=100, blank=True, verbose_name="Тип доступа")

    def __str__(self):
        return f"{self.name_ru}"
    
    class Meta:
        verbose_name = "Государственная земля"
        verbose_name_plural = "Государственные земля"



class Resolution(models.Model):
    resolution_number = models.CharField(max_length=50, verbose_name="Номер постановления")
    resolution_date = models.DateField(verbose_name="Дата постановления")
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок постановления (на русском)")
    title_kg = models.CharField(max_length=255, verbose_name="Заголовок постановления (на кыргызском)")
    content_ru = models.TextField(verbose_name="Содержание постановления (на русском)")
    content_kg = models.TextField(verbose_name="Содержание постановления (на кыргызском)")
    responsible_person_ru = models.CharField(
        max_length=255, verbose_name="Ответственное лицо или орган (на русском)", blank=True
    )
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
    notes_ru = models.TextField(blank=True, verbose_name="Примечания (на русском)")
    notes_kg = models.TextField(blank=True, verbose_name="Примечания (на кыргызском)")

    def __str__(self):
        return f"Постановление {self.resolution_number} от {self.resolution_date}"

    class Meta:
        verbose_name = "Постановление айыл окмоту"
        verbose_name_plural = "Постановления айыл окмоту"
        ordering = ['-resolution_date']


class Glava(models.Model):
    image = models.ImageField(verbose_name="Фото главы", upload_to="admin_images")
    surname = models.CharField(verbose_name="Фамилия (на русском)", max_length=20)
    name = models.CharField(verbose_name="Имя (на русском)", max_length=20)
    middle_name = models.CharField(verbose_name="Отчество (на русском)", max_length=20)
    phone = models.CharField(verbose_name="Номер телефона", max_length=13)

    def __str__(self):
        return f"{self.surname} {self.surname}"

    class Meta:
        verbose_name = "Глава"
        verbose_name_plural = "Главы"


class Admins(models.Model):
    image = models.ImageField(verbose_name="Фото руководства", upload_to="admin_images")
    surname_ru = models.CharField(verbose_name="Фамилия (на русском)", max_length=20)
    name_ru = models.CharField(verbose_name="Имя (на русском)", max_length=20)
    middle_name_ru = models.CharField(verbose_name="Отчество (на русском)", max_length=20)
    job_ru = models.CharField(verbose_name="Должность (на русском)", max_length=100)
    job_kg = models.CharField(verbose_name="Должность (на кыргызском)", max_length=100)
    phone = models.CharField(verbose_name="Номер телефона", max_length=13)

    def __str__(self):
        return f"{self.name_ru} {self.surname_ru}"

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"
