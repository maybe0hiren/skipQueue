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
import requests
from firebase import firebase


try:
    pay = []
    orderList = []

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
        tokenId = ObjectProperty(None)
        pswd = ObjectProperty(None) 
        def verify(self):
            tokenId = self.tokenId.text
            pswd = self.pswd.text
            with open('database.csv', mode="r") as userInfo:
                read = csv.reader(userInfo, delimiter=",")
                for row in read:
                    if row == [tokenId,pswd]:
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
            orderList.append(order + str(" - ") + str(RecieptPage.tokenNumber))
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
        def orderDatabase(self):
            firebaseUrl = "https://skipqueue-5f654-default-rtdb.firebaseio.com/.json"
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/MainOrder', None)
            DatabaseOrderList = {'MainOrder':prepOrderList + orderList}
            upload = requests.patch(url=firebaseUrl, json=DatabaseOrderList)
            print(upload)
            
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
            orderList.append(order + str(" - ") + str(RecieptPage.tokenNumber))
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
        def orderDatabase(self):
            firebaseUrl = "https://skipqueue-5f654-default-rtdb.firebaseio.com/.json"
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/FCOrder', None)
            DatabaseOrderList = {'FCOrder':prepOrderList + orderList}
            upload = requests.patch(url=firebaseUrl, json=DatabaseOrderList)
            print(upload)   
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
            orderList.append(order + str(" - ") + str(RecieptPage.tokenNumber))
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
        def orderDatabase(self):
            firebaseUrl = "https://skipqueue-5f654-default-rtdb.firebaseio.com/.json"
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/PoonaOrder', None)
            DatabaseOrderList = {'PoonaOrder':prepOrderList + orderList}
            upload = requests.patch(url=firebaseUrl, json=DatabaseOrderList)
            print(upload)  
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
            orderList.append(order + str(" - ") + str(RecieptPage.tokenNumber))
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
        def orderDatabase(self):
            firebaseUrl = "https://skipqueue-5f654-default-rtdb.firebaseio.com/.json"
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/NesCafeOrder', None)
            DatabaseOrderList = {'NesCafeOrder':prepOrderList + orderList}
            upload = requests.patch(url=firebaseUrl, json=DatabaseOrderList)
            print(upload)
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
            orderList.append(order + str(" - ") + str(RecieptPage.tokenNumber))
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
        def orderDatabase(self):
            firebaseUrl = "https://skipqueue-5f654-default-rtdb.firebaseio.com/.json"
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/KioskOrder', None)
            DatabaseOrderList = {'KioskOrder':prepOrderList + orderList}
            upload = requests.patch(url=firebaseUrl, json=DatabaseOrderList)
            print(upload)   
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
            orderList.append(order + str(" - ") + str(RecieptPage.tokenNumber))
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
        def orderDatabase(self):
            firebaseUrl = "https://skipqueue-5f654-default-rtdb.firebaseio.com/.json"
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/CoffeeOrder', None)
            DatabaseOrderList = {'CoffeeOrder':prepOrderList + orderList}
            upload = requests.patch(url=firebaseUrl, json=DatabaseOrderList)
            print(upload) 

    class CanteenCode(Screen):
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
        def checkCode(self):
            code = self.ids.canteenCode.text
            if code == "key1":
                page = 'canteenmanagermain'
            elif code == "key2":
                page = 'canteenmanagerfc'
            elif code == 'key3':
                page = 'canteenmanagerkiosk'
            elif code == 'key4':
                page = 'canteenmanagernescafe'
            elif code == 'key5':
                page = 'canteenmanagerpoona'
            elif code == 'key6':
                page = 'canteenmanagercoffee'
            else:
                invalid_notif()
                page = 'canteencode'
            return page

    class CanteenManagerMain(Screen):
        n = 0
        track = "Click to get more orders."
        def order(self):
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/MainOrder', None)
            prepOrder = prepOrderList[CanteenManagerMain.n] + '\n' + CanteenManagerMain.track
            print(prepOrder)
            if CanteenManagerMain.n < len(prepOrderList)-1:
                CanteenManagerMain.n = CanteenManagerMain.n + 1  
            else:
                CanteenManagerMain.track = "No more Orders"
            self.ids.OrderMainName.text = str(CanteenManagerMain.n) + " : " + prepOrder

        def but_animate(self, widget):
                animate = Animation(
                    size_hint = (0.11,0.045),
                    duration = 0.1
                )
                animate += Animation(
                    size_hint = (0.13,0.05),
                    duration = 0.1
                )
                animate.start(widget)    
    class CanteenManagerFC(Screen):
        n = 0
        track  = "Click to get more orders."
        def order(self):
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/FCOrder', None)
            prepOrder = prepOrderList[CanteenManagerFC.n] + '\n' + CanteenManagerFC.track
            print(prepOrder)
            if CanteenManagerFC.n < len(prepOrderList)-1:
                CanteenManagerFC.n = CanteenManagerFC.n + 1
            else:
                CanteenManagerFC.track = "No more orders"
            self.ids.OrderFCName.text = str(CanteenManagerFC.n) + " : " + prepOrder

        def but_animate(self, widget):
                animate = Animation(
                    size_hint = (0.11,0.045),
                    duration = 0.1
                )
                animate += Animation(
                    size_hint = (0.13,0.05),
                    duration = 0.1
                )
                animate.start(widget)
    class CanteenManagerNescafe(Screen):
        n = 0
        track  = "Click to get more orders."
        def order(self):
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/NesCafeOrder', None)
            prepOrder = prepOrderList[CanteenManagerNescafe.n] + '\n' + CanteenManagerNescafe.track
            print(prepOrder)
            if CanteenManagerNescafe.n < len(prepOrderList)-1:
                CanteenManagerNescafe.n = CanteenManagerNescafe.n + 1
            else:
                CanteenManagerNescafe.track = "No more orders"
            self.ids.OrderNescafeName.text = str(CanteenManagerNescafe.n) + " : " + prepOrder

        def but_animate(self, widget):
                animate = Animation(
                    size_hint = (0.11,0.045),
                    duration = 0.1
                )
                animate += Animation(
                    size_hint = (0.13,0.05),
                    duration = 0.1
                )
                animate.start(widget)
    class CanteenManagerCoffee(Screen):
        n = 0
        track = "Click to get more orders."
        def order(self):
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/CoffeeOrder', None)
            prepOrder = prepOrderList[CanteenManagerCoffee.n] + '\n' + CanteenManagerCoffee.track
            print(prepOrder)
            if CanteenManagerCoffee.n < len(prepOrderList)-1:
                CanteenManagerCoffee.n = CanteenManagerCoffee.n + 1
            else:
                CanteenManagerCoffee.track = "No more Orders"
            self.ids.OrderCoffeeName.text = str(CanteenManagerCoffee.n) + " : " + prepOrder

        def but_animate(self, widget):
                animate = Animation(
                    size_hint = (0.11,0.045),
                    duration = 0.1
                )
                animate += Animation(
                    size_hint = (0.13,0.05),
                    duration = 0.1
                )
                animate.start(widget)
    class CanteenManagerPoona(Screen):
        n = 0
        track  = "Click to get more orders."
        def order(self):
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/PoonaOrder', None)
            prepOrder = prepOrderList[CanteenManagerPoona.n] + '\n' + CanteenManagerPoona.track
            print(prepOrder)
            if CanteenManagerPoona.n < len(prepOrderList)-1:
                CanteenManagerPoona.n = CanteenManagerPoona.n + 1
            else:
                CanteenManagerPoona.track = "No more orders"
            self.ids.OrderPoonaName.text = str(CanteenManagerPoona.n) + " : " + prepOrder

        def but_animate(self, widget):
                animate = Animation(
                    size_hint = (0.11,0.045),
                    duration = 0.1
                )
                animate += Animation(
                    size_hint = (0.13,0.05),
                    duration = 0.1
                )
                animate.start(widget)
    class CanteenManagerKiosk(Screen):
        n = 0
        track  = "Click to get more orders."
        def order(self):
            url = firebase.FirebaseApplication("https://skipqueue-5f654-default-rtdb.firebaseio.com", None)
            prepOrderList = url.get('/KioskOrder', None)
            prepOrder = prepOrderList[CanteenManagerKiosk.n] + '\n' + CanteenManagerKiosk.track
            print(prepOrder)
            if CanteenManagerKiosk.n < len(prepOrderList)-1:
                CanteenManagerKiosk.n = CanteenManagerKiosk.n + 1
            else:
                CanteenManagerKiosk.track = "No more orders"
            self.ids.OrderKioskName.text = str(CanteenManagerKiosk.n) + " : " + prepOrder

        def but_animate(self, widget):
                animate = Animation(
                    size_hint = (0.11,0.045),
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
        with open('database.csv',mode='r') as userInfo:
            userName = csv.reader(userInfo)
            for row in userName:
                tokenName = row[0]

    kv = Builder.load_file('gui.kv')
    class SkipQueueApp(App):
        def build(self):
            return kv
    if __name__ == '__main__':
        SkipQueueApp().run()
except Exception as E:
    pass