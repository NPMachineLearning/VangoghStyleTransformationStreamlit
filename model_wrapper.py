import tensorflow as tf
from PIL import Image
from instance_norm import InstanceNormalization

class ModelWrapper:
  def __init__(self, model_path):
    self.image_size = (256,256)
    self.custom_objects={"CycleGAN>InstanceNormalization":InstanceNormalization}
    self.model = tf.keras.models.load_model(model_path,
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
