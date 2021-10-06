import machine
import utime

led1_red = machine.Pin(2,machine.Pin.OUT)
led1_amber = machine.Pin(3,machine.Pin.OUT)
led1_green = machine.Pin(4,machine.Pin.OUT)

led2_red = machine.Pin(6,machine.Pin.OUT)
led2_amber = machine.Pin(7,machine.Pin.OUT)
led2_green = machine.Pin(8,machine.Pin.OUT)

led3_red = machine.Pin(18,machine.Pin.OUT)
led3_amber = machine.Pin(19,machine.Pin.OUT)
led3_green = machine.Pin(20,machine.Pin.OUT)

led4_red = machine.Pin(26,machine.Pin.OUT)
led4_amber = machine.Pin(27,machine.Pin.OUT)
led4_green = machine.Pin(28,machine.Pin.OUT)

rld = 10; #red light delay time
dbg = 2; #delay time before green light

def a():
    
    led2_red.value(1)
    led3_red.value(1)
    led4_red.value(1)
    utime.sleep(dbg)
    led1_red.value(0)
    led1_green.value(1)

def b():
    
    led1_red.value(1)
    led3_red.value(1)
    led4_red.value(1)
    utime.sleep(dbg)
    led2_red.value(0)
    led2_green.value(1)

def c():
    
    led2_red.value(1)
    led1_red.value(1)
    led4_red.value(1)
    utime.sleep(dbg)
    led3_red.value(0)
    led3_green.value(1)

def d():
    
    led2_red.value(1)
    led3_red.value(1)
    led1_red.value(1)
    utime.sleep(dbg)
    led4_red.value(0)
    led4_green.value(1)
    
def amber_a():
    led1_amber.value(1)
    led2_red.value(1)
    led3_red.value(1)
    led4_red.value(1)

def amber_b():
    led2_amber.value(1)
    led1_red.value(1)
    led3_red.value(1)
    led4_red.value(1)
     
def amber_c():
    led3_amber.value(1)
    led2_red.value(1)
    led1_red.value(1)
    led4_red.value(1)

def amber_d():
    led4_amber.value(1)
    led2_red.value(1)
    led3_red.value(1)
    led1_red.value(1)
 
def off_led():
    led1_green.value(0)
    led1_amber.value(0)
    
    led2_green.value(0)
    led2_amber.value(0)
    
    led3_green.value(0)
    led3_amber.value(0)
    
    led4_green.value(0)
    led4_amber.value(0)
     
while True:
    off_led()
    a()
    utime.sleep(rld)
    off_led()
    amber_a()
    utime.sleep(1)
    off_led()
    b()
    utime.sleep(rld)
    off_led()
    amber_b()
    utime.sleep(1)
    off_led()
    c()
    utime.sleep(rld)
    off_led()
    amber_c()
    utime.sleep(1)
    off_led()
    d()
    utime.sleep(rld)
    off_led()
    amber_d()
    utime.sleep(1)
        
