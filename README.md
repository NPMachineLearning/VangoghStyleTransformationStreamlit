# Style Transformation Introduction

This is an streamlit app of style transformation that
can automatically transform a image into Vangogh style.

## Deep learning model

The model is hosted on cloud storage [here](https://console.cloud.google.com/storage/browser?project=ml-models-413605&prefix=&forceOnBucketsSortingFiltering=true). **Only me can access to edit permission**. The public URL to the model file is in cloud
storage.

## Local development

1. Open terminal and cd to this directory
2. Add `secrets.toml` to project follow [here](https://blog.streamlit.io/secrets-in-sharing-apps/)
3. Edit `screts.toml` by add key and value like below
   `model_url = "[to_model_file_url_in_server]"`
4. Create python environment `python -m .venv .\`
5. Activate environment `venv\scripts\activate`
6. Install dependencies `pip install tensorflow streamlit pipreqs`
7. Start streamlit `streamlit run style_transfer_app.py`

## Deploy to streamlit

1. Open terminal and cd to this directory
2. Add secrets to for delopyed project follow [here](https://blog.streamlit.io/secrets-in-sharing-apps/)
3. Edit secrets by add key and value like below
   `model_url = "[to_model_file_url_in_server]"`
4. Create python environment `python -m .venv .\` if not
5. Activate environment `venv\scripts\activate`
6. Install dependencies `pip install tensorflow streamlit pipreqs`
7. Make sure streamlit app is working `streamlit run style_transfer_app.py`
8. add requirements.txt file and edit as following

```
tensorflow==2.14.0
numpy==1.24.3
```

**Note**:

1. Python 3.9 is recommend
