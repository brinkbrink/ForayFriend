from django.test import TestCase
from django.contrib.auth.models import User
from .models import Season, ForageType, Foraged, Foray, Resource
import datetime
from .forms import ForagedForm
from django.urls import reverse_lazy, reverse

# Create your tests here.

class ForagedTest(TestCase):
    def setUp(self):
        self.typename=ForageType(typename='edible')
        self.season=Season(season='spring')
        self.user=User(username='yada')
        self.foraged=Foraged(name='Claytonia lanceolata', amountfound=3, location='Cascades', datefound=datetime.date(2022,1,1),dateentered=datetime.date(2022,1,1),)

    def test_titlestring(self):
        self.assertEqual(str(self.foraged), 'Claytonia lanceolata')

    def test_tablename(self):
        self.assertEqual(str(Foraged._meta.db_table), 'foraged')

    def test_possiblePrice(self):
        poss=self.foraged.amountfound * 15.50
        self.assertEqual(self.foraged.possiblePrice(),poss)

class SeasonTest(TestCase):
    def setUp(self):
        self.season=Season(season='summer')

    def test_titlestring(self):
        self.assertEqual(str(self.season), 'summer')

    def test_tablename(self):
        self.assertEqual(str(Season._meta.db_table), 'seasons')

class ForageTypeTest(TestCase):
    def setUp(self):
        self.typename=ForageType(typename='edible')

    def test_titlestring(self):
        self.assertEqual(str(self.typename), 'edible')

    def test_tablename(self):
        self.assertEqual(str(ForageType._meta.db_table), 'foragetypes')


class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(name='A Resource')
    
    def test_namestring(self):
        self.assertEqual(str(self.name), 'A Resource')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resources')

class ForayTest(TestCase):
    def setUp(self):
        self.name=Foray(name='Burn Morels Burn')

    def test_evtitlestring(self):
        self.assertEqual(str(self.name), 'Burn Morels Burn')

    def test_tablename(self):
        self.assertEqual(str(Foray._meta.db_table), 'forays')

class NewForagedForm(TestCase):
    #valid form data
    def test_foragedform(self):
        data={            
            'name':'rubus',
            'foragetype' : 'edible',
            'season' : 'summer',
            'datefound':'2022-03-02', 
            'dateentered':'2022-03-02', 
            'location':'cascades', 
            'user' : 'brink'}
        form=ForagedForm(data)
        self.assertTrue(form.is_valid)

class New_Foraged_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='p@ssw0rd1')
        self.season=Season.objects.create(season='summer')
        self.type=ForageType.objects.create(typename='edible')
        self.foraged=Foraged.objects.create(name='Claytonia lanceolata', foragetype=self.type, season=self.season, amountfound=3, location='Cascades', datefound=datetime.date(2022,1,1),dateentered=datetime.date(2022,1,1), user=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newforaged'))
        self.assertRedirects(response, '/accounts/login/?next=/friend/newforaged/')