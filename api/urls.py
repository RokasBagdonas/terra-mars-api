from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)

urlpatterns = [path("", include(router.urls))]
