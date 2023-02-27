import datetime
from relojjuego import *
from equipo import *
from partido import *
from scoreboard import *
from apiGetter import *
from recolectorESPN import *

reloj = RelojJuego("3:50",1)
print(reloj.tiempo)

equipoVis = Equipo(1,"TEN","Tennessee Titanso",False,10)
print(equipoVis.nombreCompleto)

equipoLocal = Equipo(1,"NE","New England Patriots",True,21)
print(equipoLocal.nombreCompleto)

ahora = datetime.datetime.now()
print(ahora)
print(ahora.strftime("%Y %b %d %H %M"))
cadenita=print(ahora.strftime('%B %d %Y'))
print(str(cadenita))
equipos = (equipoVis, equipoLocal)

partido = Partido(1000,"TEN @ NE",ahora,"SCHEDULED",equipos,reloj,True)
print(partido.equipos)
print(partido.fechaInicio)


reloj2 = RelojJuego("14:44",4)
print(reloj2.tiempo)

equipoVis2 = Equipo(1,"TB","Tampa Bay",False,30)
print(equipoVis2.nombreCompleto)

equipoLocal2 = Equipo(1,"MIA","Miami Dolphins",True,7)
print(equipoLocal2.nombreCompleto)

ahora2 = datetime.datetime.now()
equipos2 = (equipoVis2, equipoLocal2)

partido2 = Partido(1001,"TB @ MIA",ahora2,"SCHEDULED",equipos2,reloj2, False)
print(partido2.equipos)

partidos = [partido, partido2]

scoreboard = Scoreboard("NFL","2022","2",partidos)

print("\n#### Lista de partidos ####\n")
for p in scoreboard.partidos:
	#print(p.nombrePartido)
	print(p)
	#for e in p.equipos:
		#print(e.nombreCorto)
		#print(e.puntuacion)
#La url tiene q ser una variable		