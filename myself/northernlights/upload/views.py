from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route, list_route
import os
from rest_framework.response import Response
# Create your views here.
from .models import Image
from .serializer import ImageSerializer

UPLOAD_DIR = 'static/upload_photo/'

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request):
        file = request.FILES['file']
        path = os.path.join(UPLOAD_DIR, file.name)
        destination = open(path, 'wb')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()

        if not os.path.exists(path):
            print('File not found:', path)
            return create_render(request)

        image, created = Image.objects.get_or_create(filepath=path)
        if created:
            image.title = request.POST['title']
            image.body = request.POST['body']
            image.created_at = request.POST['created_at']
            image.updated_at = request.POST['updates_at']
            image.lat = float(request.POST['lat'])
            image.lng = float(request.POST['lng'])
            image.status = request.POST['status']
            image.save()

        return Response({'message': 'OK'})