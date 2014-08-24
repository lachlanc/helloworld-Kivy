# #! /usr/bin/python2
#  from kivy.app import App 
# class main(App):
# 	pass
# if __name__ == '__main__':
# 	main().run() 

from kivy.app import App
from kivy.uix.button import Button
  
class Hello(App):
    def build(self):
        btn = Button(text='Hello World')
        return  btn
  
Hello().run()