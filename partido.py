class Partido:
	def __init__(self, idPartido, nombrePartido, fechaInicio, estado, equipos, reloj, finalizado):
		self.idPartido = idPartido
		self.nombrePartido = nombrePartido
		self.fechaInicio = fechaInicio
		self.estado = estado
		self.equipos = equipos
		self.reloj = reloj
		self.finalizado = finalizado
	
	def getEquipoLocal(self):
		for e in self.equipos:
			if e.equipoLocal:
				return e
	
	def getEquipoVisitante(self):
		for e in self.equipos:
			if not e.equipoLocal:
				return e
	
	#Redefinicion de metodo str
	def __str__(self):
		equipoLocal=self.getEquipoLocal()
		equipoVisitante=self.getEquipoVisitante()
		
		# Si el partido esta finalizado mostrar solo el resultado
		if self.finalizado:
			salida=f"#{equipoLocal.nombreCorto} {str(equipoLocal.puntuacion)} - {str(equipoVisitante.puntuacion)} #{equipoVisitante.nombreCorto}"
		# Si el partido aun no ha comenzado no mostrar puntos y mostras fecha inicio
		elif self.estado == "STATUS_SCHEDULED":
			salida=f"{self.fechaInicio} #{equipoLocal.nombreCorto} - #{equipoVisitante.nombreCorto}"
		# En otro caso esta en curso. Mostrar reloj de juego fecha inicio y puntos
		else:
			salida=f"{self.fechaInicio} #{equipoLocal.nombreCorto} {str(equipoLocal.puntuacion)} - {str(equipoVisitante.puntuacion)} #{equipoVisitante.nombreCorto}"
		return salida			
			
	def imprimirTest(self):
		cadena = str(self.fechaInicio) + " " + self.nombrePartido + " " + self.estado + " " + self.equipos[0].nombreCorto + " " + str(self.equipos[0].puntuacion) + " "  + self.equipos[1].nombreCorto + " " + str(self.equipos[1].puntuacion)
		return cadena