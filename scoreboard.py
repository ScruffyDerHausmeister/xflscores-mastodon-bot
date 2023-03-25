class Scoreboard:

	partidosEnCurso=[]
	partidosFin=[]
	partidosSinComenzar=[]

	def __init__(self, liga, temporada, temporadaTipo, jornada, partidos):
		self.liga = liga
		self.temporada = temporada
		self.temporadaTipo = temporadaTipo
		self.jornada = jornada
		self.partidos = partidos

		# generar listas en funcion del eatado
		for ps in self.partidos:
			if ps.finalizado:
				self.partidosFin.append(ps)
			elif ps.estado == "STATUS_SCHEDULED":
			#elif ps.estado != "STATUS_SCHEDULED":
				self.partidosSinComenzar.append(ps)
			else:
				self.partidosEnCurso.append(ps)

	
	# Redefinicion del metodo str
	def __str__(self):
		
		partidosFinStr=""
		partidosSinComenzarStr=""
		partidosEnCursoStr=""
		
		#Imprimir encabezado
		#encabezado=f"#{self.liga} Week {self.jornada} Scores: \n"
		encabezado=self.getEncabezado()
		#tags=f"#nfl #nflfootball #football \n"
		tags=self.getTags()
		
		# Imprimir listas si tienen algun elemento
		
		if len(self.partidosFin) > 0:
		    partidosFinStr=f"Ended games:\n"
		    for pf in self.partidosFin:
		        partidosFinStr=f"{partidosFinStr}{pf}\n"
		        
		if len(self.partidosEnCurso) > 0:
		    partidosEnCursoStr=f"Running games:\n"
		    for pec in self.partidosEnCurso:
		        partidosEnCursoStr=f"{partidosEnCursoStr}{pec}\n"
		        
		if len(self.partidosSinComenzar) > 0:
		    partidosSinComenzarStr=f"Upcoming games:\n"
		    for psc in self.partidosSinComenzar:
		        partidosSinComenzarStr=f"{partidosSinComenzarStr}{psc}\n"	       
		
		#juntar todo para tener la salida
		salida=f"{encabezado}\n{partidosFinStr}{partidosEnCursoStr}{partidosSinComenzarStr} \n{tags}"
		
		# Se usaba para imprimir todos los partidos
		#for p in self.partidos:
			#salida=f"{salida} {p}\n"	
			
		return salida
	
	# Metodo para dividir en trozos el texto de un scoreboard
	def divideScoreboard(self,tam):
		#print("Funcion Divide")
		scorebrdStrList=self.__str__().splitlines(True)
		sumatam=0
		scorebrdStrSalida = []
		strTemp=""
		#print(len(strTemp))
		for s in scorebrdStrList:
		    #print("tratando "+s)
		    if ((sumatam + len(s)) < tam):
		        strTemp += s
		        sumatam = len(strTemp)
		        if s == scorebrdStrList[-1]:
		            scorebrdStrSalida.append(strTemp)		            
		    else:
		        scorebrdStrSalida.append(strTemp)
		        strTemp=f"{s}"
		        sumatam=len(strTemp)
		        if s == scorebrdStrList[-1]:
		            scorebrdStrSalida.append(strTemp)
		#Incluir la ultima lista
		
		return scorebrdStrSalida
		     
	# Metodo para comprobar si hay un partido running
	def hayPartidoEnCurso(self):

		partidoEnCurso=False

		if len(self.partidosEnCurso) > 0:
			partidoEnCurso=True
		
		return partidoEnCurso

	# Metodo para comprobar si hay un partido acabado
	def hayPartidoAcabado(self):
		partidoAcabado=False
		if len(self.partidosFin) > 0:
			partidoAcabado=True
		return partidoAcabado

	# Metodos para obtener encabezado y tags. TemporadaTipo 3 es PostSeason
	def getEncabezado(self):
		if self.temporadaTipo==3:
			encabezado=f"#{self.liga} #Playoffs {self.jornada} scores: \n"
		else:
			encabezado=f"#{self.liga} week {self.jornada} scores: \n"
		return encabezado

	def getTags(self):
		if self.temporadaTipo==3:
			tags=f"#xfl2023 #xflfootball #sport1xfl #xflplayoffs #playoffs #football #xflmastodon\n"	
		else:
			tags=f"#xfl2023 #xflfootball #sport1xfl #football \n"
		return tags

	def necesitaContentWarning(self):
		necesitaCW=False

		if self.hayPartidoEnCurso() or self.hayPartidoAcabado():
			necesitaCW=True

		return necesitaCW

