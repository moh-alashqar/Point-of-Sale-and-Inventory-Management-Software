from django.contrib import admin
from django.urls import path, include
from backend_app import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'customers',views.CustomerView, 'customer')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
]
