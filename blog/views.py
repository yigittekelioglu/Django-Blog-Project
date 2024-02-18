from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Movie, Bloger, movie_cast, Product
import random



def index(request):
    sliders = Product.objects.all()
    news = Bloger.objects.filter(bloger_types__type="News")
    sport = Bloger.objects.filter(bloger_types__type="Sport")
    travel = Bloger.objects.filter(bloger_types__type="Travel")
    technology = Bloger.objects.filter(bloger_types__type="Technology")
    movie = Movie.objects.all()

    #all_news = list(Bloger.objects.filter(bloger_types__type="News"))
    recent_new = news.order_by('-id')[:3]
    recent_sport = sport.order_by('-id')[:1:-1]
    recent_travel = travel.order_by('-id')[:1:-1]
    recent_technology = technology.order_by('-id')[:1:-1]
    recent_movie = movie.order_by('-id')[:6:-1]


    #number_of_news = news.count()
    #news_random = random.randint(0, number_of_news-1)


    # number_of_news = news.count()
    # random_new = random.sample(news, number_of_news)
    #
    # all_sport = list(Bloger.objects.filter(bloger_types__type="Sport"))
    # number_of_sport = sport.count()
    # random_sport = random.sample(all_sport, number_of_sport)
    #
    # all_travel = list(Bloger.objects.filter(bloger_types__type="Travel"))
    # number_of_travel = travel.count()
    # random_travel = random.sample(all_travel, number_of_travel)
    #
    # all_technology = list(Bloger.objects.filter(bloger_types__type="Technology"))
    # number_of_technology = technology.count()
    # random_technology = random.sample(all_technology, number_of_technology)
    #
    # all_movie = list(Movie.objects.all())
    # number_of_movie = movie.count()
    # random_movie = random.sample(all_movie, number_of_movie)



    context = {
        "news": news,
        "sport": sport,
        "travel": travel,
        "technology": technology,
        "movie": movie,
        "recent_new": recent_new,
        "recent_sport": recent_sport,
        "recent_travel": recent_travel,
        "recent_technology": recent_technology,
        "recent_movie": recent_movie,
        "sliders": sliders
        #"random_new": random_new,
        # "random_sport": random_sport,
        # "random_travel": random_travel,
        # "random_technology": random_technology,
        # "random_movie": random_movie
    }
    return render(request, 'blog/index.html', context)


def list(request, slug):
    if slug == 'news':
        news = Bloger.objects.filter(bloger_types__type="News").order_by('-id')
        context = {
            "news": news
        }
        return render(request, 'blog/list.html', context)

    elif slug == 'sport':
        sport = Bloger.objects.filter(bloger_types__type="Sport").order_by('-id')
        context = {
            "sport": sport
        }
        return render(request, 'blog/list.html', context)

    elif slug == 'travel':
        travel = Bloger.objects.filter(bloger_types__type="Travel").order_by('-id')
        context = {
            "travel": travel
        }
        return render(request, 'blog/list.html', context)

    elif slug == 'technology':
        technology = Bloger.objects.filter(bloger_types__type="Technology").order_by('-id')
        context = {
            "technology": technology
        }
        return render(request, 'blog/list.html', context)

    elif slug == 'movie':
        movie = Movie.objects.all().order_by('-id')
        context = {
            "movie": movie
        }
        return render(request, 'blog/list.html', context)


def details(request, slug):
    blog = Bloger.objects.get(bloger_slug=slug)
    context = {
        "blog": blog
    }
    return render(request, 'blog/details.html', context)



def moviedetails(request, slug):
    movie = Movie.objects.get(movie_slug=slug)
    #moviecast = Movie.objects.filter(cast_people__in=)
    #moviecast = Movie.objects.filter(cast_people__in=value)
    #moviecast = movie_cast.objects.filter(movie__cast_people=)
    #moviecast = movie_cast.objects.all()
    context = {
        "movie": movie,
        #"movie_cast": moviecast
    }
    return render(request, 'blog/moviedetails.html', context)


@login_required(login_url="/account/login")
def castdetails(request, slug):
    moviecast = movie_cast.objects.get(castslug=slug)
    context = {
        "moviecast": moviecast,
    }
    return render(request, 'blog/castdetails.html', context)


def catalog(request):
    if request.method == 'GET':
        q = request.GET['q']
        if q and q is not None:
            product = Bloger.objects.filter(bloger_title__contains=q)
            product2 = Movie.objects.filter(movie_title__contains=q)


        else:
            return HttpResponse

        context = {
            "products": product,
            "products2": product2,
        }

        return render(request, 'blog/catalog.html', context)

