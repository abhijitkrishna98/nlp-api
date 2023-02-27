from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import spacy
import json
from textblob import TextBlob
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pyAudioAnalysis import audioSegmentation
from django.conf import settings


@csrf_exempt
def nlp_api(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        print(f"resopnse= \t {data}")
        input_text = data.get('text')
        # print(input_text)
        pipeline = data.get('pipeline')
        print(pipeline)
        if "tokenize" in pipeline:
            tokenized = tokenize(input_text)
            print(tokenized)
        if "sentiment" in pipeline:
            sent = sentiment(input_text)
            print(sent)
        if "diarization" in pipeline:
            diariztion = speaker()
            print(diariztion)
        # print(f"{tokenized}    {sent}      {diariztion}")
        return HttpResponse("Done")


def tokenize(input_text):
    nlp = spacy.load('en_core_web_sm')
    tokenized_output = []
    doc = nlp(input_text)
    for token in doc:
        tokenized_output.append(token.text)
    return(tokenized_output)


def sentiment(input_text):
    blob = TextBlob(input_text)
    score = blob.sentiment.polarity
    # sid = SentimentIntensityAnalyzer()
    # scores = sid.polarity_scores(text)
    # return sentiment_score
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


def speaker():
    audio_segmentation = audioSegmentation.speaker_diarization(
        f"{settings.BASE_DIR}/male.wav", n_speakers=2)
    return (audio_segmentation)
