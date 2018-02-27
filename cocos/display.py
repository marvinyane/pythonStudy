#! /usr/bin/env python

import cocos
import pyglet

class KeyDisplay(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(KeyDisplay, self).__init__()

        self.text = cocos.text.Label("", x=100, y=20)

        self.key_pressed = set()
        self.update_text()
        self.add(self.text)

    def on_key_press (self, key, modifiers):
        self.key_pressed.add(key)
        self.update_text()

    def on_key_release (self, key, modifiers):
        #self.key_pressed.remove(key)
        self.update_text()

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string (k) for k in self.key_pressed]
        text = 'keys: ' + ','.join(key_names)

        self.text.element.text = text

cocos.director.director.init(resizable=True)
cocos.director.director.run(cocos.scene.Scene(KeyDisplay()))
