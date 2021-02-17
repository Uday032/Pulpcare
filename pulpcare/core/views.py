from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response


from .models import Website
from .serializers import WebsiteSerializers
# Create your views here.

def mainpage(request,*args, **kwargs):
    return render(request,"index.html")

def websites(request,*args, **kwargs):
    queryset = Website.objects.all()
    serializer = WebsiteSerializers(queryset, many=True)
    content = {
        'data': serializer.data
    }
    return render(request,"websites.html", content)

def getwebsite(request,id, *args, **kwargs):
    queryset = Website.objects.get(pk=id)
    print(queryset.logo)
    # serializer = WebsiteSerializers(queryset, many=Flase)
    content = {
        'logo': queryset.logo,
        'tagline': queryset.tagline
    }
    return render(request,"createdwebsite.html", content)

class CreateWebsite(APIView):

    serializer_class = WebsiteSerializers

    def get(self, request, *args, **kwargs):
        queryset = Website.objects.all()
        serializer = WebsiteSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print(request.data)
        logo = request.data['logo']
        Website.objects.create(logo=logo, tagline= request.data['tagline'])
        return Response({'message': 'File created'}, status=status.HTTP_200_OK)