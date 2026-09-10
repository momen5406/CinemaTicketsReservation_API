from django.contrib import admin
from django.urls import path, include
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path("django/jsonresponsenomodel/", views.no_rest_no_model),
    #2
    path("django/jsonresponsefrommodel/", views.no_rest_from_model),
    #3.1
    path("rest/fbvlist/", views.fbv_list)
]
