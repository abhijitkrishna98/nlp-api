conda create -n nlp_env python=3.9
conda activate nlp_env
pip install -r requirements.txt
(maybe) pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz
python manage.py runserver

send api request to => http://127.0.0.1:8000/nlp_api
POST body
{
    "text": "This is cool",
    "pipeline": ["tokenize","sentiment","diarization"]
}
Note: pipeline is configurable