from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
  
from .models import User
from .serializers import UserSerializer, UserSerializerUpdate
  
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from rest_framework.pagination import PageNumberPagination

from rest_framework import pagination

@api_view(['GET',])

# @permission_classes([AllowAny,])

def list_view(request):

    paginator = PageNumberPagination()
    paginator.page_size = 5
    person_objects = User.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET','POST'])
def user_create(request):
    # paginator = PageNumberPagination()
    # paginator.page_size = 2
    
    if request.method == 'GET':
        # paginator = PageNumberPagination()
        # paginator.page_size = 5
        user = User.objects.all()
        # result_page = paginator.paginate_queryset(user, request)
        serializer = UserSerializer(user, many=True)
        
        return Response(serializer.data)
  
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail(request, id=None):
    # pagination_class = StandardResultsSetPagination
    # user_id = request.user.id
    # print(user_id.id)
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = UserSerializerUpdate(user)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = UserSerializerUpdate(user, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)