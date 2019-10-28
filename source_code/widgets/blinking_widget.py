from PyQt5.QtCore import QTimer

def make_label_can_blink(widget):
    widget.blinkTimer = QTimer(widget)
    widget.blinkCounter = 0
    widget.blinkText = ""
    widget.blinkTimer.setInterval(100)
    widget.blinkTimer.timeout.connect(lambda: blinkLoop(widget))


def blink(widget):
    widget.blinkCounter = 3
    widget.blinkText = widget.text()
    widget.blinkTimer.start()


def blinkLoop(widget):
    if widget.blinkCounter == 0:
        widget.blinkTimer.stop()
        return

    if widget.text():
        widget.setText("")
    else:
        widget.setText(widget.blinkText)
        widget.blinkCounter -= 1
