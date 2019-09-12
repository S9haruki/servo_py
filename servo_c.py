#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
import time
import signal
import sys


# def rotate_servo(servo, angle):
#     # 2.5 - 12 (9.5)
#     # 0 - 180
#     d = (angle / 18.94736842105263) + 2.0
#     servo.ChangeDutyCycle(d)
def rotate_servo(servo, angle):
    #   0度の位置 0.5 ms / 20 ms * 100 = 2.5 %
    # 180度の位置 2.4 ms / 20 ms * 100 = 12 %
    #      変動幅 12% - 2.5% (9.5%)
    # angle * 9.5 / 180
    if 0 <= angle <= 180:
        d = ((angle * 8.5 / 180) + 3.5)
        servo.ChangeDutyCycle(d)
    else:
        raise ValueError("angle")

def servo_angle(angle):
    if 0 <= angle <= 180:
        d = ((angle * 8.5 / 180) + 3.5)
        return d;
    else:
        raise ValueError("angle")
        return 0;



def init_servo(gpios):
    """
    初期化します。gpiosは利用するGPIOをLISTで指定してください。
    :param gpios: GPIO番号(LIST)
    :return: GPIO.PWM (List)
    """
    pwms = []
    GPIO.setmode(GPIO.BCM)
    if isinstance(gpios, list):
        for gpio in gpios:
            GPIO.setup(gpio, GPIO.OUT)
            # GPIO.PWM(GPIO, 周波数(Hz))
            s = GPIO.PWM(gpio, 50)
            s.start(0.0)
            pwms.append(s)
    else:
        raise Exception("gpios isn't list object.")

    return pwms
#目close 口close
def move_servo_A1(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(165)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)
        d1 = servo_angle(165)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)

#目close 口open
def move_servo_A2(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(165)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)
        d1 = servo_angle(165)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)

#目close 口pakupaku
def move_servo_A3(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(165)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)
        d1 = servo_angle(165)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)

#目open 口close
def move_servo_B1(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(33)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)
        d1 = servo_angle(33)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)

#目open 口open
def move_servo_B2(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(33)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)
        d1 = servo_angle(33)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)

#目open 口pakupaku
def move_servo_B3(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(33)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)
        d1 = servo_angle(33)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)

#目patipati 口close
def move_servo_C1(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(165)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)
        d1 = servo_angle(33)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)

#目patipati 口open
def move_servo_C2(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(165)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)
        d1 = servo_angle(33)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)

#目patipati 口pakupaku
def move_servo_C3(pwms,times):
    times = int(times/0.5)
    for t in range(times):
        d1 = servo_angle(165)
        d2 = servo_angle(83)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 0)
        #rotate_servo(pwms[1], 0)
        time.sleep(0.25)
        d1 = servo_angle(33)
        d2 = servo_angle(75)
        pwms[0].ChangeDutyCycle(d1)
        pwms[1].ChangeDutyCycle(d2)
        #rotate_servo(pwms[0], 120)
        #rotate_servo(pwms[1], 45)
        time.sleep(0.25)

#口pakupakuコマンド
def move_pakupaku(pwms,times):
    times = int(times/1)
    for t in range(times):

        
        d2 = servo_angle(83)
        pwms[1].ChangeDutyCycle(d2)
        time.sleep(0.25)

        d2 = servo_angle(75)
        pwms[1].ChangeDutyCycle(d2)
        time.sleep(0.25)

        d2 = servo_angle(83)
        pwms[1].ChangeDutyCycle(d2)
        time.sleep(0.25)

        d2 = servo_angle(67)
        pwms[1].ChangeDutyCycle(d2)
        time.sleep(0.25)


if __name__ == "__main__":
    # GPIO 12番を使用
    pwms =[]
    GPIO_12 = 12
    GPIO_13 = 13
    GPIO.setmode(GPIO.BCM)
    #######################
    GPIO.setup(12, GPIO.OUT)
    s = GPIO.PWM(12, 50)
    s.start(0.0)
    pwms.append(s)
    #######################
    GPIO.setup(13, GPIO.OUT)
    s = GPIO.PWM(13, 50)
    s.start(0.0)
    pwms.append(s)
    #######################

    # 初期化
    #pwms = init_servo([GPIO_12, GPIO_13])

    try:
        # -90°の位置まで動かし3秒停止します。
        move_servo_A1(pwms,4)
        move_servo_A2(pwms,4)
        move_servo_A3(pwms,4)
        move_servo_B1(pwms,4)
        move_servo_B2(pwms,4)
        move_servo_B3(pwms,4)
        move_servo_C1(pwms,4)
        move_servo_C2(pwms,4)
        move_servo_C3(pwms,4)


    except KeyboardInterrupt as ki:
        # サーボの動作を停止します。
        pwms[0].stop()
        pwms[1].stop()
        GPIO.cleanup()
