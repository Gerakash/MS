from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsSuperuserOrReadOnly

from .serializers import *
# Create your views here.

class DocumentView(views.APIView):
    permission_classes = [IsSuperuserOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            group = request.user.groups.all()[0].name.lower()
        except IndexError:
            return Response("Please authorize!")
        if group == 'general':
            docs = Document.objects.all()
        elif group == 'gef':
            docs = Document.objects.filter(status='active', secret_level='private')
        elif group in ['sergeant', 'leit', 'captain']:
            docs = Document.objects.filter(status='active', secret_level__in=['public', 'private', 'secret'])
        elif group in ['major', 'podpol', 'polkovnik']:
            docs = Document.objects.filter(status='active',
                                           secret_level__in=['public', 'private', 'secret', 'top-secret'])
        elif group == 'cleaner':
            docs = Document.objects.filter(status='active')
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)



    def post(self,request,*args,**kwargs):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":"Document created successfully!"})