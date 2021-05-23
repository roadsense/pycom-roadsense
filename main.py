from machine import UART
# this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
uart = UART(1, baudrate=115200, rx_buffer_size=8192)

while uart.any() > 0:               # returns the number of characters available for reading
    # byte = uart.read(0) # read up to 5 bytes
    # Frame += byte + " "
    uart.readinto(Frame)
    
print(Frame)