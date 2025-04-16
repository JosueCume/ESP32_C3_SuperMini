from machine import Pin
import time

# Configurar el pin 8 como salida
led = Pin(8, Pin.OUT)

while True:
    # Encender el LED
    led.on()
    time.sleep(1)  # Esperar 1 segundo
    
    # Apagar el LED
    led.off()
    time.sleep(1)  # Esperar 1 segundo
