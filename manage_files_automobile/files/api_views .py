from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import FileSerilizers
from .models import File


# class FileView(APIView):
#   parser_classes = (MultiPartParser, FormParser)

#   def post(self, request, *args, **kwargs):
#     file_serializer = FileSerilizers(data=request.data)
#     if file_serializer.is_valid():
#       file_serializer.save()
#       return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FileView(viewsets.ModelViewSet):
 
    queryset = File.objects.all()
    serializer_class = FileSerilizers
    parser_classes = [MultiPartParser, FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']








