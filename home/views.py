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

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Personview(request):

    #---------  GET METHOD----------

    if request.method == 'GET':
        data = Person.objects.all()
        serializer=PesronModelSerializer(data,many=True)
        return Response(serializer.data)
    
    
    # ----------  POST METHOD-----------

    if request.method == 'POST':
        serializer=PesronModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('added')
        return Response('not added')
    

    # ---------- PUT METHOD -------------
        
    if request.method == 'PUT':
        pk=request.data['id']
        obj=Person.objects.get(id=pk)
        print(request.data['id'])
        serializer=PesronModelSerializer(obj,data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated ...','data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # -------------- PATCH ------------------


    if request.method =='PATCH':
        pk=request.data['id']
        obj=Person.objects.get(id=pk)
        serializer=PesronModelSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data partial Updated ...','data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # ---------DELETE----------

    if request.method == 'DELETE':
        pk=request.data['id']
        obj=Person.objects.get(id=pk)
        obj.delete()
        return Response({'msg':'Data Deleted !!!'})
        
    
    


# ///////// class based view ///////////

class PersonClassview(APIView):

    def get(self,request):

        data=Person.objects.all()

        serializer=PesronModelSerializer(data,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer=PesronModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'DATA ADDED ....'})
        
    def put(self,request):
        pk =request.data['id']
        print(pk)
        obj=Person.objects.get(id=pk)
        serializer=PesronModelSerializer(obj,data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()

            return Response({"msg":"PUT UPDATE COMPLETED"})
        
    def patch(self,request):
        pk =request.data['id']
        obj=Person.objects.get(id=pk)
        serializer=PesronModelSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({"msg":"PATCH UPDATE COMPLETED"})
        
    def delete(seslf,request):
        pk=request.data['id']
        data=Person.objects.all(id=pk)
        data.delete()

        return Response({"msg":"data deleted !!!"})

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
    


    def retrive(self,req,pk=None):
        id=pk
        if pk is not None:
            data=Person.objects.get(id=pk)
            serializer=PesronModelSerializer(data,many=True)
            return Response(serializer.data)
    
    

    def create(self,req):
        data =req.data
        serializer=PesronModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response('not added',status=status.HTTP_404_NOT_FOUND)
        


    def update(self,req,pk= None):
            if pk is not None:
                obj=Person.objects.get(id=pk)
                serializer=PesronModelSerializer(obj,data=req.data,partial=False)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)


    def partial_update(self,request,pk=None):
        if pk is not None:
                obj=Person.objects.get(id=pk)
                serializer=PesronModelSerializer(obj,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
                
    def delete(self,request,pk=None):

        if pk is not None: 
            obj=Person.objects.get(id=pk)
            obj.delete()

            return Response('msg':'data deleted')
        

# /////genericviews//////////


class PersonConcreteGenricView(ListCreateAPIView):

    queryset = Person.objects.all()
    serializer_class = PesronModelSerializer




