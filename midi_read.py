# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mido

m = mido.MidiFile("entchen.mid")

for msg in m:
    if not msg.is_meta:
        print(msg)
