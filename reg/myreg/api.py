from  myreg.models import Reg
from rest_framework import viewsets,permissions
from .serializers import RegSerializer
from .serializers import RegSerializer2

class RegViewSet(viewsets.ModelViewSet):
    queryset = Reg.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class= RegSerializer
    
class RegViewSet2(viewsets.ModelViewSet):
    queryset = Reg.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class= RegSerializer2    
    
    