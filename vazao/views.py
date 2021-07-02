from django.shortcuts import render
from .models import Timeseriesresults, Timeseriesresultvalues, CvCensorcode, CvQualitycode, Units, Organizations
from django.utils import timezone
import pandas as pd
from django.utils import timezone
import datetime
import hidrocomp
from hidrocomp.series.flow import Flow
import plotly.offline as pyo
import plotly.graph_objs as go
from functools import reduce
import hydro_api
from hydro_api.ana.hidro.serie_temporal import SerieTemporal
#import matplotlib.pyplot as plt

datetime.datetime.now(tz=timezone.utc)

def paginainicial(request):
    context={}
    return render(request, 'index.html',context)

def projeto(request):
    context = {}

    return render(request, 'vazao/base.html', context)

def dados(request):
    flow = Flow(station=['39970000', '39980000'], source='ANA')
    fig, data = flow.gantt(title="Gráfico gantt da bacia hidrográfica do Rio Coruripe, AL")
    pyo.plot(fig, filename="vazao/dados.html")

    return render(request, 'vazao/dados.html')


