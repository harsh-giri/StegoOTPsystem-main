from stegano import lsb

def decrypt(enc_image):
	clear_message = lsb.reveal(enc_image)
	return clear_message
