from kivyoav import autosized_label
from kivy.lang import Builder
from kivy.app import App

class TestApp(App):
    def build(self):
        return Builder.load_string("""
<ButtonBox@BoxLayout+Button>:
    id: pop
    

BoxLayout:
    AutoSizedLabel:
        text: "Cool"
        ratio: 0.90
    GridLayout:
        cols: 2
        AutoSizedLabel:
            text: "1"
            ratio: 1.0
        AutoSizedLabel:
            text: "2"
            ratio: .5
        AutoSizedLabel:
            text: "3"
            ratio: .2
        ButtonBox:
            AutoSizedLabel:
                size_hint: 1., 1.
                text: "4"
                ratio: .8
            
        
        
        

"""             )
        
if __name__ == '__main__':
    TestApp().run()
        