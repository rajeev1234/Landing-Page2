
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of theater_actor : theater_actor_list

    path('', views.theater_actorListView.as_view(), name='theater_actor_list'),

    # Path to create new theater_actor : theater_actor_new

    path('new/', views.theater_actorCreateView.as_view(), name='theater_actor_new'),

    # Path to edit theater_actor : edit_list

    path('<int:pk>/edit', views.theater_actorUpdateView.as_view(), name='theater_actor_edit'),

    # Path to delete theater_actor : theater_actor_delete

    path('<int:pk>/delete', views.theater_actorDeleteView.as_view(), name='theater_actor_delete'),

    # Path to detail view of theater_actor : theater_actor_details

    path('<int:pk>', views.theater_actorDetailView.as_view(), name='theater_actor_details')
]
