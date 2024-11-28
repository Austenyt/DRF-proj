from rest_framework.routers import SimpleRouter

from dogs.apps import DogsConfig
from dogs.views import DogViewSet

app_name = DogsConfig.name

router = SimpleRouter()
router.register("", DogViewSet)

urlpatterns = []

urlpatterns += router.urls
