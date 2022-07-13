from flask import Flask, render_template, url_for, request
from email_send import *
from get_random_image import *
from encrypt import *
from decrypt import *

app = Flask(__name__)

@app.route("/get-otp", methods=["GET", "POST"])
def getOTP():
	if request.method == "GET":
		return render_template("getOTP.html")
	elif request.method == "POST":
		if "email" in request.form.keys():
			email = request.form["email"]
			image = get_random_image()
			enc_image = encrypt(image)
			send_an_email(email, enc_image)
			return "Email successfully delivered!"
		else:
			return "Invalid parameter."

@app.route("/validate-otp", methods=["GET", "POST"])
def validateOTP():
	if request.method == "GET":
		return render_template("validateOTP.html")
	elif request.method == "POST":
		if "file" in request.files.keys():
			f = request.files["file"]
			f.save("saved/" + f.filename)
			client_otp = decrypt("saved/" + f.filename)
			with open("otp.txt", "r") as rf:
				system_otp = rf.read()
			if client_otp == system_otp:
				return "SUCCESS! OTP verified."
			else:
				return "Verification failed."
		else:
			return "Invalid parameter."

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == "__main__":
	app.run()