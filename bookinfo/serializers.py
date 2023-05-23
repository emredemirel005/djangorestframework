from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    publish_date = serializers.DateField()
    page_number = serializers.IntegerField()
    stock = serializers.IntegerField()

    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        return Books.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.author = validated_data.get('author',instance.author)
        instance.publish_date = validated_data.get('publish_date',instance.publish_date)
        instance.page_number = validated_data.get('page_number',instance.page_number)
        instance.stock = validated_data.get('stock',instance.stock)
        instance.save()
        return instance