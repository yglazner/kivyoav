'''
Created on Dec 11, 2016

@author: yglazner
'''
from kivy.clock import Clock
from functools import wraps
import types



def _apply(g):
    for timeout in g:
        Clock.schedule_once(lambda dt: _apply(g), timeout=timeout)
        return
    


def delayable(fn):
    '''delayable decorator lets you write a function/method that can delay its execution by using "yield timeout". it cannot return any value though...
    also, exceptions will probaly get lost somewhere :)
    '''
    @wraps(fn)
    def _dec(*args, **kw):
        g = fn(*args, **kw)
        assert isinstance(g, types.GeneratorType), 'delayable decorator only works on generators! (put some yields inside the function ....)'
        Clock.schedule_once(lambda dt: _apply(g))
        return
    return _dec