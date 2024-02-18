from django.contrib import admin

from blog.forms import ProductForm
from blog.models import Movie, Bloger, bloger_type, movie_type, movie_cast, movie_video, bloger_video, WebsiteSettings, \
    Product, ImagesGal


class BlogerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"bloger_slug": ["bloger_title"]}
    list_display = ('bloger_title', 'bloger_date')
    list_filter = ('bloger_types', 'bloger_date')
    # readonly_fields = ("bloger_slug",)


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"movie_slug": ["movie_title"]}
    list_display = ('movie_title', 'movie_budget', 'mark', 'movie_date')
    list_filter = ('movie_types', 'mark', 'movie_budget', 'movie_date')


class MovieCastAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    prepopulated_fields = {"castslug": ["first_name"] + ["last_name"]}

class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('settingname',)

class ProductImageInline(admin.TabularInline):
    model = ImagesGal
    resimEk = 5


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    inlines = [ProductImageInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        for file in request.FILES.getlist('image_files'):
            ImagesGal.objects.create(product=obj, image=file)


class ImagesGalAdmin(admin.ModelAdmin):
    list_display = ['product','title','image']

class KategoriAdmin(admin.ModelAdmin):
    ...



admin.site.site_header = "OleyBlog Admin Panel"
admin.site.register(Movie, MovieAdmin)
admin.site.register(Bloger, BlogerAdmin)
#admin.site.register(movie_type)
#admin.site.register(bloger_type)
#admin.site.register(movie_video)
#admin.site.register(bloger_video)
admin.site.register(movie_cast, MovieCastAdmin)
admin.site.register(WebsiteSettings, WebsiteSettingsAdmin)

admin.site.register(Product, ProductAdmin)
admin.site.register(ImagesGal, ImagesGalAdmin)