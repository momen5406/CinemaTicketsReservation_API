from django.contrib import admin
from django.urls import path, include
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path("django/jsonresponsenomodel/", views.no_rest_no_model),
    #2
    path("django/jsonresponsefrommodel/", views.no_rest_from_model),
    #3.1 GET POST
    path("rest/fbvlist/", views.fbv_list),
    #3.2 GET PUT DELETE
    path("rest/fbvlist/<int:pk>", views.fbv_pk),
    #4.1 GET POST (CBV)
    path("rest/cbv/", views.CBV_List.as_view()),
    #4.2 GET PUT DELETE (CBV)
    path("rest/cbv/<int:pk>", views.CBV_pk.as_view())
]
