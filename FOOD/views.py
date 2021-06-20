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
            res = {'msg':'data created !'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            Json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(Json_data, content_type='application/json')


def View_All(request):
    stu = Pizza.objects.all()
    serializer = PizzaSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT', 'PATCH', 'DELETE'])
def Crud(request, pk=None):
    if request.method == 'PUT':
        id = pk
        stu = Pizza.objects.get(pk = id)
        # pythondata = JSONParser().parse(stream)
        serializer = PizzaSerializer(stu, partial=True) #For_partial_update(Not_Required All fields)
        # serializer = PizzaSerializer(stu, data = pythondata, partial=True) #For_complete_update(Required All fields)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated !!'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    if request.method == 'PATCH':
        id = pk
        stu = Pizza.objects.get(pk = id)
        # serializer = PizzaSerializer(stu, data = pythondata, partial=True) #For_partial_update(Not_Required All fields)
        serializer = PizzaSerializer(stu, partial=True) #For_complete_update(Required All fields)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated !!'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    if request.method == 'DELETE':
        id = pk
        stu = Pizza.objects.get(pk=id)
        if id is not None:
            stu.delete()
            return Response({'msg' : 'Data deleted'}, status=status.HTTP_302_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)