from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from . models import Person
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializer import PesronModelSerializer
import json
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework import status

# Create your views here.



# /////// FUNCTION VIEWS //////

@api_view(['GET'])
def Personview(request):
    if request.method == 'GET':
        data = Person.objects.all()
        serializer=PesronModelSerializer(data,many=True)
        return Response(serializer.data)
    


# ///////// class based view ///////////

class PersonClassview(APIView):

    def get(self,request):

        data=Person.objects.all()

        serializer=PesronModelSerializer(data,many=True)

        return Response(serializer.data)
    


# /////////// modelviewset ////////////


class PersonModelViewset(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class=PesronModelSerializer





# ////////////////////// viewssets.viewsets /////////


class PersonViewsets(viewsets.ViewSet):

    def list(self,request):
        data = Person.objects.all()

        serializer=PesronModelSerializer(data,many=True)

        return Response(serializer.data)
    
    def create(self,req):

        data =req.data
        serializer=PesronModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:

            return Response('not added',status=status.HTTP_404_NOT_FOUND)
        
    def update(self,req,pk= None):
            data=Person.objects.get(id=pk)

            if data:
                serializer=PesronModelSerializer(data=req.data)
                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data,status=status.HTTP_200_OK)

        

# /////genericviews//////////


class PersonConcreteGenricView(ListCreateAPIView):

    queryset = Person.objects.all()
    serializer_class = PesronModelSerializer




