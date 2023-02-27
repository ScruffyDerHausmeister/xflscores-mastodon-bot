from relojjuego import *
from equipo import *
from partido import *
from scoreboard import *

# Esta clase traduce el json dd Espn en objetos mediante el metodo generaScoreboard. Si se usara una API diferente necesitaria su propia clase
class RecolectorESPN:
	def __init__(self,datos):
		self.datos = datos
		
	def imprimeInfo(self):
		info=self.datos
		liga=info['leagues'][0]
		print(liga['abbreviation'])
		temporada=info['season']
		print(temporada['year'])
		jornada=info['week']
		print(jornada['number'])
		partidos=info['events']
		for p in partidos:
			print(p['shortName'])

	def esPlayoffs(self,tempTipo):
		playoffs=False
		# TemporadaTipo 3 es PostSeason
		if tempTipo==3:
			playoffs=True

		return playoffs

	def obtenerRondaPlayoffs(self,weekNum):
		switcher = {
			1: 'Wild Card',
			2: 'Divisional Round',
			3: 'Conference Championship',
			4: 'Pro Bowl',
			5: 'Super Bowl'
		}

		return switcher.get(weekNum, "Unknown Round")

	def generaScoreboard(self):
		info=self.datos
		liga=info['leagues'][0]['abbreviation']
		temporada=info['season']['year']
		temporadaTipo=info['season']['type']
		jornada=info['week']['number']

		if self.esPlayoffs(temporadaTipo):
			#print("Estamos en Playoffs")
			jornada=self.obtenerRondaPlayoffs(jornada)
			#print(jornada)
		else:
			print("NO estamos en Playoffs")
		
		#generar partidos
		listaPartidos = []
		for p in info['events']:
			idPartido=p['id']
			nombrePartido=p['shortName']
			#Realmente fecha inicio es el campo shortDetail. Partido sin comenzar muestra fecha inicio. Partido en curso muestra reloj de juego
			fechaInicioPartido=p['status']['type']['shortDetail']
			finalizadoPartido=p['status']['type']['completed']
			estadoPartido=p['status']['type']['name']
			relojPartido=RelojJuego(p['status']['displayClock'],p['status']['period'])
			
			equiposApi=p['competitions'][0]['competitors']
			#print(type(equiposApi))
			
			#Estos equipos hay q convertilos a objeto equipo
			equiposPartido = []
			for e in equiposApi:
				idEquipo=e['id']
				nombreCortoEquipo=e['team']['abbreviation']
				nombreCompletoEquipo=e['team']['displayName']
				puntuacionEquipo=e['score']
				if e['homeAway'] == "home":
					equipoCasa=True
				else:
					equipoCasa=False
				# Generar la lista de los equipos
				equiposPartido.append(Equipo(idEquipo,nombreCortoEquipo,nombreCompletoEquipo,equipoCasa,puntuacionEquipo))
			
			#Con todo listo generar la lista de partidos
			listaPartidos.append(Partido(idPartido,nombrePartido,fechaInicioPartido,estadoPartido,equiposPartido,relojPartido,finalizadoPartido))	
		scoreboardESPN = Scoreboard(liga,temporada,temporadaTipo,jornada,listaPartidos)
			
		return scoreboardESPN
