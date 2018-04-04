"""workforfilms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #Basic
    path('', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('Dashboards.urls')),
    path('user/', include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
    #Ayushi
    path('actionvehicle/',include('actionvehicle.urls')),
    path('actors/',include('actors.urls')),
    path('amenity_adresses/',include('Amenity_Adresses.urls')),
    path('booking/',include('Booking.urls')),
    path('childartist/',include('ChildArtist.urls')),
    path('circleinvite/',include('CircleInvite.urls')),
    path('client/',include('Client.urls')),
    path('comments/',include('Comments.urls')),
    path('contactmessages/',include('ContactMessages.urls')),
    path('conversations/',include('conversations.urls')),
    path('userprofessionalinfo/',include('userprofessionalinfo.urls')),
    path('userdetails/',include('userdetails.urls')),
    #Sharique
    path('costumes/', include('Costumes.urls')),
    path('dancers/', include('Dancers.urls')),
    path('districts/',include('Districts.urls')),
    path('educationinfos/',include('EducationInfos.urls')),
    path('filmlocationscheduleforpermit/',include('FilmLocationScheduleForPermit.urls')),
    path('filmlocationfromguidedwithserial/',include('FilmLocationFromGuidedWithSerial.urls')),
    path('filmprojectforpermit/',include('FilmProjectForPermit.urls')),
    path('filmrecceroute/',include('FilmRecceRoute.urls')),
    path('filmreccetourguide/',include('FilmRecceTourGuide.urls')),
    path('servicecatagory/',include('ServiceCatagory.urls')),
    path('servicesubcatagory/',include('ServiceSubcatagory.urls')),
    path('singer/',include('Singer.urls')),
    path('specialart/',include('SpecialArt.urls')),
    path('states/',include('State.urls')),
    path('profileprojects/',include('ProfileProjects.urls')),
    path('subscriptionplan/',include('SubscriptionPlan.urls')),
    path('talentprofile/',include('TalentProfile.urls')),
    path('voiceoverartist/',include('VoiceOverArtist.urls')),
    path('usercoinbox/',include('UserCoinBox.urls')),
    #Shatish
    path('location_financial/', include('location_financials.urls')),
    path('posts/', include('posts.urls')),
    path('location_pitch/', include('location_pitch.urls')),
    path('location_psndc/', include('location_psndc.urls')),
    path('location_subcategory/', include('location_subcategory.urls')),
    path('messages/', include('message.urls')),
    path('mimicry_artist/', include('mimicry_artist.urls')),
    path('model/', include('model.urls')),
    path('musician/', include('musician.urls')),
    path('officer_contact/', include('officer_contact.urls')),
    path('permit_query/', include('permit_query.urls')),
    path('pets/', include('pets.urls')),
    path('police_station/', include('police_station.urls')),
    path('platform_works/', include('platform_works.urls')),
    path('portfolio_element/', include('portfolio_element.urls')),
    #Ashish
    path('help_center/', include('help_center.urls'),name = 'help_center'),
    path('help_category/', include('help_category.urls')),
    path('help_Qna/', include('help_Qna.urls')),
    path('help_subcategory/', include('help_subcategory.urls')),
    path('Letter_pdf/', include('Letter_pdf.urls')),
    path('Location/', include('Location.urls')),
    path('Location_Amenitie/', include('Location_Amenitie.urls')),
    path('Location_Authoritie/', include('Location_Authorities.urls')),
    path('Location_Category/', include('Location_Category.urls')),
    path('prop/', include('Prop.urls')),
    path('quick_requirments/', include('Quick_Requirements.urls')),
    path('rating/', include('Ratings.urls')),
    path('review/', include('Review.urls')),
    path('search/', include('Search.urls')),
]
