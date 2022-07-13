from stegano import lsb
import random
import string

def get_random_otp():
	return str(random.randint(1000, 9999))

def encrypt(image):
	filename = ''.join(random.choice(string.ascii_letters) for _ in range(10))
	otp = get_random_otp()
	secret = lsb.hide(image, otp)
	secret.save(f"outputs/{filename}.png")
	with open("otp.txt", "w") as wf:
		wf.write(otp)
	return f"outputs/{filename}.png"

