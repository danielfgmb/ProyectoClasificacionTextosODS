from django.shortcuts import render
from django.conf import settings
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from django.http import JsonResponse
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import os
import joblib

model = joblib.load(os.path.join(settings.BASE_DIR,"pipes/modeloP1E2Regresion.pkl"))


def clasificacion(request):
    return render(request, 'clasificacion.html', {})

def caracteristicas(request):
    return render(request, 'caracteristicas.html', {})

@csrf_exempt
def ajaxClasificacion(request):
    if request.method == 'POST':
        texts = request.POST.get('texts')
        texts = texts.replace("\\n"," ")
        texts = texts.split("\n")
        df = pd.Series(texts)
        df_res = pd.DataFrame()
        df_res["id"] = list(range(len(texts)))
        df_res["Textos"] = texts
        df_res["ODS"] = model.predict(df).tolist()
        pie = df_res["ODS"].value_counts().to_dict()
        return JsonResponse({"error":0,"results":df_res.to_dict('records'),"pie":pie})
    return JsonResponse({})

@csrf_exempt
def ajaxCaracteristicas(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        text = text.replace("\\n"," ")        
        p1 = model.steps[0][1].transform(pd.Series([text]))
        p2 = model.steps[1][1].transform(p1)
        tokens = p2[0].split(" ")
        p3 = model.steps[2][1].transform(p2)
        p4 = model.steps[3][1].predict_proba(p3)[0].tolist()
        res = int(model.steps[3][1].predict(model.steps[2][1].transform(p2)))
        proba = {"ODS6":p4[0],"ODS7":p4[1],"ODS16":p4[2]}
        imp = []
        coef = model.steps[3][1].coef_
        tokens_p = {}
        for token in tokens:
            if token not in tokens_p:
                if token in model.steps[2][1].vocabulary_:
                    imp.append({\
                            "Token":token,\
                            "TfIdf":float(p3.getcol(model.steps[2][1].vocabulary_[token]).toarray()[0][0]),\
                            "ODS6":float(coef[0][model.steps[2][1].vocabulary_[token]]),\
                            "ODS7":float(coef[1][model.steps[2][1].vocabulary_[token]]),\
                            "ODS16":float(coef[2][model.steps[2][1].vocabulary_[token]])\
                            })
                tokens_p[token]=1
        return JsonResponse({"error":0,"res":res,"tokenizado":p2[0],"proba":proba,"imp":imp,"tokens":tokens, "dict":pd.DataFrame(imp).to_dict()})
    return JsonResponse({})




