from django.urls import path
from rest_framework.urlpatters import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    re_path('api/books/(?P<pk>[0-9]*)', views.BookApi.as_view(), name='books'),
])
