import os

#BÚSQUEDA EN ARCHIVO
#DEFINIENDO EL GRAFO MEDIANTE UN DICCIONARIO DE PYTHON:
#PARA MEJOR COMPRENSION EL VALOR 'Pando': [('p',4), ('j',15), ('Beni',1)],
#INDICA QUE EL VERTICE 'Pando' ES ADYACENTE CON 'P', CON 'J' Y CON 'Beni' 


grafo = {'Pando': [('Beni',448),('El Alto',648)],
         'Beni': [('Pando',448),('Montero',381)],
         'El Alto': [('Pando',648),('La Paz',20),('Quillacollo',364),('Oruro',223)],
         'La Paz': [('El Alto',6)],
         'Oruro': [('El Alto',4),('Sucre',3),('Potosi',12)],
         'Sucre': [('Oruro',8),('Cochabamba',3),('Potosi',3)],
         'Quillacollo': [('El Alto',12),('Cochabamba',12)],
         'Montero': [('Cochabamba',12),('Beni',12),('Warnes',12)],
         'Cochabamba': [('Quillacollo',12),('Montero',12),('Sucre',12),('Sacaba',12)],
         'Warnes': [('Montero',12),('Santa Cruz',12)],
         'Santa Cruz': [('Warnes',12),('Sacaba',12),('La Guardia',12)],
         'Sacaba': [('Cochabamba',12),('Santa Cruz',12)],
         'Potosi': [('Sucre',12),('Oruro',12),('Tarija',12),('Yacuiba',12),('La Guardia',12)],
         'Tarija': [('Potosi',12),('Yacuiba',12)],
         'La Guardia': [('Santa Cruz',12),('Potosi',12)],
         'Yacuiba': [('Potosi',12),('Tarija',12)]

}
#MUESTRA EL GRAFO ANTES DEL RECORRIDO
print("Muestra el grafo antes del recorrido: \n")
for key, lista in grafo.items():
	print(key)
	print(lista)


print("MOSTRANDO CAMINO de pando a cochabamba:")


def busquedaavara(inicio, fin, graph, cola=[], visitados=[]):
    #Agregamos el inicio a la lista de visitados
    if inicio not in visitados:
        print(inicio)
        visitados.append(inicio)
    
    cola=cola+[x for x in graph[inicio] if x[0][0] not in visitados]
    #Se ordena la cola
    cola.sort(key=lambda x:x[1])
 
    if cola[0][0]==fin:
        #Si llegamos al fin, terminamos e imprimimos
        print(cola[0][0])
    else:
        #guardamos el nodo que estamos procesando, el primero de la cola en orden
        procesando=cola[0]
        cola.remove(procesando)
        #procesamos desde el nuevo nodo, es decir, el de mas prioridad, hacia el destino
        busquedaavara(procesando[0], fin, graph, cola, visitados)
#Aqui llamamos al metodo, segun de donde a donde queramos ir
busquedaavara('Beni', 'Tarija', grafo)
os.system("pause")