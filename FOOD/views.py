from typing import IO
from .models import Pizza
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import PizzaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

@csrf_exempt
def Add_new(request):
    if request.method == 'POST':
        Json_data = request.body
        stream = IO.BytesIO(Json_data)
        pythondata = JSONParser().parse(stream)
        serializer = PizzaSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created !!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def View_All(request):
    stu = Pizza.objects.all()
    serializer = PizzaSerializer(stu, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT', 'PATCH', 'DELETE'])
def Crud(request, pk=None):
    if request.method == 'PUT':
        id = pk
        stu = Pizza.objects.get(pk = id)
        serializer = PizzaSerializer(stu, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated !!'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        stu = Pizza.objects.get(pk = id)
        serializer = PizzaSerializer(stu, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated !!'}, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        stu = Pizza.objects.get(pk=id)
        if id is not None:
            stu.delete()
            return Response({'msg' : 'Data deleted'}, status=status.HTTP_400_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

#For Search data we gonnna use generic class
class Search_data(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['pizza_type', 'pizza_size']