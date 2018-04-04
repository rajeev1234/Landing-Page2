from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import PoliceStation
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for PoliceStation Application

class PoliceStationTest(TestCase):

########################## Model Testing ############################


    # PoliceStation object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.PoliceStation =  PoliceStation.objects.create(

        # Fields according to defined in Model
        PoliceStation_Area_Police_Station = 'PoliceStation_Area_Police_Station',
        PoliceStation_DCP='PoliceStation_DCP',
        PoliceStation_Station_Name='PoliceStation_Station_Name',
        PoliceStation_Author=self.user,       # Defined above in get_user_model
        PoliceStation_Created_Date = timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to PoliceStation details
        self.assertEquals(self.PoliceStation.get_absolute_url(), '/police_station/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of PoliceStation object created by create object query set
    def test_PoliceStation_content(self):
        # Verify for each field
        self.assertEqual(f'{self.PoliceStation.PoliceStation_Area_Police_Station}', 'PoliceStation_Area_Police_Station')
        self.assertEqual(f'{self.PoliceStation.PoliceStation_DCP}', 'PoliceStation_DCP')
        self.assertEqual(f'{self.PoliceStation.PoliceStation_Station_Name}', 'PoliceStation_Station_Name')
        self.assertEqual(f'{self.PoliceStation.PoliceStation_Author}', self.user.username)   # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test PoliceStation List View

    def test_PoliceStationList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('police_station_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/PoliceStation
        self.assertTemplateUsed(response, 'police_station/police_station_list.html')

#--------------------------------------------------------------------------------------------#

    # Test PoliceStation Detail View

    def test_PoliceStationDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PoliceStation_pk = PoliceStation.objects.get(PoliceStation_Station_Name = 'PoliceStation_Station_Name').pk

        # Get response
        response = self.client.get(reverse_lazy('police_station_details',kwargs={'pk':PoliceStation_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('police_station_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'PoliceStation_Station_Name')

        # Check for Correct template used in template/PoliceStation
        self.assertTemplateUsed(response, 'police_station/police_station_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_PoliceStationCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/police_station/new/', {
        'PoliceStation_Area_Police_Station' : 'PoliceStation_Area_Police_Station',
        'PoliceStation_DCP':'PoliceStation_DCP',
        'PoliceStation_Station_Name':'PoliceStation_Station_Name',
        'PoliceStation_Author':self.user,       # Defined above in get_user_model
        'PoliceStation_Created_Date' : timezone.now(),
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'PoliceStation_Area_Police_Station')
        self.assertContains(response, 'PoliceStation_DCP')
        self.assertContains(response, 'PoliceStation_Station_Name')
        self.assertContains(response, self.user.username)     # Same as defined in SetUp


        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'police_station/police_station_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_PoliceStationupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PoliceStation_pk = PoliceStation.objects.get(PoliceStation_Station_Name='PoliceStation_Station_Name').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('police_station_details',kwargs={'pk':PoliceStation_pk}), {
        'PoliceStation_Area_Police_Station' : 'PoliceStation_Area_Police_Station',
        'PoliceStation_DCP':'PoliceStation_DCP',
        'PoliceStation_Station_Name':'PoliceStation_Station_Name',
        'PoliceStation_Author':self.user,       # Defined above in get_user_model
        'PoliceStation_Created_Date' : timezone.now(),
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'police_station/police_station_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_PoliceStationdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PoliceStation_pk = PoliceStation.objects.get(PoliceStation_Station_Name='PoliceStation_Station_Name').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('police_station_delete',kwargs={'pk':PoliceStation_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('police_station_delete',kwargs={'pk':PoliceStation_pk}))

        # self.assertRedirects(post_response, reverse_lazy('police_station_delete',kwargs={'pk':PoliceStation_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'police_station/police_station_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
