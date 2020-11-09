from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
def articles_list(request):
    articles = models.Article.objects.all().order_by('date')

    args = {'articles':articles}
    return render(request, 'articles/articleslist.html',args)

class ListCourse(APIView):
    def get(self, request, format=None):
        Courses = models.Article.objects.all()
        serializer = serializers.CourseSerializer(Courses, many=True)
        return Response(serializers.data)
