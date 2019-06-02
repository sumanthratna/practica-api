from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
from bs4 import BeautifulSoup

from collections import OrderedDict

URL = "https://www.123teachme.com/translated_sentences/prep"


@api_view(['GET'])
def sentence_generator(request):
    return Response(OrderedDict((
        ("info", "All requests must be GET requests."),
        ("/english/<word>/", "Fetch English sentences containing a given phrase."),
        ("/espanol/<palabra>/", "Busca oraciónes españoles que contiene un frase dada."),
    )))


def get_pairs(params):
    r = requests.get(url=URL, params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    pairs = []
    for tmp in soup.find_all('div', class_='translated-sentence-pair'):
        pair = {
            'español': tmp.find('div', class_='spanish-sentence').contents[0].strip(),
            'english': tmp.find('div', class_='english-sentence').contents[0].strip()
        }
        pairs.append(pair)
    return pairs


@api_view(['GET'])
def english(request, word):
    params = {"phrase": word, "trans_type": "e2s", "commit": "Submit"}
    return Response(get_pairs(params))


@api_view(['GET'])
def espanol(request, palabra):
    params = {"phrase": palabra, "trans_type": "s2e", "commit": "Submit"}
    return Response(get_pairs(params))
