import usb

class AirSensor(object):
    """docstring for AirSensor"""
    def __init__(self):
        vendor = 0x03eb
        product = 0x2013

        dev = usb.core.find(idVendor=vendor, idProduct=product)

        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)
        dev.reset()
        dev.set_configuration()

        self.dev = dev

    def get_voc(self):

        # @h*TR
        cmd = b'\x40\x68\x2a\x54\x52\x0a\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40'

        n = self.dev.write(0x02, cmd, timeout=10000)

        arr = self.dev.read(0x081, size_or_buffer=0x10, timeout=10000)
        voc = int.from_bytes(arr[2:4], byteorder="little")

        return voc
