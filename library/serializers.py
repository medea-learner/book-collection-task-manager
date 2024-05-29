from django.core.exceptions import ValidationError
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    def validate(self, attrs):
        data = attrs["isbn"]
        isbn_len =  len(data)
        if 10 > isbn_len or isbn_len > 13:
            raise ValidationError("ISBN should be between 10 and 13")
        return attrs

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'isbn']
