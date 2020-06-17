#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
import time
import signal
import sys

def servo_angle(angle):
	if 0 <= angle <= 180:
		d = ((angle * 8.5 / 180) + 3.5)
		return d;
	else:
		raise ValueError("angle")
		return 0;



class servo_control:
	def __init__(self):
		# GPIO 12番を使用
		self.pwms =[]
		#self.GPIO_12 = 12
		#self.GPIO_13 = 13
		GPIO.setmode(GPIO.BCM)
		#######################
		GPIO.setup(12, GPIO.OUT)
		s = GPIO.PWM(12, 50)
		s.start(0.0)
		self.pwms.append(s)
		#######################
		GPIO.setup(13, GPIO.OUT)
		s = GPIO.PWM(13, 50)
		s.start(0.0)
		self.pwms.append(s)
		#######################
		self.mouth1 = 83
		self.mouth2 = 75
		self.mouth3 = 67
		#######################
		self.eye1 = 165
		self.eye2 = 33
		self.eye3 = 0
		#######################

	#目close 口close
	def move_servo_A1(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)
	
	#目close 口open
	def move_servo_A2(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)

	#目close 口pakupaku
	def move_servo_A3(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)

	
	#目open 口close
	def move_servo_B1(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)
	
	#目open 口open
	def move_servo_B2(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)
	
	#目open 口pakupaku
	def move_servo_B3(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)
	
	#目patipati 口close
	def move_servo_C1(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)
	
	#目patipati 口open
	def move_servo_C2(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye2)
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)
	
	#目patipati 口pakupaku
	def move_servo_C3(self,times):
	    times = int(times/0.5)
	    for t in range(times):
	        e_angle = servo_angle(self.eye1)
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)
 
	        time.sleep(0.25)
	        e_angle = servo_angle(self.eye2)
	        m_angle  = servo_angle(self.mouth2)
	        self.pwms[0].ChangeDutyCycle(e_angle)
	        self.pwms[1].ChangeDutyCycle(m_angle)

	        time.sleep(0.25)

	#single mouth move
	def move_servo_SERM(self):
	    m_angle = servo_angle(self.mouth1)
	    self.pwms[1].ChangeDutyCycle(m_angle)
 
	#single eye move
	def move_servo_SERE(self):
	    e_angle = servo_angle(self.eye1)
	    self.pwms[0].ChangeDutyCycle(e_angle)



	
	#口pakupakuコマンド
	def move_pakupaku(self,times):
	    times = int(times/1)
	    for t in range(times):
	
	        m_angle = servo_angle(self.mouth1)
	        self.pwms[1].ChangeDutyCycle(m_angle)
	        time.sleep(0.25)
	
	        m_angle = servo_angle(self.mouth2)
	        self.pwms[1].ChangeDutyCycle(m_angle)
	        time.sleep(0.25)

	        m_angle = servo_angle(self.mouth1)
	        self.pwms[1].ChangeDutyCycle(m_angle)
	        time.sleep(0.25)
	
	        m_angle = servo_angle(self.mouth3)
	        self.pwms[1].ChangeDutyCycle(m_angle)
	        time.sleep(0.25)

	#目winkコマンド
	def move_wink(self,times):
	    times = int(times/0.75)
	    for t in range(times):
	
	        m_angle = servo_angle(self.eye2)
	        self.pwms[0].ChangeDutyCycle(m_angle)
	        time.sleep(0.25)
	
	        m_angle = servo_angle(self.eye1)
	        self.pwms[0].ChangeDutyCycle(m_angle)
	        time.sleep(0.25)

	        m_angle = servo_angle(self.eye2)
	        self.pwms[0].ChangeDutyCycle(m_angle)
	        time.sleep(0.25)


if __name__ == "__main__":
    servo_m = servo_control()

    try:
        # -90°の位置まで動かし3秒停止します。
        servo_m.move_servo_A1(4)
        servo_m.move_servo_A2(4)
        servo_m.move_servo_A3(4)
        servo_m.move_servo_B1(4)
        servo_m.move_servo_B2(4)
        servo_m.move_servo_B3(4)
        servo_m.move_servo_C1(4)
        servo_m.move_servo_C2(4)
        servo_m.move_servo_C3(4)
        servo_m.move_pakupaku(4)

    except KeyboardInterrupt as ki:
        # サーボの動作を停止します。
        pwms[0].stop()
        pwms[1].stop()
        GPIO.cleanup()
