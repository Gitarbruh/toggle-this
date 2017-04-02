import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

@app.route("/hello/<action>")
def hello(action):
 if action == "on":
  GPIO.output(4, True)
  message = "It's on"


 if action == "off":
  GPIO.output(4, False)
  message = "It's off"



 
 return render_template('main.html', action=action )

if __name__ == "__main__":
 app.run(host='0.0.0.0', port = 80, debug=True)

