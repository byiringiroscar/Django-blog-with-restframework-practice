from django.urls import path
from Sport.api.views import StatisticList, StatisticRetrieve, CommentList, CommentRetrieve, DemoView

name = 'Sport'

urlpatterns = [
    # path('<id>/', api_detail_view, name='detail'),
    # path('create', api_create_view, name='create')
    path('list/', StatisticList.as_view()),
    path('retrieve/<int:pk>/', StatisticRetrieve.as_view()),
    path('commentlist/', CommentList.as_view()),
    path('commentretrieve/<int:pk>/', CommentRetrieve.as_view()),
    path('demo', DemoView.as_view()),
]