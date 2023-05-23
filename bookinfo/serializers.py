from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    publish_date = serializers.DateField()
    page_number = serializers.IntegerField()
    stock = serializers.IntegerField()

    