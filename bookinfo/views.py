from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from bookinfo.serializers import BooksSerializer
from bookinfo.models import Books

@api_view(['GET'])
def book_list(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# class BookList(APIView):

#     def get(self,request):
#         book = Books.objects.all()
#         serializer = BooksSerializer(book,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         data = {
#             'author':request.data.get('author'),
#             'book_name':request.data.get('book_name'),
#         }
#         serializer = BooksSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
