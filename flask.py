#!/usr/bin/python
# -*- coding: utf-8 -*- 

import time
import YanAPI
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

ip_addr = "192.168.1.248"
YanAPI.yan_api_init(ip_addr)


#----flask init---------------------
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/led/<int:id>',methods=['POST'])
def button_led(id):
    if request.method == 'POST':
        if id == 1:
            YanAPI.set_robot_led("button", "red", "on")
            print('ok turn on led')
        elif id == 2:
            YanAPI.set_robot_led("button", "blue", "breath")
            print('ok turn off led')
    return redirect(url_for('index'))

@app.route('/robot/<int:id>',methods=['POST'])
def robot_control(id):
    if request.method == 'POST':
        if id == 1:
	        YanAPI.start_play_motion("walk", "forward", "normal", 2, 1)
	        time.sleep(3)
	        YanAPI.start_play_motion("reset")
	        print('ok robot move forward')
        elif id == 2:
	        YanAPI.start_play_motion("walk", "backward", "normal", 3, 1)
	        time.sleep(3)
	        YanAPI.start_play_motion("reset")
	        print('ok robot backward')
        elif id == 3:
	        YanAPI.start_play_motion("walk", "left", "normal", 3, 1)
	        time.sleep(3)
	        YanAPI.start_play_motion("reset")
	        print('ok robot move left')
        elif id == 4:
	        YanAPI.start_play_motion("walk", "right", "normal", 3, 1)
	        time.sleep(3)
	        YanAPI.start_play_motion("reset")
	        print('ok robot move right')
        elif id == 5:
                YanAPI.start_play_motion("raise", "left", "normal", 3, 1)
                time.sleep(3)
                YanAPI.start_play_motion("reset")
                print('ok robot raise left hand')
        elif id == 6:
	        YanAPI.start_play_motion("bow", "", "very slow")
	        time.sleep(3)
	        YanAPI.start_play_motion("reset")
	        print('ok robot bow')
        elif id == 7:
                YanAPI.start_voice_tts("你好，我是一个智能教学机器人")
                print('ok robot say something')
        elif id == 8:
	        YanAPI.stop_play_motion()
	        print('ok robot stop motion') 
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run( host='192.168.1.248', port=5000, debug=True )



