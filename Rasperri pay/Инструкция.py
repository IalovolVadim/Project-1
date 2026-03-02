#Включение светодиода 
import Rpi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM) #Настраиваем как обращаться к пинам
GPIO.setup(14,GPIO.OUT) #Вход/выход 
GPIO.output(14,1) #Что подаем на выходящее пины
