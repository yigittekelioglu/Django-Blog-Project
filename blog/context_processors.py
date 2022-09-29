from blog.models import WebsiteSettings


def settings(request):
    websitesettings = WebsiteSettings.objects.all()
    return {'websitesettings': websitesettings}