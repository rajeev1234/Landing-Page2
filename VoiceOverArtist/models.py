from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your VoiceOverArtists here.
class VoiceOverArtist(models.Model):
    VoiceOverArtist_Charges_Available=models.BooleanField()
    VoiceOverArtist_Daily_charges = models.IntegerField(default=0)
    VoiceOverArtist_Description = models.CharField(max_length=200)
    VoiceOverArtist_Language = models.CharField(max_length=200)
    # VoiceOverArtist_Portfolio= models.ForeignKey(portfolio_element,related_name='VoiceOverArtist',on_delete=models.CASCADE)
    # VoiceOverArtist_Ratings = models.ForeignKey(Rating,related_name='VoiceOverArtist',on_delete=models.CASCADE)
    # VoiceOverArtist_Video = models.ForeignKey(video,related_name='VoiceOverArtist',on_delete=models.CASCADE)
    VoiceOverArtist_Voice_Scale = models.CharField(max_length=200)
    VoiceOverArtist_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='VoiceOverArtist', on_delete=models.CASCADE)
    VoiceOverArtist_Created_Date = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('VoiceOverArtist_details', args=[str(self.id)])


# Create VoiceOverArtists Comments here.


class Comment(models.Model):

    VoiceOverArtist_Comment = models.CharField(max_length=150, null=False)
    Comment_VoiceOverArtist = models.ForeignKey(VoiceOverArtist,related_name="VoiceOverArtist", null=False, on_delete=models.CASCADE)
    VoiceOverArtist_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="VoiceOverArtist_Comment", on_delete=models.CASCADE)

    # VoiceOverArtist_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.VoiceOverArtist_Comment

    def get_absolute_url(self):
        return reverse('VoiceOverArtist_list')










