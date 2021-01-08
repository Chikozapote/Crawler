from urllib.request import urlopen


url='https://sawy891.wordpress.com'
enlaces=[]

def obteneratri(html_codigo,capa):
    while True:
        url,posf=obtener_enlances(html_codigo)
        if not url:
            break
        if not url in enlaces:
            enlaces.append(url)
            if capa == 1:
                obtener_codigo(url,2)

        html_codigo=html_codigo[posf:]

def obtener_enlances(html_codigo):
    empieza_attri=html_codigo.find(".jpg")
    empieza_texto=html_codigo.find("<img ", empieza_attri)
    final_texto=html_codigo.find(">", empieza_texto+1)
    atri = html_codigo[empieza_texto +1:final_texto]

    empieza_h=atri.find(".jpg")
    empieza_hre=atri.find("<img ", empieza_h)
    final_hre=atri.find(">", empieza_hre + 1)
    href = atri[empieza_hre + 1:final_hre]

    posf=final_texto
    return href,posf


def obtener_codigo(pagina_url,capa):

    try:
        response = urlopen(pagina_url)
        html_codigo = str(response.read())
        obteneratri(html_codigo,capa)

    except Exception as e:
        return set()

def imprimir():
    print("\n\n\n imprimio la wea esa \n")
    for url in enlaces:
        print(url)

obtener_codigo(url,1)
imprimir()





