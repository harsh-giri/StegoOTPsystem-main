import os
import random

def get_random_image():
  images = os.listdir("./uploads")
  rand_img = random.choice(images)
  return f"uploads/{rand_img}"