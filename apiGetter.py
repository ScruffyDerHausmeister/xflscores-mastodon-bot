import requests
import json

class ApiGetter:
	def __init__(self, url, timeout):
		self.url = url
		self.timeout = timeout
		
	def obtenerDatosAPI(self):
		respuesta = requests.get(self.url,timeout=self.timeout)
		#print(peticion.text)
		#print(peticion.status_code)
		#TODO. comprobar status code
		return respuesta.json()