from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, ReviewDetailView, ReviewCreateView, ReviewpostUpdateView, ReviewpostDeleteView
from . import views 

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('review/new/', ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update/', ReviewpostUpdateView.as_view(), name='reviewpost-update'),
    path('review/<int:pk>/delete/', ReviewpostDeleteView.as_view(), name='reviewpost-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('review/<int:pk>/comment/', views.add_comment_to_reviewpost, name='add_comment_to_reviewpost'),
    path('reviewcomment/<int:pk>/approve/', views.reviewcomment_approve, name='reviewcomment_approve'),
    path('reviewcomment/<int:pk>/remove/', views.reviewcomment_remove, name='reviewcomment_remove'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('about/', views.about, name='blog-about'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/', views.review, name='review'),
    path('search', views.search, name='search'),
    path('southsearch', views.searchsouthfood, name='searchsouthfood'),
    path('northsearch', views.searchnorthfood, name='searchnorthfood'),
    path('noodlesearch', views.searchnoodlefood, name='searchnoodlefood'),
    path('japansearch', views.searchjapanfood, name='searchjapanfood'),
    path('chinesesearch', views.searchchinesefood, name='searchchinesefood'),
    path('buffetsearch', views.searchbuffetfood, name='searchbuffetfood'),
    path('fastfoodsearch', views.searchfastfood, name='searchfastfood'),
    path('thaifoodsearch', views.searchthaifood, name='searchthaifood'),
    path('somtumsearch', views.searchsomtumfood, name='searchsomtumfood'),
    path('cafesearch', views.searchcafefood, name='searchcafefood'),
]


