from rest_framework.viewsets import ModelViewSet


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    