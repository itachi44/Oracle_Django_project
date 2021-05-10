from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cx_Oracle
from django.conf import settings as cfg

# Create your views here.

#page d'accueil
def index(request):
    context={

    }
    return render(request, 'one4all/index.html', context)

def ajax(request):
    result=""
    a = request.POST.get("a")
    #on relie la vue aux données de la BD via cx_Oracle
    try:
        connection=cx_Oracle.connect(
            cfg.DATABASES["default"]['USER'],
            cfg.DATABASES["default"]['PASSWORD'],
            cfg.DATABASES["default"]['NAME'],
            encoding="UTF-8"
        )

    #create a cursor
        with connection.cursor() as cursor:
            refCursor = connection.cursor()
         #creation des variables qui vont contenir les outputs 
            cursor.callproc('getRegisteredClient',[refCursor])

        #appel des procédures
    #on fait un test sur a pour savoir quelle procédure appeler
        if a=="client":
            data=list()
            for row in refCursor:
                data.append(row)
                print(row)
            
        else:
            data="implementation en cours!!!"
    except cx_Oracle.Error as error:
        print(error)
        
    
    #on fait appel à nos procedures sql pour récupérer les résultats
    #puis on injecte les données dans la page, l'API fetch fera la récupération...
    
    return JsonResponse({"result": data})