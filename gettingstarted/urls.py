
# from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import Tienda.views

urlpatterns = [
    path('', include('Tienda.urls')), 
    path("db/", Tienda.views.db, name="db"),
    path('admin/', admin.site.urls),
    # Uncomment this and the entry in `INSTALLED_APPS` if you wish to use the Django admin feature:
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
    # path("admin/", admin.site.urls),
]
