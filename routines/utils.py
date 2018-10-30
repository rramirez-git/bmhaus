from django.conf import settings

from os import path, mkdir


def print_error(message, level="Warning"):
    """
    Imprime un mensaje como valor de error.

    (string/var) message                mensaje / var a mostrar
        (string) level      = Warning   string del nivel a mostrar

    return None
    """
    print("=======================", level, message)


def print_list(lista):
    """
    Imprime una lista de valores junto con el indice correspondiente.

    return None
    """
    for indice, elemento in enumerate(lista):
        print("{:04d}: {}".format(indice, elemento))


def requires_jquery_ui(request):
    """
    Indica si el navegador del usuario requiere el uso de jQueryUI basado
    en el USER_AGENT del navegador.

    (request) request   Objeto request sobre el que se realizará la
                            verificación.

    return boolean
    """
    ua = request.META["HTTP_USER_AGENT"].lower()
    if "chrome" in ua \
            or "chromium" in ua \
            or "edge" in ua \
            or "mobi" in ua \
            or "phone" in ua:
        return False
    return True


def month_name(month):
    """
    Devuelve en cadena de 3 letras el mes.

    Si el numero del mes no esta entre 1 y 12 se devuelve una cadena vacia.

    (int) month mes a convertir

    return string
    """
    if 1 == int(month):
        return "Ene"
    if 2 == int(month):
        return "Feb"
    if 3 == int(month):
        return "Mar"
    if 4 == int(month):
        return "Abr"
    if 5 == int(month):
        return "May"
    if 6 == int(month):
        return "Jun"
    if 7 == int(month):
        return "Jul"
    if 8 == int(month):
        return "Ago"
    if 9 == int(month):
        return "Sep"
    if 10 == int(month):
        return "Oct"
    if 11 == int(month):
        return "Nov"
    if 12 == int(month):
        return "Dic"
    return ""


def clean_name(name, to_lower=True):
    """
    Limpia un nombre para generar un nombre inglés y sustituye los
    espacios por _

    (string) name               nombre a limpiar
    (boolean) to_lower = True   convertir a minusculas

    return string
    """
    name = name.replace(" ", "_")
    name = name.replace("ñ", "n")
    name = name.replace("Ñ", "N")
    name = name.replace("á", "a")
    name = name.replace("Á", "A")
    name = name.replace("é", "e")
    name = name.replace("É", "E")
    name = name.replace("í", "i")
    name = name.replace("Í", "I")
    name = name.replace("ó", "o")
    name = name.replace("Ó", "O")
    name = name.replace("ú", "u")
    name = name.replace("U", "U")
    name = name.replace("ä", "a")
    name = name.replace("Ä", "A")
    name = name.replace("ë", "e")
    name = name.replace("ë", "E")
    name = name.replace("ï", "i")
    name = name.replace("Ï", "I")
    name = name.replace("ö", "o")
    name = name.replace("ö", "O")
    name = name.replace("ü", "u")
    name = name.replace("Ü", "U")
    if to_lower is True:
        name = name.lower()
    return name


def move_uploaded_file(file, upload_to):
    """
    Mueve un archivo a la ruta especificada.

    (UploadedFile) file archivo a mover
    (string) upload_to  path relativo a settings.MEDIA_ROOT donde se
                        almacenará el archivo

    return string
    """
    filename = file.name.replace(" ", "_")
    newfilename = path.join(settings.MEDIA_ROOT, upload_to, filename)
    cont = 0
    if not path.exists(path.join(settings.MEDIA_ROOT, upload_to)):
        mkdir(path.join(settings.MEDIA_ROOT, upload_to))
    while path.isfile(newfilename):
        cont += 1
        fname, fext = path.splitext(filename)
        newfilename = path.join(
            settings.MEDIA_ROOT,
            upload_to,
            "{}_{:04d}{}".format(fname, cont, fext))
    with open(newfilename, 'wb+') as archivo:
        try:
            for chunk in file.chunks:
                archivo.write(chunk)
        except:
            archivo.write(file.read())
    return path.join(upload_to, path.basename(newfilename))