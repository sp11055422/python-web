from django.urls import path
from .views import PollList, PollView, PollVote, PollCreate, PollEdit


urlpatterns = [
    path('', PollList.as_view(), name='poll_list'),
    path('list/', PollList.as_view(), name='poll_list'),
    path('add/', PollCreate.as_view(), name='poll_create'),
    path('<int:pk>/', PollView.as_view(), name='poll_view'),
    path('<int:pk>/edit/', PollEdit.as_view(), name='poll_edit'),
    path('<int:oid>/vote/', PollVote.as_view(), name='poll_vote'),
]
