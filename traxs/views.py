from .models import Trax
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TraxSerializer


class TraxViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Trax.objects.all()
    # The serializer class for serializing output
    serializer_class = TraxSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]