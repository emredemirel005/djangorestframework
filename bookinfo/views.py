from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from bookinfo.serializers import BooksSerializer
from bookinfo.models import Books

@api_view(['GET','POST'])
def books(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','DELETE','PUT'])
def book(request,id):
    try:
        book = Books.objects.get(pk=id)
    except Books.DoesNotExist:
        return Response({"error":"save does not found!"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BooksSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BooksSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

