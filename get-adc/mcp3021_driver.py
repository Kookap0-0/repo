import smbus
import time as t

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
        return number
    
    # def set_number(self, number):
    #     first_byte = self.wm | self.pds | number >> 8
    #     second_byte = number & 0xFF
    #     self.bus.write_byte_data(0x61, first_byte, second_byte)
    
    def get_voltage(self):
        voltage = self.get_number()*self.dynamic_range/652
        if self.verbose:
            print(f"Напряжение: {voltage}")
        return voltage
        

if __name__ == "__main__":
    try:
        adc = MCP3021(3.283, True)
        
        while True:
            try:
                adc.get_voltage()
                t.sleep(1.1)

            except KeyboardInterrupt():
                print("Keyboard interruption\n")

    finally:
        adc.deinit()

