#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os

def convert_text_for_servo(command_action,num):
	text=[]
	#######################################################################
        # num = time
	# 実行コマンド
	#######################################################################
	if command_action == 'A1':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'A2':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'A3':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'B1':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'B2':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'B3':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'C1':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'C2':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'C3':
		text = 'ser.move_servo_'+ command_action + "(" + str(num) + ')'
		#print(text)
	elif command_action == 'SERM':
		text = 'ser.move_servo_'+ command_action + "(" + " " + ')'
		#print(text)
	elif command_action == 'SERE':
		text = 'ser.move_servo_'+ command_action + "(" + " " + ')'
		#print(text)
	elif command_action == 'pakupaku':
		text = 'ser.move_'+ command_action + "(" + str(num) + ')'
	elif command_action == 'wink':
		text = 'ser.move_'+ command_action + "(" + str(num) + ')'
	#######################################################################
	# num = degree
	# 変数を変更するコマンド,角度
	# 口　M1=, M2=, M3=,
	# 目　E1=, E2=, E3=,
	#######################################################################
		#print(text)
	elif command_action == 'M1=':
		text = 'ser.mouth1 = '+ str(num)
		#print(text)
	elif command_action == 'M2=':
		text = 'ser.mouth2 = '+ str(num)
		#print(text)
	elif command_action == 'M3=':
		text = 'ser.mouth3 = '+ str(num)
		#print(text)
	elif command_action == 'E1=':
		text = 'ser.eye1 = '+ str(num)
		#print(text)
	elif command_action == 'E2=':
		text = 'ser.eye2 = '+ str(num)
		#print(text)
	elif command_action == 'E3=':
		text = 'ser.eye3 = '+ str(num)
		#print(text)
	#######################################################################
	# num = time
	# time.sleep
	#######################################################################
	elif command_action == 'time':
		text = 'time.sleep('+ str(num) + ')'
		#print(text)


	else:
		test =''
	return text

fp = open(sys.argv[1], 'r')
command =[]
for line in fp.readlines():
	l = line.strip().strip("\n")
	l = l.split(',')
	l[1] = float(l[1])

	out = convert_text_for_servo(l[0],l[1])
	command.append(out)
fp.close()

#print(command)
file_name = sys.argv[1].replace("csv", "py")
file = open(file_name, 'w')
file.write("#!/usr/bin/env python3\n")
file.write("# -*- coding: UTF-8 -*-\n\n")
file.write("import RPi.GPIO as GPIO\n")
file.write("import time\n")
file.write("import signal\n")
file.write("import sys\n")
file.write("from servo_py import servo_d as serd\n")
file.write("#######################\n")
file.write("ser = serd.servo_control()\n")
file.write("#######################\n")

for w_c in command:
	file.write(w_c+"\n")

file.write("#######################\n")
file.write("ser.pwms[0].stop()\n")
file.write("ser.pwms[1].stop()\n")
file.write("GPIO.cleanup()\n")

file.close()

os.chmod(file_name, 0o777)
