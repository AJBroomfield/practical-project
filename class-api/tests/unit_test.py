from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestClass(TestBase):
    def test_get_class(self):
        role=['Barbarian','Bard','Cleric','Driud','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
        for _ in range (20):
            response = self.client.get(url_for('get_class'))
            self.assertIn(response.data.decode('utf-8'),role)
            self.assertEqual(response.status_code,200)