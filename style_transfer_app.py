import streamlit as st
from PIL import Image
import io
from Localization import Localization
from model_wrapper import ModelWrapper

st.set_page_config(page_title="Style Transformation",
                    page_icon="title_icon.jpg")

if "current_lang" not in st.session_state:
  st.session_state["current_lang"] = "en"

def on_lang_change():
  st.session_state.current_lang = st.session_state.selected_lang

@st.cache_resource
def load_wrapper():
  wrapper = ModelWrapper("gen_f.h5")
  return wrapper

def load_localization():
  local = Localization("localizations", st.session_state.current_lang)
  return local

wrapper = load_wrapper()
localizer = load_localization()

lang_code_map = {local["name"]:local["code"] for local in localizer.available_locals()}
code_lang_map = {v:k for k, v in lang_code_map.items()}

titl_image = Image.open('title_icon.jpg')
titl_image = titl_image.resize((60,60))
st.image(titl_image)

st.title(localizer.localize("title"))
st.markdown(localizer.localize("desc"))

st.selectbox(localizer.localize("select_language"), 
              list(lang_code_map.values()), 
              index=localizer.current_language_index(),
              format_func=lambda x: code_lang_map[x],
              on_change=on_lang_change,
              key="selected_lang")

uploaded_image = st.file_uploader(localizer.localize("select_image"), type=["jpg"])
if uploaded_image is not None:
  img_byte = io.BytesIO(uploaded_image.getvalue())
  image = Image.open(img_byte)
  image = image.convert("RGB")
  width, height = image.size
  st.image(image, caption=localizer.localize("original_image"))

  if st.button(localizer.localize('transform'), type="primary"):
    out_image = wrapper.predict_from_PIL(image)
    out_resized_image = out_image.resize((width, height))
    st.image(out_resized_image, caption=localizer.localize("vangogh_image"))
    st.image(out_image, caption=localizer.localize("vangogh_image"))



