"""
URL configuration for bible project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name=''),
    path('main', main.views.index, name='home'),
    path('page', main.views.page, name='page'),
    path('nav', main.views.nav, name='search_nav'),
    path('search', main.views.search, name='search'),
    path('detail/<int:post_id>', main.views.detail, name='detail'),
    path('select', main.views.select, name='select'),
    path('selected_page', main.views.selected_page, name='selected_page'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
