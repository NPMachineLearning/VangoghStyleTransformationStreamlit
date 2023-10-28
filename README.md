# Style Transformation Introduction

This is an streamlit app of style transformation that
can automatically transform a image into Vangogh style.

## Local development

1. Open terminal and cd to this directory
2. Create python environment `python -m venv .\`
3. Activate environment `venv\scripts\activate`
4. Install dependencies `pip install tensorflow streamlit pipreqs`
5. Start streamlit `streamlit run style_transfer_app.py`

## Deploy to streamlit

1. Open terminal and cd to this directory
2. Create python environment `python -m venv .\` if not
3. Activate environment `venv\scripts\activate`
4. Install dependencies `pip install tensorflow streamlit pipreqs`
5. Make sure streamlit app is working `streamlit run style_transfer_app.py`
6. Ouput **requirements.txt** `pipreqs .\`
7. Modify **requirements.txt**, remove any packages except following:
   - tensorflow

**Note**:

1. Python 3.9 is recommend
