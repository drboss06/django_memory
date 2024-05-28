from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('main.urls')),
    # path('api/', include('main.urls')),
    # path('add_place/', include('main.urls')),
    # path('add_memory/', include('main.urls')),
    # path('check_memory/', include('main.urls'))
    path("", include("main.urls")),
    path("accounts/", include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', include('polls.urls'))
]'''
