from django.contrib import admin
from django.urls import path, include
from main.views.errors import CustomErrorServer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('laboratory.urls'))
]


handler404 = CustomErrorServer.error_404
handler500 = CustomErrorServer.error_500