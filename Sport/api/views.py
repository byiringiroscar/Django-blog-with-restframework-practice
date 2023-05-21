from abc import ABC

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .permissions import IsOwnerOrReadOnly

from Sport.models import Statistic, Comment
from Sport.api.serializers import StatisticSerializer, CommentSerializer
from rest_framework import generics, permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import filters
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission


class StatisticList(generics.ListCreateAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'name', 'position']
    ordering_fields = ['id', 'name', 'position']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(posted=self.request.user)


class StatisticRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = str(user.username)

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# @api_view(['GET'])
# def api_detail_view(request, id):
#     try:
#         stati = Statistic.objects.get(id=id)
#
#     except Statistic.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = StatisticSerializer(stati, many=False)
#         return Response(serializer.data)
#
#
# @api_view(['PUT'])
# def api_put_view(request, id):
#     try:
#         stati = Statistic.objects.get(id=id)
#
#     except Statistic.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         serializer = StatisticSerializer(stati, data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = "update successful"
#             return Response(data=data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['DELETE'])
# def api_delete_view(request, id):
#     try:
#         stati = Statistic.objects.get(id=id)
#
#     except Statistic.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#         operatiom = stati.delete()
#         data = {}
#         if operatiom:
#             data["success"] = "update successful"
#         else:
#             data["failure"] = "delete failed"
#
#         return Response(data=data)
#
#
# @api_view(['POST'])
# def api_create_view(request):
#     serializer = StatisticSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class DemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'success': "successfully done it"})
