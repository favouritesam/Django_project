from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
# from rest_framework import status
from rest_framework.decorators import api_view
# from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, ReviewModel
from .serializers import AuthorSerializer, BooKSerializer, ReviewSerializer


# from .models import Author
#
# users = [
#     {"name": "sheriff"},
#     {"name": "Ned"},
#     {"name": "sher"},
# ]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooKSerializer

    # def get_serializer_class(self):
    #     return {'request': self.request}


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return ReviewModel.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_id': self.kwargs['book_pk']}

    # def get(self, request):
    #     queryset = Book.objects.select_related('author').all()
    #     serializer = BooKSerializer(queryset, many=True, content={'request'})
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def post(self, request):
    #     class BookDetails(APIView):
    #         def get(self, request, pk):
    #             book = get_object_or_404(Book, pk=pk)
    #             serializer = BooKSerializer(book, context={'request': request})
    #             return Response(serializer.data, status=status.HTTP_200_OK)

    #
    # def put(self, request, pk):
    #             book = get_object_or_404(Book, pk=pk)
    #             serializer = CreateBooKSerializer(book, data=request.data)
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def delete(self, request, pk):
    #
    #
    #             book = get_object_or_404(Book, pk=pk)
    #             book.delete()
    #             return Response(status=status.HTTP_204_NO_CONTENT)
#
# class AuthorList(APIView):
#      def get(self, request):
#                  queryset = Author.objects.select_related('author').all()
#                  serializer = AuthorSerializer(queryset, many=True, context={'request'})
#                  return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)


# # Create your views here.
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.select_related('author').all()
#         serializer = BooKSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateBooKSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BooKSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = CreateBooKSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         query_set = Author.objects.all()
#         serializer = AuthorSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         serializer = CreateAuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     if request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
