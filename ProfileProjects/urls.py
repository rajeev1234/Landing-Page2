
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of ProfileProjects : ProfileProjects_list

    path('', views.ProfileProjectsListView.as_view(), name='ProfileProjects_list'),

    # Path to create new ProfileProjects : ProfileProjects_new

    path('new/', views.ProfileProjectsCreateView.as_view(), name='ProfileProjects_new'),

    # Path to edit ProfileProjects : edit_list

    path('<int:pk>/edit', views.ProfileProjectsUpdateView.as_view(), name='ProfileProjects_update'),

    # Path to delete ProfileProjects : ProfileProjects_delete

    path('<int:pk>/delete', views.ProfileProjectsDeleteView.as_view(), name='ProfileProjects_delete'),

    # Path to detail view of ProfileProjects : ProfileProjects_details

    path('<int:pk>', views.ProfileProjectsDetailView.as_view(), name='ProfileProjects_details')
]
