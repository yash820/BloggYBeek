from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import home,base,post,aboutview,category

urlpatterns = [
    path('', home),
    #
    path('blog/<slug:url>',post),
    path('about/',aboutview),
    path('category/<slug:url>',category)

    ]
