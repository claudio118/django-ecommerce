"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include


from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import RedirectView, TemplateView

from accounts.views import LoginView, RegisterView, GuestRegisterView

from carts.views import cart_home

from .views import home_page, about_page, contact_page


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include(('accounts.urls', 'accounts'), namespace='account')),
    path('accounts/', include('accounts.passwords.urls')),
    path('contact/', contact_page, name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('cart/', include(('carts.urls', 'carts'), namespace='cart')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
    path('products/', include(("products.urls", 'products'), namespace='products')),
    path('search/', include(("search.urls", 'search'), namespace='search')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
