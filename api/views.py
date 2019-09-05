from whiskydatabase.models import WhiskyInfo, Distillery
from rest_framework import viewsets
from api.serializers import WhiskySerializer, DistillerySerializer


class WhiskyViewSet(viewsets.ModelViewSet):
    queryset = WhiskyInfo.objects.all()
    serializer_class = WhiskySerializer
    

class DistilleryViewSet(viewsets.ModelViewSet):
    queryset = Distillery.objects.all()
    serializer_class = DistillerySerializer