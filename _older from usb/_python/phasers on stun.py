##import usb.core
##import usb.util
##from usb.backend import libusb1
##be = libusb1.get_backend()
##devices = usb.core.find(find_all = True, backend=be)
##print(str(devices))
import os
os.environ['PYUSB_DEBUG'] = 'debug'
import usb.core
usb.core.find()
