from django.urls import path

from post.views import *

urlpatterns = [
    path('', post_index,name="post-index"),
    path('<int:post_id>/detail',post_detail,name="detail"),
    path("create/",post_create,name="create"),
    path("delete/",post_delete,name="delete"),
    path("update/",post_update,name="update"),
]
