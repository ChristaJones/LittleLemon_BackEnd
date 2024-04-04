from django.test import TestCase, Client



class ViewTest(TestCase):
	def test_view_home(self):
		client = Client()
		response = self.client.get('/restaurant/')
		self.assertEquals(response.status_code, 200)
		#print("content", response.content)
		#self.assertContains(response.content, "Copyright 2024 Little Lemon")
		
		