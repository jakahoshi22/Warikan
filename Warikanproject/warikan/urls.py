from django.urls import path
from .views import MemberList, DetailList, AddMember, AddDetail, DetailUpdate, DetailDelete

urlpatterns = [
    path('memberlist/', MemberList.as_view(),name='memberlist'),
    path('detaillist/<int:pk>', DetailList.as_view(),name='detaillist'),
    path('addmember/', AddMember.as_view(),name='addmember'),
    path('adddetail/<int:pk>', AddDetail.as_view(),name='adddetail'),
    path('detailupdate/<int:pk>', DetailUpdate.as_view(),name='detailupdate'),
    path('detaildelete/<int:pk>', DetailDelete.as_view(),name='detaildelete'),   
]