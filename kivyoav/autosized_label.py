import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty

Builder.load_string("""
<AutoSizedLabel>:
    font_size: [self._calc_font_size(), self.size, self.ratio, self.text][0]
    ratio: 0.5
""")

class AutoSizedLabel(Label):
    
    ratio = NumericProperty(1.0)
    
    def __init__(self, **kw):
        self.old_stuff = []
        self.co_list = list()
        super().__init__(**kw)
        
        
    def _calc_font_size(self):

        if [self.size, self.texture_size] == self.old_stuff:
            return self.font_size
        if self.text == "":
            return self.font_size
        self.old_stuff = list(self.size), list(self.texture_size)
        id_ = object()
        self.co_list.append(id_)
        self._make_adjustments(id_=id_)
        return self.font_size

    def _make_adjustments(self, id_, growing=True):
        if self.co_list[0]!=id_:
            self.co_list.remove(id_)
            return
        w, h = self.size
        wt, ht = self.texture_size
        w = int(w*self.ratio)
        h = int(h*self.ratio)
        if w < wt or h < ht:
            self.font_size -= 1
            growing = False
        elif growing:
            self.font_size += 1
        else:
            self.co_list.remove(id_)
            return
       
        Clock.schedule_once(lambda dt: self._make_adjustments(id_=id_, 
                                                              growing=growing))
           
        
            

if __name__ == '__main__':
    class _TestApp(App):
        def build(self):
            return AutoSizedLabel(text="crazy\ncheese", ratio=0.5)

    _TestApp().run()
