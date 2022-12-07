'''IMPORTAR LIBRERIAS PARA LEER EXCEL'''
import pandas as pd
import openpyxl
'''CLASES DE ESTRUCTURAS Y TICKETES'''
class Nodes:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkList:
  def __init__(self):
    self.Kopf = None

  def Add(self, dato, position):
    Count = 1
    Current = self.Kopf
    while Count < position - 1 and Current is not None:
      Count += 1
      Current = Current.next
    if position == 1:
      newNodes = Nodes(dato)
      newNodes.next = Current
      self.Kopf = newNodes
    else:
      newNodes = Nodes(dato)
      newNodes.next = Current.next
      Current.next = newNodes

  def Delete(self, position):
    Current = self.Kopf
    last = None
    Count = 1
    while Current.next is not None and Count < position:
      last = Current
      Current = Current.next
      Count += 1
    if Current == self.Kopf:
      self.Kopf = Current.next
      del Current
    else:
      last.next = Current.next
      del Current

  def Len(self):
    Count = 0
    Current = self.Kopf
    while Current is not None:
      Count += 1
      Current = Current.next
    return Count

  def Print(self):
    current = self.Kopf
    i = 0
    while current is not None:
      if i < self.Len() - 1:
        print(current.data, end=" ")
      else:
        print(current.data, end='\n')
      current = current.next
      i += 1

  def Indice(self, position):
    Current = self.Kopf
    count = 0
    while Current is not None:
      count += 1
      if count == position:
        return Current.data
      else:
        Current = Current.next


#Pila
class Stack:

  def __init__(self):
    self.item = []

  def isEmpty(self):
    return self.item == []

  def Add(self, item):
    self.item.append(item)

  def Takeout(self):
    return self.item.pop(0)

  def Indice(self):
    return self.item[0]

  def Len(self):
    return len(self.item)

  def Print(self):
    i = 0
    while i < self.Len():
      if i < self.Len() - 1:
        print(self.item[i], end=' ')
      else:
        print(self.item[i], end='\n')
      i += 1


#Cola
class Queue:

  def __init__(self):
    self.items = []

  def estaVacia(self):
    return self.items == []

  def Add(self, item):
    self.items.append(item)

  def Sacar(self):
    return self.items.pop(0)

  def Acceder(self):
    return self.items[0]

  def Len(self):
    return len(self.items)

  def Print(self):
    i = 0
    while i < self.Len():
      if i < self.Len() - 1:
        print(self.items[i], end=' ')
      else:
        print(self.items[i], end='\n')
      i += 1


#Creación de Tiquetes
class Ticket:

  def __init__(self, numero, aerolinea, numVuelo, fecha, hora, destino, salida,
               asiento, clase, equipajeMano, equipaje, puerta, grupo, precio,
               disponibilidad):
    self.numero = numero
    self.aerolinea = aerolinea
    self.numVuelo = numVuelo
    self.fecha = fecha
    self.hora = hora
    self.destino = destino
    self.salida = salida
    self.asiento = asiento
    self.clase = clase
    self.equipajeMano = None
    self.equipaje = equipaje
    self.puerta = puerta
    self.grupo = grupo
    self.precio = precio
    self.disponibilidad = disponibilidad


#Creación Listas Enlazadas


'''LISTA ENLAZADA DE TICKETES'''
FileUrl = "data/AvailableFlights.xlsx"
DicCol = {
  "No. Ticket": str,
  "Airline": str,
  "No. Vuelo": str,
  "Date": str,
  "Time": str,
  "Destiny": str,
  "Departure Point": str,
  "Seat": str,
  "Class": str,
  "Handluggage": str,
  "Luggage": str,
  "Gate": str,
  "Group": str,
  "Price": str
}
Sheet = 'Hoja1'
Tabla = pd.read_excel(FileUrl, sheet_name=Sheet, dtype=DicCol)
Tickets = LinkList()
historial = Stack()
for i in range(len(Tabla["No. Ticket"])):

  ObjAux = Ticket(Tabla["No. Ticket"][i], Tabla["Airline"][i],
                  Tabla["No. Vuelo"][i], Tabla["Date"][i], Tabla["Time"][i],
                  Tabla["Destiny"][i], Tabla["Departure Point"][i],
                  Tabla["Seat"][i], Tabla["Class"][i], Tabla["Handluggage"][i],
                  Tabla["Luggage"][i], Tabla["Gate"][i], Tabla["Group"][i],
                  Tabla["Price"][i], True)

  Tickets.Add(ObjAux, i + 1)