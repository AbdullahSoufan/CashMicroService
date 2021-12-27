from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Cache
from . serializer import  bookSerializer2


class bookList2(APIView):
    def get(self,request,id):
        certain_book = Cache.objects.all().filter(bookid=id)
        serializer = bookSerializer2(certain_book, many=True)
        return Response(serializer.data)
    def put(self,request,id):
        certain_book = Cache.objects.all().filter(bookid=id)
        if certain_book:
            Cache.objects.filter(bookid=id).delete()
            return Response("SUCCESS Remove")
        return Response("No such book to remove")

    def post(self, request, id):
        b = Cache(bookid= id, title= request.data["title"] , quantity= request.data["quantity"] , price= request.data["price"] )
        b.save()
        return Response("SUCCESS SAVE")
