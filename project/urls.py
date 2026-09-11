from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tickets import views

router = DefaultRouter()
router.register('guests', views.Viewset_guest)
router.register('movies', views.Viewset_movie)
router.register('reservations', views.Viewset_reservation)

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
    path("rest/cbv/<int:pk>", views.CBV_pk.as_view()),
    #5.1 GET POST (MIXINS)
    path("rest/mixins/", views.Mixins_list.as_view()),
    #5.2 GET PUT DELETE (MIXINS)
    path("rest/mixins/<int:pk>", views.Mixins_pk.as_view()),
    #6.1 GET POST (GENERICS)
    path("rest/generics/", views.Generics_list.as_view()),
    #6.2 GET PUT DELETE (GENERICS)
    path("rest/generics/<int:pk>", views.Generics_pk.as_view()),
    #7 Viewsets
    path("rest/viewset/", include(router.urls))
]
