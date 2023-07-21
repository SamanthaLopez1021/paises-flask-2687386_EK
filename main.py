"""Importar flask"""
"""importar render template"""
from flask import Flask,render_template

"""Variable app, toma valor de flask por nombre """
app=Flask(__name__)

@app.route('/hola')
def index():
    return 'hola'

@app.route('/paises')
def paises():
    """ listas en python """
    """ paises=['Colombia','Peru','Argentina','Chile', 'Uruguay', 'Salvador', 'Mexico'],['Vietnam','Israel','Irak','Jerusalen'],['España','Portugal','Francia','Italia'] """
    """     paises=[
        [
        {
            "nombre":"America", 
            "paises":['Colombia','Peru','Argentina','Chile', 'Uruguay', 'Salvador', 'Mexico']
        }
    ],
    [
        {
            "nombre":"Asia", 
            "paises":['Vietnam','Israel','Irak','Jerusalen']
        }

    ],
    [
        {
            "nombre":"Europa", 
            "paises":['España','Portugal','Francia','Italia']
        }

    ]
    ] """
    paises= [
        
            {
                "nombre":"America",
                "paises":[
                     {"nombre":"Colombia",
                     "capital" :"Bogota",
                     "moneda":"peso",
                     "poblacion":"",
                     "superficie":""
                     },
                     {"nombre":"peru",
                      "capital":"lima",
                        "moneda":"sol",
                        "poblacion":"",
                        "superficie":""
                     }
                 ]
            },
            
            {
                "nombre":"Asia",
                "paises":[
                    {
                        "nombre":"china",
                        "capital":"pekin",
                        "moneda":"yen",
                        "poblacion":"",
                        "superficie":""
                    },
                    {
                        "nombre":"Japon",
                        "capital":"tokio",
                        "moneda ": "yen",
                        "poblacion":"",
                        "superficie":""
                    }
                ]
                
            },

            {
                "nombre":"Europa",
                "paises":[
                    {
                        "nombre":"España",
                        "capital":"madrid",
                        "moneda":"euro",
                        "poblacion":"",
                        "superficie":""
                    },
                    {
                        "nombre":"francia",
                        "capital":"paris",
                        "moneda":"euro",
                        "poblacion":"",
                        "superficie":""
                    }
                ]
            }

        ]

    """ variables de conteo para cada continente """
    contadorPaisesAmerica=0
    for pais in paises[0][0]["paises"]:
        contadorPaisesAmerica=contadorPaisesAmerica+1
    print(contadorPaisesAmerica)
    contadorPaisesEuropa=0
    for pais in paises[1][0]["paises"]:
        contadorPaisesEuropa=contadorPaisesEuropa+1
    print(contadorPaisesEuropa)
    contadorPaisesAsia=0
    for pais in paises[2][0]["paises"]:
        contadorPaisesAsia=contadorPaisesAsia+1
    print(contadorPaisesAsia)

    """  longitud_america = len(paises[0][0]["pais"])

    longitud_europa = len(paises[1][0]["pais"])

    longitud_asia = len(paises[2][0]["pais"])

    print(longitud_america)

    print(longitud_europa)

    print(longitud_asia) """

    user='Eimmy y Kevin'
    return render_template('paises_listas.html',user=user, continentes=paises,America=contadorPaisesAmerica,Europa=contadorPaisesEuropa,Asia=contadorPaisesAsia)






