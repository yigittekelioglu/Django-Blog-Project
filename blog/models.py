import string
from random import random

from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from colorfield.fields import ColorField


# Create your models here.



class movie_type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

choices = (
    ('News', 'News'),
    ('Sport', 'Sport'),
    ('Travel', 'Travel'),
    ('Technology', 'Technology'),
)
class bloger_type(models.Model):
    type = models.CharField(choices=choices,max_length=100)

    def __str__(self):#admin panelinde isimleri ile listelenmelerini sağlıyor
        return self.type


class movie_cast(models.Model):

    genders = (
        ('M', 'Erkek'),
        ('F', 'Kadın'),
    )

    duty_types = (
        ('1','Görevli'),
        ('2', 'Oyuncu'),
        ('3', 'Yönetmen'),
        ('4', 'Senarist'),
    )

    first_name = models.CharField(max_length=50, verbose_name='İsim')
    last_name = models.CharField(max_length=50, verbose_name='Soyisim')
    biography = models.TextField(validators= [MinLengthValidator(20)], verbose_name='Biyografi')
    image = models.FileField(upload_to="images", verbose_name='Kişi Fotoğrafı')
    date_of_birth = models.DateField(verbose_name='Doğum Tarihi')
    gender = models.CharField(max_length=1, choices=genders, verbose_name='Cinsiyet')
    duty_type = models.CharField(max_length=1, choices=duty_types, verbose_name='İş Pozisyonu')
    nationality = models.CharField(max_length=50, verbose_name='Uyruk')
    castslug = models.SlugField(unique=True, verbose_name='Kişi Slug')

    class Meta:
        verbose_name = "Kast Ekibi"
        verbose_name_plural = "Kast Ekibi"

    #def save(self, *args, **kwargs):
        #self.castslug = slugify(self.first_name)
        #super().save(args, kwargs)

    @property #oyuncunun admin panelinde isminin gözükmesi icin admin.py list_display ile birlikte calısıyo
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    full_name.fget.short_description = "isim soyisim"

    def __str__(self): #bak
        return f"{self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type)-1][1]})"


class Movie(models.Model):
    movie_title = models.CharField(max_length=100, verbose_name="Film İsmi")
    movie_description = models.TextField(validators= [MinLengthValidator(20)], verbose_name='Film Açıklaması')
    mark = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Film Puanı")
    movie_pic = models.FileField(upload_to="images", verbose_name='Film Fotoğrafı')
    movie_date = models.DateField(auto_now = True, verbose_name="Film İncelemesi Oluşturma Tarihi")
    movie_slug = models.SlugField(unique=True, verbose_name='Film Slug')
    movie_budget = models.DecimalField(max_digits=20, decimal_places=0, verbose_name="Film Bütçesi")
    cast_people = models.ManyToManyField(movie_cast, related_name='movie_cast', verbose_name="Film Kadrosu")
    movie_types = models.ManyToManyField(movie_type, verbose_name='Film Tipi')

    class Meta:
        verbose_name = "Film İncelemesi"
        verbose_name_plural = "Film İncelemeleri"
    #def save(self, *args, **kwargs):
        #self.movie_slug = slugify(self.movie_title)
        #super().save(args, kwargs)

    def __str__(self):
        return self.movie_title

class Bloger(models.Model):
    bloger_title = models.CharField(max_length=100, verbose_name="Blog Yazısı Başlığı")
    bloger_description = models.TextField(validators= [MinLengthValidator(20)], verbose_name='Blog Yazısı')
    bloger_pic = models.FileField(upload_to="images", verbose_name='Blog Yazısı Fotoğrafı')
    bloger_date = models.DateField(auto_now = True, verbose_name="Blog Yazısı Oluşturma Tarihi")
    bloger_slug = models.SlugField(unique=True, verbose_name='Blog Yazısı Slug')
    bloger_types = models.ManyToManyField(bloger_type, verbose_name='Blog Yazısı Tipi')

    class Meta:
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yazıları"

    # def save(self, *args, **kwargs):
    #     self.bloger_slug = slugify(self.bloger_title)
    #     super().save(args, kwargs)
    def __str__(self):
        return self.bloger_title

class movie_video(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class bloger_video(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    bloger = models.ForeignKey(Bloger, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class WebsiteSettings(models.Model):
    settingname = models.CharField(max_length=40, null=True, verbose_name="Site Ayarı İsmi", help_text="Site Ayarı ismini giriniz")
    navbarcolor = ColorField(default="#0D50B0",verbose_name="Menü Rengi",help_text="Menü rengini giriniz.")
    navbarlogo = models.CharField(max_length=250,verbose_name="Menü Logosu",help_text="Menü logosunu giriniz.")
    backgroundcolor =  ColorField(default="#EEF1F4",verbose_name="Arka Plan Rengi",help_text="Site için arka plan rengi giriniz.")
    aboutustext = models.TextField(max_length=500,verbose_name="Hakkımızda Bilgisi",help_text="Hakkımızda kısmını doldurunuz.")
    contactphone = models.CharField(max_length=250,verbose_name="İletişim Numarası",help_text="İletişim numarası giriniz.")
    contactmail = models.CharField(max_length=250,verbose_name="İletişim Maili",help_text="İletişim maili giriniz.")
    contactadres = models.TextField(max_length=250,verbose_name="İletişim Adres",help_text="İletişim adresi giriniz.")
    footer = models.CharField(max_length=250,verbose_name="Footer Metni",help_text="Footer metni giriniz.")
    footercolor = ColorField(default="#d6d9e3",verbose_name="Footer Rengi",help_text="Footer rengini giriniz.")
    bottomfootercolor = ColorField(default="#0D50B0",verbose_name="Alt Footer Rengi",help_text="Alt Footer rengini giriniz.")
    twitter = models.CharField(max_length=250,verbose_name="Twitter URL Bağlantısı",help_text="Twitter adresinizi giriniz.")
    facebook = models.CharField(max_length=250,verbose_name="Facebook URL Bağlantısı",help_text="Facebook adresinizi giriniz.")
    instagram = models.CharField(max_length=250,verbose_name="Instagram URL Bağlantısı",help_text="Instagram adresinizi giriniz.")

    class Meta:
        verbose_name = "Web Sitesi Ayarı"
        verbose_name_plural = "Web Sitesi Ayarları"