"""
In earlier projects we were defining urls at project level

Here we're defining url patterns at application level instead of project level
=>>
    for this we've to create separate urls.py file at application level and
    include this application level urls.py file to project level urls.py
=>>
    this promotes reusability of the application
    project level urls.py is clean & more readable
"""

from django.urls import path
from urlapp import views

urlpatterns = [
    path('first/', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
    path('fourth/', views.fourth_view),
    path('fifth/', views.fifth_view)
]

# now include all this urls at the project level urls.py file
