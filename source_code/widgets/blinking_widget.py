"""Module Name: blinking_textlabel
Author: Wei Kaitao (U1922499K)
Description:
Provide functions to make the text label be able to blink.
"""
from PyQt5.QtCore import QTimer

def make_label_can_blink(textlabel):
    textlabel.blinkTimer = QTimer(textlabel)
    textlabel.blinkCounter = 0
    textlabel.blinkText = ""
    textlabel.blinkTimer.setInterval(100)
    textlabel.blinkTimer.timeout.connect(lambda: blink_loop(textlabel))


def blink(textlabel):
    textlabel.blinkCounter = 3
    textlabel.blinkText = textlabel.text()
    textlabel.blinkTimer.start()


def blink_loop(textlabel):
    if textlabel.blinkCounter == 0:
        textlabel.blinkTimer.stop()
        return

    if textlabel.text():
        textlabel.setText("")
    else:
        textlabel.setText(textlabel.blinkText)
        textlabel.blinkCounter -= 1
