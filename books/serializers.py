from rest_framework import serializers
from .models import Book, Author, ReviewModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class BooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'copies', 'author']

        author = AuthorSerializer

    # name_of_book =serializers.CharField(source='title')

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name="author-detail"
    # )


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email']


class CreateBooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'copies', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['id', 'reviewer_name', 'description']

    def create(self, validated_data):
        return ReviewModel.objects.create(book_id=self.context['book_id'], **validated_data)

    # name_of_book =serializers.CharField(source='title')

# class BookSerializer (serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     isbn = serializers.CharField(max_length=13)
#     genre = serializers.CharField(max_length=8)


# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=150)
#     last_name = serializers.CharField(max_length=150)
#     email = serializers.EmailField
