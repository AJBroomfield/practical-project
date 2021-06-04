from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestClass(TestBase):
    def test_get_race(self):
        race=['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half-Elf','Half-Orc','Teifling']
        for _ in range (20):
            response = self.client.get(url_for('get_race'))
            self.assertIn(response.data.decode('utf-8'),race)
            self.assertEqual(response.status_code,200)