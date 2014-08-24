#! /usr/bin/python2
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
class simpleform(BoxLayout):
	def hello(self):
		print("hello world")

class main(App):
	def hello(self):
		print("Hello World")
	

if __name__ == '__main__':
	main().run() 
