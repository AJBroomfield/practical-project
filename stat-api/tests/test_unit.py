from flask import url_for
from flask_testing import TestCase
from app import app, stat_roller
from unittest.mock import patch
import json

class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestStat(TestBase):
    def test_get_stat(self):
        with patch('app.stat_roller') as s:
            
            s.return_value = {"STR":20,"DEX":20,"CON":20,"INT":20,"WIS":20,"CHA":20}
            
            response = self.client.post(
                url_for('get_stats'), 
                json={"role":"Cleric","race":"Gnome"})
            
            self.assertEqual(response.json,{"STR":20,"DEX":20,"CON":20,"INT":20,"WIS":20,"CHA":20})
            
            self.assertEqual(response.status_code,200)
    
class TestStatRoller(TestBase):
    def test_roll_result(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = stat_roller('Cleric','Gnome')
            self.assertEqual(response,{"STR":3,"DEX":3,"CON":4,"INT":5,"WIS":3,"CHA":3})
        
