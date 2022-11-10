"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from library.models import Book, Notes
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root),
    path('books/', views.BookList.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer), name='booklist'),
    path('featured/', views.FeaturedList.as_view(queryset=Book.objects.filter(featured=True), serializer_class=FeaturedSerializer), name='featuredlist'),
    path('notes/', views.NoteList.as_view(queryset=Note.objects.all(), serializer_class=NoteSerializer), name='notelist'),
    path('create/', views.CreateBook.as_view({'get': 'list'}), name='book-create')
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
