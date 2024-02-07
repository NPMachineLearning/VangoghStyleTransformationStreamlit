import tensorflow as tf
from PIL import Image
from instance_norm import InstanceNormalization
import urllib.request
import os
import streamlit as st
import numpy as np

class STProgressBar():
  def __init__(self, text=""):
    self.text = text
    self.progressbar = None
  def __call__(self, block_num, block_size, total_size):
    progress = block_num * block_size / total_size
    progress = np.clip(progress, 0.0, 1.0)
    if self.progressbar is None:
      self.progressbar = st.progress(value=0.0, text=self.text)
    if self.progressbar:
      self.progressbar.progress(value=progress, text=self.text)

MODEL_URL = "https://storage.googleapis.com/np-machine-learning-models/tf2/gan/photo2vangogh_gen_f.h5"
FILE_PATH = "./gen_f.h5"

class ModelWrapper:
  def __init__(self, download_progress:STProgressBar=None, download_complete=None):
    self.image_size = (256,256)
    self.custom_objects={"CycleGAN>InstanceNormalization":InstanceNormalization}
    if not os.path.exists(FILE_PATH):
      if download_progress is not None:
        urllib.request.urlretrieve(MODEL_URL, FILE_PATH, 
                                   reporthook=download_progress)
      else:
        urllib.request.urlretrieve(MODEL_URL, FILE_PATH)
      if download_complete is not None:
        download_complete()
    self.model = tf.keras.models.load_model(FILE_PATH,
                                            custom_objects=self.custom_objects,
                                            compile=False)
  
  def predict_from_PIL(self, img):
    input_data = self.get_input_data_array(img)
    output = self.model.predict(input_data, verbose=0)
    output_img = tf.squeeze(output, axis=0)
    output_img = output_img * 127.5 + 127.5
    output_img = tf.cast(output_img, tf.uint8)
    return Image.fromarray(output_img.numpy())

  def get_input_data_array(self, img):
    input_img = tf.keras.utils.img_to_array(img, dtype="uint8")
    input_img = tf.cast(input_img, tf.float32)
    input_img = (input_img - 127.5) / 127.5
    input_img = tf.image.resize(input_img, self.image_size)
    input_img = tf.expand_dims(input_img, axis=0)
    return input_img
