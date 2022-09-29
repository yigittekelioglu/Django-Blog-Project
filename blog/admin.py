from django.contrib import admin
from blog.models import Movie, Bloger,bloger_type, movie_type, movie_cast, movie_video, bloger_video, WebsiteSettings




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


admin.site.site_header = "OleyBlog Admin Panel"
admin.site.register(Movie, MovieAdmin)
admin.site.register(Bloger, BlogerAdmin)
#admin.site.register(movie_type)
#admin.site.register(bloger_type)
#admin.site.register(movie_video)
#admin.site.register(bloger_video)
admin.site.register(movie_cast, MovieCastAdmin)
admin.site.register(WebsiteSettings, WebsiteSettingsAdmin)