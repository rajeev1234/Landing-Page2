from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import PlatformWorks
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for PlatformWorks Application

class PlatformWorksTest(TestCase):

########################## Model Testing ############################


    # PlatformWorks object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.PlatformWorks =  PlatformWorks.objects.create(

        # Fields according to defined in Model
        PlatformWorks_Client_Name = 'PlatformWorks_Client_Name',
        PlatformWorks_Project_Name='PlatformWorks_Project_Name',
        PlatformWorks_Project_Details='PlatformWorks_Project_Details',
        PlatformWorks_Author=self.user,        # Defined above in get_user_model
        PlatformWorks_Created_Date = timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to PlatformWorks details
        self.assertEquals(self.PlatformWorks.get_absolute_url(), '/platform_works/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of PlatformWorks object created by create object query set
    def test_PlatformWorks_content(self):
        # Verify for each field
        self.assertEqual(f'{self.PlatformWorks.PlatformWorks_Client_Name}', 'PlatformWorks_Client_Name')
        self.assertEqual(f'{self.PlatformWorks.PlatformWorks_Project_Name}', 'PlatformWorks_Project_Name')
        self.assertEqual(f'{self.PlatformWorks.PlatformWorks_Project_Details}', 'PlatformWorks_Project_Details')
        self.assertEqual(f'{self.PlatformWorks.PlatformWorks_Author}', self.user.username)   # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test PlatformWorks List View

    def test_PlatformWorksList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('platform_works_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/PlatformWorks
        self.assertTemplateUsed(response, 'platform_works/platform_works_list.html')

#--------------------------------------------------------------------------------------------#

    # Test PlatformWorks Detail View

    def test_PlatformWorksDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PlatformWorks_pk = PlatformWorks.objects.get(PlatformWorks_Project_Name = 'PlatformWorks_Project_Name').pk

        # Get response
        response = self.client.get(reverse_lazy('platform_works_details',kwargs={'pk':PlatformWorks_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('platform_works_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'PlatformWorks_Project_Name')

        # Check for Correct template used in template/PlatformWorks
        self.assertTemplateUsed(response, 'platform_works/platform_works_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_PlatformWorksCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/platform_works/new/', {
        'PlatformWorks_Client_Name' : 'PlatformWorks_Client_Name',
        'PlatformWorks_Project_Name':'PlatformWorks_Project_Name',
        'PlatformWorks_Project_Details':'PlatformWorks_Project_Details',
        'PlatformWorks_Author' : self.user,        # Defined above in get_user_model
        'PlatformWorks_Created_Date' : timezone.now(),
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'PlatformWorks_Client_Name')
        self.assertContains(response, 'PlatformWorks_Project_Name')
        self.assertContains(response, 'PlatformWorks_Project_Details')
        self.assertContains(response, self.user.username)     # Same as defined in SetUp


        # Check for correct template used in template/PlatformWorks
        self.assertTemplateUsed(response, 'platform_works/platform_works_detail.html')

#---------------------------------------------------------------------------------------#


    # Test PlatformWorks Update view

    def test_PlatformWorksupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PlatformWorks_pk = PlatformWorks.objects.get(PlatformWorks_Project_Name='PlatformWorks_Project_Name').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('platform_works_details',kwargs={'pk':PlatformWorks_pk}), {
        'PlatformWorks_Client_Name' : 'PlatformWorks_Client_Name',
        'PlatformWorks_Project_Name':'PlatformWorks_Project_Name',
        'PlatformWorks_Project_Details':'PlatformWorks_Project_Details',
        'PlatformWorks_Author' : self.user,        # Defined above in get_user_model
        'PlatformWorks_Created_Date' : timezone.now(),
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'platform_works/platform_works_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_PlatformWorksdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PlatformWorks_pk = PlatformWorks.objects.get(PlatformWorks_Project_Name='PlatformWorks_Project_Name').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('platform_works_delete',kwargs={'pk':PlatformWorks_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('platform_works_delete',kwargs={'pk':PlatformWorks_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'platform_works/platform_works_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
