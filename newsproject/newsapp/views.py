from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'newsapp/home.html')

def movie_news_view(request):
    news1 = 'In hindi cinema SRK is no longer king of Bollywood'
    news2 = 'Salman & Aishwarya going to marry soon...'
    news3 = "Thief Hritik Roshan is not available for Dhoom 4, as he's in jail (caught by ACP Bachchan) "
    news4 = "Actor Rajnikant is getting older & not getting good roles in movies, so he's taking Rebirth"
    news5 = "SSR consulted Swami Nityananda, for shifting his Meade 14” LX-600 to the heaven "
    my_dict = {'news1':news1, 'news2':news2, 'news3':news3, 'news4':news4, 'news5':news5}
    return render(request, 'newsapp/mnews.html', my_dict)

def politics_view(request):
    return render(request, 'newsapp/pnews.html')

def sports_view(request):
    return render(request, 'newsapp/snews.html')
