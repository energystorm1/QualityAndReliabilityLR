import time
import pywinauto
from pywinauto.application import Application


app = Application().start(cmd_line=r"C:\Program Files\PuTTY\putty.exe")#открываем putty
time.sleep(2)#ожидаем 5 секунд
app = Application().connect(title="PuTTY Configuration")
window = app.PuTTYConfigBox
window.set_focus()
window[u"Host Name (or IP address):Edit"].type_keys("fthats@tty.sdf.org")
#window[u"Port:Edit"].set_edit_text("")
#window[u"Port:Edit"].type_keys("21")
window["Open"].click()
time.sleep(4)
app = Application().connect(title="tty.sdf.org - PuTTY")
window = app.PuTTY
window.type_keys("RjASJwh4ZFTIPA")
window.type_keys("{ENTER}")
time.sleep(1)
window.type_keys("{BACKSPACE}")
time.sleep(1)
window.type_keys("{ENTER}")
window.type_keys("{ENTER}")

