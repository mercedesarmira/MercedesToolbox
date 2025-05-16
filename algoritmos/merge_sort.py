# Ordenamiento por mezcla

def merge_sort(lista):
    if len(lista) > 1:
        #dividimos la lista en sublistas
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        # recursividad
        merge_sort(izquierda)
        merge_sort(derecha)

        i=j=k=0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] =derecha[j]
                j+=1
            k+=1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1