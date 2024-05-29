from rest_framework import generics

from .models import Book
from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer


class BookApi(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
