from kivyoav import autosized_label
from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivyoav.delayed import delayable
import random



class MyBox(BoxLayout):
    
    
    
    @delayable
    def updated_loop(self):
        while 1:
            yield 0.3 # delay of 300ms
            self.t.text = random.choice(['clown', 'party', 'balloon', 'meat'])


class TestApp(App):
    def build(self):
        
        
        Builder.load_string("""\
<MyBox>:
    t: changing_text_id
    orientation: 'vertical'
    AutoSizedLabel:
        text: "The text below will keep changing using a delayed function..."
        ratio: 0.95
    AutoSizedLabel:
        id: changing_text_id
        text: "no change yet"
        ratio: 0.75
        
        """
        )
        mybox = MyBox()
        mybox.updated_loop()
        return mybox
        
if __name__ == '__main__':
    TestApp().run()
        