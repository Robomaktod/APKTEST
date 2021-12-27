import kivy
import socket
kivy.require('1.0.7')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.106', 2023))


class TestApp(App):
    def build(self):
        wid = Widget()

        Lbtn = Button(text='', on_press=lambda youtube: client.send('RMB'.encode()), width=430, height=580)
        Rbtn = Button(text='', on_press=lambda youtube: client.send('LMB'.encode()), width=430, height=580)
        SWsld = Slider(orientation='vertical')

        # sw


        layout = BoxLayout(size_hint=(None, 2), width=1080, height=2340)
        layout.add_widget(Rbtn)
        layout.add_widget(SWsld)
        layout.add_widget(Lbtn)



        root = BoxLayout(orientation='horizontal')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    TestApp().run()


