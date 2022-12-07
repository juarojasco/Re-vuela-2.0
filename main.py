from browser import document, window, alert
import random 
from Panda.py import Tickets
print("Importación exitosa")
"CLASES"
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





"VARIABLES"
menu=0
clase=None
mano=None
bodega = None
tiquete = False
tiqueteG = ''
aerolinea = False
aerolineaG = ''
vuelo = False
vueloG = ''
fecha = False
fechaG = 'DD.MM.AAAA'
hora = False
horaG = 'HH:MM'
destino = False
destinoG = 'Ciudad, País'
partida = False
partidaG = 'Ciudad, País'
asiento = False 
asientoG=''
puerta = False 
puertaG = ''
grupo = False
grupoG = ''
precio = False
precioG = ''

def sketch(p): 
    #PRELOAD
    Home = p.loadImage("Menus/Home.png")
    Search = p.loadImage("Menus/SearchMenu.png")
    Sell = p.loadImage("Menus/SellMenu.png")
    Destino = p.loadImage("Menus/MenuDestino.png")
    Fecha = p.loadImage("Menus/MenuFecha.png")
    Partida = p.loadImage("Menus/MenuPartida.png")
    fir = p.loadImage("Botones/FIR.png")
    eco = p.loadImage("Botones/ECO.png")
    eje = p.loadImage("Botones/EJE.png")
    m = p.loadImage("Botones/M.png")
    l = p.loadImage("Botones/L.png")
    NO = p.loadImage("Botones/NO.png")
    no = p.loadImage("Botones/no.png")
    s = p.loadImage("Botones/S.png")
    xl = p.loadImage("Botones/XL.png")
    si = p.loadImage("Botones/SI.png")
    xs = p.loadImage("Botones/XS.png")
  
    def setup():
        p.createCanvas(750, 350)
        p.background(255)
        p.rectMode(p.CENTER)
      
    def draw():
      global menu
      global clase
      global mano
      global bodega
      global tiquete
      global tiqueteG
      global aerolinea
      global aerolineaG
      global vuelo
      global vueloG
      global fecha
      global fechaG
      global hora
      global horaG
      global destino
      global destinoG
      global partida
      global partidaG
      global asiento
      global asientoG
      global puerta
      global puertaG
      global grupo
      global grupoG
      global precio
      global precioG
      
      if menu==0:
        p.image(Home,0,0,750,350)
      elif menu==1:
        p.image(Sell,0,0,750,350);
        #Clase
        if clase==1:
          p.image(fir,477,112,56,28)
        if clase==2:
          p.image(eje,527,112,56,28)
        if clase==3:
          p.image(eco,578,112,56,28)
        #Equipaje mano
        if mano==1:
          p.image(si,477,146,72,36)
        if mano==2:
          p.image(no,551,146,72,36)
        #Equipaje bodega
        if bodega==1:
          p.image(NO,478,178,60,30)
        if bodega==2:
          p.image(xs, 503,178,60,30)
        if bodega==3:
          p.image(s, 527,178,60,30)
        if bodega==4:
          p.image(m, 551,178,60,30)
        if bodega==5:
          p.image(l, 575,178,60,30)
        if bodega==6:
          p.image(xl, 600,178,60,30)
        #Tiquete
        p.textSize(14)
        p.text(tiqueteG,237,98) 
        #Aerolinea
        p.textSize(14)
        p.text(aerolineaG,237,132) 
        #No Vuelo
        p.textSize(14)
        p.text(vueloG,237,166) 
        #Fecha
        p.textSize(14)
        p.text(fechaG,237,199) 
        #Fecha
        p.textSize(14)
        p.text(horaG,237,232)
        #Destino
        p.textSize(14)
        p.text(destinoG,237,266)
        #Partida
        p.textSize(14)
        p.text(partidaG,237,299)
        #asiento
        p.textSize(14)
        p.text(asientoG,488,98)
        #puerta
        p.textSize(14)
        p.text(puertaG,488,232)
        #Grupo
        p.textSize(14)
        p.text(grupoG,488,266)
        #Precio
        p.textSize(14)
        p.text(precioG,488,299)
        
      elif menu==2:
        p.image(Search,0,0,750,350)
      elif menu==3:
        p.image(Destino,0,0,750,350)
      elif menu==4:
        p.image(Partida,0,0,750,350)
      elif menu==5:
        p.image(Fecha,0,0,750,350)
        
    def mousePressed(self):
        print(p.mouseX,p.mouseY)
        global menu
        global clase
        global mano
        global bodega
        global tiquete
        global tiqueteG
        global aerolinea
        global aerolineaG
        global vuelo
        global vueloG
        global fecha
        global fechaG
        global hora
        global horaG
        global destino
        global destinoG
        global partida
        global partidaG
        global asiento
        global asientoG
        global puerta
        global puertaG
        global grupo
        global grupoG
        global precio
        global precioG
      
        #PANTALLA HOME
        if menu==0:
          if p.mouseX>445 and p.mouseX<615:
            if p.mouseY>205 and p.mouseY<275:
              menu=1
          if p.mouseX>135 and p.mouseX<305:
            if p.mouseY>205 and p.mouseY<275:
              menu=2
        #PANTALLA VENTA     
        if menu==1:
          #Home
          if p.mouseX>110 and p.mouseX<136:
            if p.mouseY>15 and p.mouseY<35:
              menu=0
              clase=None
              mano=None
              bodega=None
              tiqueteG=""
              aerolineaG=""
              vueloG=""
              fechaG="DD.MM.AAAA"
              horaG="HH:MM"
              destinoG="Ciudad, País"
              partidaG="Ciudad, País"
              asientoG=""
              puertaG=""
              grupoG=""
              precio=""
              
          #Guardar 
          if p.mouseX>653 and p.mouseX<723:
            if p.mouseY>268 and p.mouseY<306:
              menu=0
              
          #first
          if p.mouseX>476 and p.mouseX<523:
            if p.mouseY>111 and p.mouseY<138:
              clase=1
          #Ejecutive
          if p.mouseX>527 and p.mouseX<574:
            if p.mouseY>111 and p.mouseY<138:
              clase=2
          #Economic
          if p.mouseX>578 and p.mouseX<625:
            if p.mouseY>111 and p.mouseY<138:
              clase=3
          "EQUIPAJE MANO"
          #si
          if p.mouseX>476 and p.mouseX<547:
            if p.mouseY>146 and p.mouseY<172:
              mano=1
          #no
          if p.mouseX>551 and p.mouseX<624:
            if p.mouseY>146 and p.mouseY<172:
              mano=2
          "EQUIPAJE BODEGA"
          #No
          if p.mouseX>478 and p.mouseX<499:
            if p.mouseY>177 and p.mouseY<205:
              bodega=1
          #Xs
          if p.mouseX>503 and p.mouseX<525:
            if p.mouseY>177 and p.mouseY<205:
              bodega=2
          #S
          if p.mouseX>527 and p.mouseX<548:
            if p.mouseY>177 and p.mouseY<205:
              bodega=3
          #M
          if p.mouseX>551 and p.mouseX<572:
            if p.mouseY>177 and p.mouseY<205:
              bodega=4
          #L
          if p.mouseX>575 and p.mouseX<597:
            if p.mouseY>177 and p.mouseY<205:
              bodega=5
          #Xl
          if p.mouseX>600 and p.mouseX<621:
            if p.mouseY>177 and p.mouseY<205:
              bodega=6
          "TIQUETE"
          if p.mouseX>225 and p.mouseX<374:
            if p.mouseY>77 and p.mouseY<105:
              tiquete=True
              aerolinea=False
              vuelo=False
              fecha=False
              hora=False
              destino=False
              partida=False
              asiento=False
              puerta=False
              grupo=False
              precio=False

          "AEROLINEA"
          if p.mouseX>225 and p.mouseX<374:
            if p.mouseY>111 and p.mouseY<139:
              aerolinea=True
              tiquete=False
              vuelo=False
              fecha=False
              hora=False
              destino=False
              partida=False
              asiento=False
              puerta=False
              grupo=False
              precio=False
          
          "NO VUELO"
          if p.mouseX>225 and p.mouseX<374:
            if p.mouseY>146 and p.mouseY<172:
              vuelo=True
              tiquete=False
              aerolinea=False
              fecha=False
              hora=False
              destino=False
              partida=False
              asiento=False
              puerta=False
              grupo=False
              precio=False
              
          "FECHA"
          if p.mouseX>225 and p.mouseX<374:
            if p.mouseY>179 and p.mouseY<204:
              fecha=True
              tiquete=False
              aerolinea=False
              vuelo=False
              hora=False
              destino=False
              partida=False
              asiento=False
              puerta=False
              grupo=False
              precio=False

          "HORA"
          if p.mouseX>225 and p.mouseX<374:
            if p.mouseY>214 and p.mouseY<238:
              hora=True
              tiquete=False
              aerolinea=False
              vuelo=False
              fecha=False
              destino=False
              partida=False
              asiento=False
              puerta=False
              grupo=False
              precio=False
              
          "DESTINO"
          if p.mouseX>225 and p.mouseX<374:
            if p.mouseY>245 and p.mouseY<272:
              destino=True
              tiquete=False
              aerolinea=False
              vuelo=False
              fecha=False
              hora=False
              partida=False
              asiento=False
              puerta=False
              grupo=False
              precio=False
              
          "PARTIDA"
          if p.mouseX>225 and p.mouseX<374:
            if p.mouseY>280 and p.mouseY<306:
              partida=True
              tiquete=False
              aerolinea=False
              vuelo=False
              fecha=False
              hora=False
              destino=False
              asiento=False
              puerta=False
              grupo=False
              precio=False
              
          "ASIENTO"
          if p.mouseX>478 and p.mouseX<623:
            if p.mouseY>77 and p.mouseY<105:
              asiento=True
              tiquete=False
              aerolinea=False
              vuelo=False
              fecha=False
              hora=False
              destino=False
              partida=False
              puerta=False
              grupo=False
              precio=False
              
          "PUERTA"
          if p.mouseX>478 and p.mouseX<623:
            if p.mouseY>214 and p.mouseY<238:
              puerta=True
              tiquete=False
              aerolinea=False
              vuelo=False
              fecha=False
              hora=False
              destino=False
              partida=False
              asiento=False
              grupo=False
              precio=False
              
          "GRUPO"
          if p.mouseX>478 and p.mouseX<623:
            if p.mouseY>245 and p.mouseY<272:
              grupo=True
              tiquete=False
              aerolinea=False
              vuelo=False
              fecha=False
              hora=False
              destino=False
              partida=False
              asiento=False
              puerta=False
              precio=False
              
              
          "PRECIO"
          if p.mouseX>478 and p.mouseX<623:
            if p.mouseY>280 and p.mouseY<306:
              precio=True
              tiquete=False
              aerolinea=False
              vuelo=False
              fecha=False
              hora=False
              destino=False
              partida=False
              asiento=False
              puerta=False
              grupo=False
              
        #PANTALLA BUSCAR 
        if menu==2:
          if p.mouseX>95 and p.mouseX<124:
            if p.mouseY>15 and p.mouseY<40:
              menu=0
          #BUSCAR DESTINO
          if p.mouseX>135 and p.mouseX<285:
            if p.mouseY>185 and p.mouseY<235:
              menu=3
          #BUSCAR PARTIDA
          if p.mouseX>298 and p.mouseX<448:
            if p.mouseY>185 and p.mouseY<235:
              menu=4
          #BUSCAR FECHA
          if p.mouseX>461 and p.mouseX<611:
            if p.mouseY>185 and p.mouseY<235:
              menu=5
            
        if menu == 3:
          if p.mouseX>119 and p.mouseX<142:
            if p.mouseY>11 and p.mouseY<33:
              menu=0 
        if menu == 4:
          if p.mouseX>119 and p.mouseX<142:
            if p.mouseY>11 and p.mouseY<33:
              menu=0  
        if menu == 5:
          if p.mouseX>119 and p.mouseX<142:
            if p.mouseY>11 and p.mouseY<33:
              menu=0 
    

    def keyTyped(self):
      global menu
      global clase
      global mano
      global bodega
      global tiquete
      global tiqueteG
      global aerolinea
      global aerolineaG
      global vuelo
      global vueloG
      global fecha
      global fechaG
      global hora
      global horaG
      global destino
      global destinoG
      global partida
      global partidaG
      global asiento
      global asientoG
      global puerta
      global puertaG
      global grupo
      global grupoG
      global precio
      global precioG
      if tiquete==True:
        letra=p.key
        if len(tiqueteG)<16:
          tiqueteG+=letra
          
      if aerolinea==True:
        letra=p.key
        if len(aerolineaG)<16:
          aerolineaG+=letra
          
      if vuelo==True:
        letra=p.key
        if len(vueloG)<16:
          vueloG+=letra

      if fecha==True:
        letra=p.key
        if len(fechaG)<10:
          fechaG+=letra
          
      if hora==True:
        letra=p.key
        if len(horaG)<5:
          horaG+=letra

      if destino==True:
        letra=p.key
        if len(destinoG)<18:
          destinoG+=letra
          
      if partida==True:
        letra=p.key
        if len(partidaG)<18:
          partidaG+=letra

      if asiento==True:
        letra=p.key
        if len(asientoG)<4:
          asientoG+=letra

      if puerta==True:
        letra=p.key
        if len(puertaG)<3:
          puertaG+=letra
          
      if grupo==True:
        letra=p.key
        if len(grupoG)<2:
          grupoG+=letra

      if precio==True:
        letra=p.key
        if len(precioG)<13:
          precioG+=letra

    def keyPressed(self):
      global menu
      global clase
      global mano
      global bodega
      global tiquete
      global tiqueteG
      global aerolinea
      global aerolineaG
      global vuelo
      global vueloG
      global fecha
      global fechaG
      global hora
      global horaG
      global destino
      global destinoG
      global partida
      global partidaG
      global asiento
      global asientoG
      global puerta
      global puertaG
      global grupo
      global grupoG
      global precio
      global precioG
      if tiquete==True:
        if p.key == "Backspace" and len(tiqueteG)>0:
          tiqueteG = tiqueteG[:-1]
          
      if aerolinea==True:
        if p.key == "Backspace" and len(aerolineaG)>0:
          aerolineaG = aerolineaG[:-1]

      if vuelo==True:
        if p.key == "Backspace" and len(vueloG)>0:
          vueloG = vueloG[:-1]

      if fecha==True:
        if p.key == "Backspace" and len(fechaG)>0:
          fechaG = fechaG[:-1]

      if hora==True:
        if p.key == "Backspace" and len(horaG)>0:
          horaG = horaG[:-1]

      if destino==True:
        if p.key == "Backspace" and len(destinoG)>0:
          destinoG = destinoG[:-1]
          
      if partida==True:
        if p.key == "Backspace" and len(partidaG)>0:
          partidaG = partidaG[:-1]

      if asiento==True:
        if p.key == "Backspace" and len(asientoG)>0:
          asientoG = asientoG[:-1]

      if puerta==True:
        if p.key == "Backspace" and len(puertaG)>0:
          puertaG = puertaG[:-1]
      if grupo==True:
        if p.key == "Backspace" and len(grupoG)>0:
          grupoG = grupoG[:-1]
      if precio==True:
        if p.key == "Backspace" and len(precioG)>0:
          precioG = precioG[:-1]
          
    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyTyped = keyTyped
    p.keyPressed = keyPressed
    
  
      
myp5 = window.p5.new(sketch)


