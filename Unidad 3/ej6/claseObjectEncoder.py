import json
from pathlib import Path
from claseLista import Lista
from claseHeladera import Heladera
from claseLavarropa import Lavarropa
from claseTelevisor import Televisor
from claseAparato import Aparato

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                aparatos=d['aparatos']
                dAparato = aparatos[0]
                lista=class_()
                for i in range(len(aparatos)):
                    dAparato=aparatos[i]
                    class_name=dAparato.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAparato['__atributos__']
                    unAparato=class_(**atributos)
                    lista.agregarElemento(unAparato)
            return lista
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
