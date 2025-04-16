# Código remoto para controlar el LED - puedes editar este archivo en GitHub
from machine import Pin
import time

def main():
    led = Pin(8, Pin.OUT)
    
    # Patrón personalizable desde GitHub
    print("Ejecutando código desde GitHub - LED.py")
    
    while True:
        # Secuencia rápida (3 parpadeos rápidos)
        for _ in range(3):
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(0.5)
        
        # Pausa larga
        time.sleep(2)
        
        # Secuencia lenta
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

# El código principal ejecutará esta función
