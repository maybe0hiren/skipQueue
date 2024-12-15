from kivy.uix.accordion import NumericProperty
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd
import random
import csv

pay = []

#test for github

class Interface(ScreenManager):
    pass
sm = Interface()

profiles = pd.read_csv('database.csv')

class Pop(FloatLayout):
    pass

def invalid_notif():
    show = Pop()
    window = Popup(title = "Invalid", content = show, size_hint = (None,None), size = (300,100))
    window.open()

class Invalid(Widget):
    def btn(self):
        invalid_notif()

class LoginPage(Screen):
    email = ObjectProperty(None)
    pswd = ObjectProperty(None) 
    def verify(self):
        email = self.email.text 
        pswd = self.pswd.text
        with open('database.csv', mode="r") as userInfo:
            read = csv.reader(userInfo, delimiter=",")
            for row in read:
                if row == [email,pswd]:
                    self.manager.current = 'home'
                    break
                else:
                    invalid_notif()
                    break

        
    def but_animate(self, widget):
            animate = Animation(
                size_hint = (0.085,0.045),
                duration = 0.1
            )
            animate += Animation(
                size_hint = (0.1,0.05),
                duration = 0.1
            )
            animate.start(widget)
    def txt_animate(self, widget):
            animate = Animation(
                color = (0,0,1,1),
                duration = 0.1
            )
            animate += Animation(
                color = (0,0,0,1),
                duration = 0.1
            )
            animate.start(widget)
class SignupPage(Screen):
    email = ObjectProperty(None)
    pswd = ObjectProperty(None)
    def but_animate(self, widget):
            animate = Animation(
                size_hint = (0.12,0.045),
                duration = 0.1
            )
            animate += Animation(
                size_hint = (0.15,0.05),
                duration = 0.1
            )
            animate.start(widget)
    def sign(self):
        with open('database.csv', newline='') as file:
            read = csv.reader(file)
            rows = list(read)
        newRows = rows[:0]
        with open('database.csv', 'w', newline='') as file:
            write = csv.writer(file)
            write.writerows(newRows)
        with open('database.csv', mode="a", newline="") as userInfo:
            write = csv.writer(userInfo, delimiter=",")
            email = self.email.text
            pswd = self.pswd.text
            write.writerow([email, pswd])
            
class HomePage(Screen):
    def but_animate(self, widget):
        animate = Animation(
            background_color = (0,0,1,1),
            duration = 0.1
        )
        animate += Animation(
            background_color = (0,0,0,0),
            duration = 0.1
        )
        animate.start(widget)
    def txt_animate(self, widget):
        animate = Animation(
            color = (1,0,0,1),
            duration = 0.1
        )
        animate += Animation(
            color = (0,0,0,1),
            duration = 0.1
        )
        animate.start(widget) 

class VitMain(Screen):
    order = ObjectProperty
    price = NumericProperty
    def GetOrder(self, order,price):
        print(order, ":", price)
        pay.append(price)
        kart = 0
        for i in range(len(pay)):
            kart += pay[i]
        print(kart)
    def but_animate(self, widget):
        for i in range(len(pay)):
            pay.remove(pay[0])
        animate = Animation(
            size_hint = (0.12,0.045),
            duration = 0.1
        )
        animate += Animation(
            size_hint = (0.13,0.05),
            duration = 0.1
        )
        animate.start(widget)   
class VitFC(Screen):
    order = ObjectProperty
    price = NumericProperty
    def GetOrder(self, order,price):
        print(order, ":", price)
        pay.append(price)
        kart = 0
        for i in range(len(pay)):
            kart += pay[i]
        print(kart)
    def but_animate(self, widget):
        for i in range(len(pay)):
            pay.remove(pay[0])
        animate = Animation(
            size_hint = (0.12,0.045),
            duration = 0.1
        )
        animate += Animation(
            size_hint = (0.13,0.05),
            duration = 0.1
        )
        animate.start(widget)    
class VitPoona(Screen):
    order = ObjectProperty
    price = NumericProperty
    def GetOrder(self, order,price):
        print(order, ":", price)
        pay.append(price)
        kart = 0
        for i in range(len(pay)):
            kart += pay[i]
        print(kart)
    def but_animate(self, widget):
        for i in range(len(pay)):
            pay.remove(pay[0])
        animate = Animation(
            size_hint = (0.12,0.045),
            duration = 0.1
        )
        animate += Animation(
            size_hint = (0.13,0.05),
            duration = 0.1
        )
        animate.start(widget)    
class VitNesCafe(Screen):
    order = ObjectProperty
    price = NumericProperty
    def GetOrder(self, order,price):
        print(order, ":", price)
        pay.append(price)
        kart = 0
        for i in range(len(pay)):
            kart += pay[i]
        print(kart)
    def but_animate(self, widget):
        for i in range(len(pay)):
            pay.remove(pay[0])
        animate = Animation(
            size_hint = (0.12,0.045),
            duration = 0.1
        )
        animate += Animation(
            size_hint = (0.13,0.05),
            duration = 0.1
        )
        animate.start(widget)
class VitKiosk(Screen):
    order = ObjectProperty
    price = NumericProperty
    def GetOrder(self, order,price):
        print(order, ":", price)
        pay.append(price)
        kart = 0
        for i in range(len(pay)):
            kart += pay[i]
        print(kart)
    def but_animate(self, widget):
        for i in range(len(pay)):
            pay.remove(pay[0])
        animate = Animation(
            size_hint = (0.12,0.045),
            duration = 0.1
        )
        animate += Animation(
            size_hint = (0.13,0.05),
            duration = 0.1
        )
        animate.start(widget)    
class VitCoffee(Screen):
    order = ObjectProperty
    price = NumericProperty
    def GetOrder(self, order,price):
        print(order, ":", price)
        pay.append(price)
        kart = 0
        for i in range(len(pay)):
            kart += pay[i]
        print(kart)
    def but_animate(self, widget):
        for i in range(len(pay)):
            pay.remove(pay[0])
        animate = Animation(
            size_hint = (0.12,0.045),
            duration = 0.1
        )
        animate += Animation(
            size_hint = (0.13,0.05),
            duration = 0.1
        )
        animate.start(widget)    
        
class RecieptPage(Screen):
    tokenNumber = ObjectProperty
    tokenNumber = str(random.randint(0,1000))
    



kv = Builder.load_file('gui.kv')
class SkipQueueApp(App):
    def build(self):
        return kv
if __name__ == '__main__':
    SkipQueueApp().run()