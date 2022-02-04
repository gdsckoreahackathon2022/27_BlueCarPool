from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/', include('report.urls')),
    path('review/', include('review.urls')),
    path('recruitment/', include('recruitment.urls')),
    path('', include('recruitment.urls')),
]
