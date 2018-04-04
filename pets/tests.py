from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Pets
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for Pets Application

class PetsTest(TestCase):

########################## Model Testing ############################


    # Pets object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Pets =  Pets.objects.create(

        # Fields according to defined in Model
        Pets_Age = 1,
        Pets_Animal_Type='Pets_Animal_Type',
        Pets_Breed='Pets_Breed',
        Pets_Daily_Charges=1,
        Pets_Description = 'Pets_Description',
        Pets_Ownership_Status = 'True',
        Pets_Weekly_Charges = 1,
        Pets_Author = self.user,       # Defined above in get_user_model
        Pets_Created_Date = timezone.now(),

        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Pets details
        self.assertEquals(self.Pets.get_absolute_url(), '/pets/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of Pets object created by create object query set
    def test_Pets_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Pets.Pets_Age}', '1')
        self.assertEqual(f'{self.Pets.Pets_Animal_Type}', 'Pets_Animal_Type')
        self.assertEqual(f'{self.Pets.Pets_Breed}', 'Pets_Breed')
        self.assertEqual(f'{self.Pets.Pets_Daily_Charges}', '1')
        self.assertEqual(f'{self.Pets.Pets_Description}', 'Pets_Description')
        self.assertEqual(f'{self.Pets.Pets_Ownership_Status}', 'True')
        self.assertEqual(f'{self.Pets.Pets_Weekly_Charges}', '1')
        self.assertEqual(f'{self.Pets.Pets_Author}', self.user.username)      # Defined in SetUp



#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test Pets List View

    def test_PetsList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('pets_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/Pets
        self.assertTemplateUsed(response, 'pets/pets_list.html')

#--------------------------------------------------------------------------------------------#

    # Test Pets Detail View

    def test_PetsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Pets_pk = Pets.objects.get(Pets_Animal_Type = 'Pets_Animal_Type').pk

        # Get response
        response = self.client.get(reverse_lazy('pets_details',kwargs={'pk':Pets_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('pets_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Pets_Age')

        # Check for Correct template used in template/Pets
        self.assertTemplateUsed(response, 'pets/pets_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test Pets Create View

    def test_PetsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/pets/new/', {
        'Pets_Age' : 1,
        'Pets_Animal_Type':'Pets_Animal_Type',
        'Pets_Breed':'Pets_Breed',
        'Pets_Daily_Charges':1,
        'Pets_Description' : 'Pets_Description',
        'Pets_Ownership_Status' : True,
        'Pets_Weekly_Charges' : 1,
        'Pets_Author' : self.user,       # Defined above in get_user_model
        'Pets_Created_Date' : timezone.now(),
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, '1')
        self.assertContains(response, 'Pets_Animal_Type')
        self.assertContains(response, 'Pets_Breed')
        self.assertContains(response, '1')
        self.assertContains(response, 'Pets_Description')
        self.assertContains(response, 'True')
        self.assertContains(response, '1')
        self.assertContains(response, self.user.username)      # Same as defined in SetUp


        # Check for correct template used in template/pets
        self.assertTemplateUsed(response, 'pets/pets_detail.html')

#---------------------------------------------------------------------------------------#


    # Test pets Update view

    def test_Petsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Pets_pk = Pets.objects.get(Pets_Animal_Type='Pets_Animal_Type').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('pets_details',kwargs={'pk':Pets_pk}), {
        'Pets_Age' : 1,
        'Pets_Animal_Type':'Pets_Animal_Type',
        'Pets_Breed':'Pets_Breed',
        'Pets_Daily_Charges':1,
        'Pets_Description' : 'Pets_Description',
        'Pets_Ownership_Status' : True,
        'Pets_Weekly_Charges' : 1,
        'Pets_Author' : self.user,       # Defined above in get_user_model
        'Pets_Created_Date' : timezone.now(),
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'pets/pets_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of pets views

    def test_Petsdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Pets_pk = Pets.objects.get(Pets_Animal_Type='Pets_Animal_Type').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('pets_delete',kwargs={'pk':Pets_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('pets_delete',kwargs={'pk':Pets_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Pets_delete',kwargs={'pk':Pets_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'pets/pets_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
