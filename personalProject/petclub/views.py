from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio


class PetAPIview(APIView):
    def get(self, request):
        return Response(data="I am in get", status=200)

    def patch(self, request):
        return Response(data="I am in patch", status=200)
    def delete(self, request):
        return Response(data="I am in delete", status=200)
    def post(self, request):
        return Response(data="I am in post", status=200)


class PersonAPIview(APIView):
    def get(self, request):
        return Response(data="I am in get", status=200)

    def patch(self, request):
        return Response(data="I am in patch", status=200)
    def delete(self, request):
        return Response(data="I am in delete", status=200)
    def post(self, request):
        return Response(data="I am in post", status=200)