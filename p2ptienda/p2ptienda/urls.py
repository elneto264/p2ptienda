"""p2ptienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
<<<<<< HEAD
from p2pApp.views import Carrazo
=======
from p2pApp import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
urlpatterns = patterns('',
    url(r'^stock/', include('stock.urls', namespace="stock")),
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
url(r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/',include(('p2pApp.urls','p2pApp'))),
    
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from usuario.views import RegistroUsuario,Login,logoutUsuario
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/',include(('p2pApp.urls','p2pApp'))),
<<<<<<< HEAD
    path('registrar/',RegistroUsuario.as_view(),name='registrar'), 
    path('accounts/login/',Login.as_view(),name ='login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    
 ] 
=======
   
    path('registrar/',RegistroUsuario.as_view(),name='registrar'), 
    path('accounts/login/',Login.as_view(),name ='login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
>>>>>>> c44c8b2f789dc14e2d45c420f2521e74ddf689b7
]
 
>>>>>>> ee067739651006e340e14deb9a4de2e7bb607437
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

