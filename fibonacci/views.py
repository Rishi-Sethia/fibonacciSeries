from django.shortcuts import render
from django.http.response import HttpResponse
import time
# Create your views here.

def getfibo(request):
    return render(request, "details/fibonacci.html" )

def getNth(request, nvalue):

    startTime = time.time()
    fiboList = [0,1]
    queryDict = request.GET
    
    finalDict = {}
    givenNumber = ''
    try:
        for k,v in queryDict.items():
            key = str(k)
            value = int(v)
            finalDict[key] = value
            fiboFinal = "The Fibonacci Series for {}th number is as follows : {} .\n"
            givenNumber = finalDict['nthvalue']
            
            if givenNumber > 0:
                while len(fiboList) < givenNumber:
                    fiboList.append(sum(fiboList[-2:]))
                fiboList = ', '.join([str(i) for i in fiboList[1:]])
            else:
                fiboFinal = "Provide Value Greater than 0!!"
    except:
        fiboFinal = "ERROR : Please Provide a Valid Input!!!"
    
    finalTime = time.time()
    execTime = finalTime - startTime
    fiboList = fiboFinal.format(givenNumber, fiboList) +" Time Taken to Exec Query : {} seconds.".format(execTime)
    
    
    context = { 'fibo' : fiboList }
    return render(request, "details/fibonacci.html", context)
