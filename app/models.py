# this module contains the classes for the project
import datetime


class Member(object):
	"""the member's age & name """
	def __init__(self, name, age):
		self.id = 0
		self.name = name
		self.age = age
		self.posts = []

	def __str__(self):
		#return f"Name: {self.name}, Age: {self.age}"
		return "Name: {}, Age: {}".format(self.name, self.age)

class Post(object):
	"""the post's manupilations class"""
	def __init__(self, title, content, member_id= 0):
		self.id = 0
		self.title = title
		self.content = content
		self.member_id = member_id
		self.date = datetime.datetime.now()


	def __str__(self):
		#return f"Title: {self.title}, Content: {self.content}"
		return "Title: {}, Content: {}".format(self.title, self.topic)
    