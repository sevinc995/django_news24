from rest_framework.response import Response 
from rest_framework.views import APIView
from .models import NewsCore
from .serializers import NewsCoreSerializer


class NewsCoreList(APIView):
    def get(self, request):
        queryset = NewsCore.objects.all()
        serializer = NewsCoreSerializer(queryset, many=True)
        return Response({'news': serializer.data})


