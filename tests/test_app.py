#tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>About · Nikki Licea</title>' in html
        # TODO Add more tests relating to the home page

    def test_timeline(self):
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert 'timeline_posts' in json
        assert len(json['timeline_posts']) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add  more tests relating to the timeline page


    def test_faulty_post(self):
        # POST Request with no name
        response = self.client.post("/api/timeline_post", data={"email": "sristipanchu@gmail.com", "content": "Hiiii!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Name" in html

        # Faulty email
        response = self.client.post("/api/timeline_post", data={"name": "sristi", "email": "hi", "content" : "Hi"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Email" in html
        
        # no content
        response = self.client.post("/api/timeline_post", data={"name": "Sristi", "email": "sristipanchu@gmail.com"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Content" in html
