from flask import url_for
from flask_testing import TestCase
from app import app, PlayerInfo, db
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SQLALCEHMY_TRACK_MODIFICATIONS=False,
            DEBUG=True
            )
        return app
    
    def setUp(self):
        db.create_all()
        character1 = PlayerInfo(
            race = "Human", 
            role = "Cleric",
            strength = 15,
            dexterity = 12,
            constitution = 14,
            intelligence = 18,
            wisdom = 19,
            charisma = 9
        )
        db.session.add(character1)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestServer(TestBase):
    def test_home(self):
        default_stats={"STR":20,"DEX":19,"CON":18,"INT":17,"WIS":16,"CHA":15}
        with requests_mock.Mocker() as mocker:
            mocker.get('http://class_api:5000/get_class', text="Ranger")
            mocker.get('http://race_api:5000/get_race', text="Dragonborn")
            mocker.post('http://stat_api:5000/get_stats', json=default_stats)
            response= self.client.get(url_for('home'))
            self.assertEqual(response.status_code,200)
            for key, values in default_stats.items():
                statement = f'{key}: {values}'
                self.assertIn(statement.encode(),response.data)



