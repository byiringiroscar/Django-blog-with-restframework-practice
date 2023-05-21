from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Sport.new_api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from Sport.models import Statistic
from Sport.new_api.serializers import StatisticSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from Sport.new_api.serializers import AccountPropertiesSerializer


@api_view(['GET', ])
# @permission_classes((IsAuthenticated,))
def api_detail_blog_view(request, pk):
    try:
        stat = Statistic.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StatisticSerializer(stat)
        return Response(serializer.data)


@api_view(['GET', ])
def api_detail_view(request):
    try:
        stat = Statistic.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StatisticSerializer(stat, many=True)
        return Response(serializer.data)


@api_view(['POST', ])
# @permission_classes([IsAuthenticated])
def registration_view_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user. "
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['data'] = token
            return Response(data, status=status.HTTP_201_CREATED)


        else:

            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_blog(request, pk):
    try:
        stat = Statistic.objects.get(id=pk)

        if Statistic.objects.filter(posted=request.user, id=pk):

            if request.method == "PUT":
                serializer = StatisticSerializer(stat, data=request.data)
                data = {}
                if serializer.is_valid():
                    serializer.save()
                    data["success"] = "update succesfully"
                    return Response(data=data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'response': "you don't have permission to edit"})
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def api_delete_blog(request, pk):
    try:
        stat = Statistic.objects.get(id=pk)
        if Statistic.objects.filter(posted=request.user, id=pk):

            if request.method == 'DELETE':
                operation = stat.delete()
                data = {}
                if operation:
                    data["success"] = "delete successfuly"
                else:
                    data["failure"] = "delete failed"
                return Response(data=data)
            return Response("method not allowed")
        else:
            return Response("user not match")





    except Statistic.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def api_create_blog(request):
    user = request.user
    stat = Statistic(posted=user)
    if request.method == 'POST':
        serializer = StatisticSerializer(stat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiStatListView(ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'position', 'posted__username')  # posted__username will help us to search username for
    # one who posted


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def registration_view(request):
    try:
        account = request.user
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_view(request):
    try:
        account = request.user
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = AccountPropertiesSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'response': ['data update succesfully']}
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
