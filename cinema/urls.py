from django.urls import path, include

from rest_framework import routers

from cinema.views import (GenreViewList,
                          GenreViewDetail,
                          ActorViewList,
                          ActorViewDetail,
                          CinemaHallViewSet,
                          MovieViewSet)


cinema_hall_list = CinemaHallViewSet.as_view(actions={"get": "list",
                                                      "post": "create"})

cinema_hall_detail = (CinemaHallViewSet.as_view
                      (actions={"get": "retrieve",
                                "put": "update",
                                "patch": "partial_update",
                                "delete": "destroy"}))

router = routers.DefaultRouter()

router.register("movie", MovieViewSet, basename="movie")

# use /movie/ for get or post amd use  /movie/pk/ for delete, update etc...

urlpatterns = [
    path("genres/", GenreViewList.as_view(),
         name="genres-list"),
    path("genres/<int:pk>/", GenreViewDetail.as_view(),
         name="genres-detail"),
    path("actors/", ActorViewList.as_view(),
         name="actors-list"),
    path("actors/<int:pk>/", ActorViewDetail.as_view(),
         name="actor-detail"),
    path("cinema-halls/", cinema_hall_list,
         name="cinema-halls-list"),
    path("cinema-halls/<int:pk>/", cinema_hall_detail,
         name="cinema-hall-detail"),
    path("", include(router.urls)),

]

app_name = "cinema"
