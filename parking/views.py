# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import ast
import checkcp

@csrf_exempt
def request_msg(request):

    if request.method == 'GET':
        data = request.GET
        print '_'*20+'\n'
        print data
        print '_'*20+'\n'
        print 'get request'

    elif request.method == 'POST':
        data = request.POST
        print '_'*20+'\n'
        print data
        print '_'*20+'\n'
        print 'post request'
    else:
        print 'no request'


    myDict = dict(data.iterlists())

    
    print myDict

    newd = {}
    for x in myDict:
        newd[str(x)] = float(myDict[x][0])

    print newd


    lots = checkcp.fiveLots()
    result = lots.nearestLots(lat=newd['lat'], lon=newd['lon'])


##    mc.on_chat_message(newd)



    return JsonResponse(result)
