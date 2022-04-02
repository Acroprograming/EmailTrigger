from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #for interview inclure interview urls
    path('interview/', include('interview.urls')),
    path('admin/', admin.site.urls),
]