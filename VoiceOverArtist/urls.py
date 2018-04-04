
from django.urls import path

from . import views


urlpatterns = [

    # Path to list view of VoiceOverArtist : VoiceOverArtist_list

    path('', views.VoiceOverArtistListView.as_view(), name='VoiceOverArtist_list'),

    # Path to create new VoiceOverArtist : VoiceOverArtist_new

    path('new/', views.VoiceOverArtistCreateView.as_view(), name='VoiceOverArtist_new'),

    # Path to edit VoiceOverArtist : edit_list

    path('<int:pk>/edit', views.VoiceOverArtistUpdateView.as_view(), name='VoiceOverArtist_update'),

    # Path to delete VoiceOverArtist : VoiceOverArtist_delete

    path('<int:pk>/delete', views.VoiceOverArtistDeleteView.as_view(), name='VoiceOverArtist_delete'),

    # Path to detail view of VoiceOverArtist : VoiceOverArtist_details

    path('<int:pk>', views.VoiceOverArtistDetailView.as_view(), name='VoiceOverArtist_details')
]
