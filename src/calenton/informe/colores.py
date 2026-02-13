# definiciones de colores en hexadecimal
# Para utilizar con los graficos del modulo pycha


class miColor():
	_color = {
		'black':	'#000000',	# black
		'silver':	'#C0C0C0',	# ~gray75 (or SystemButtonFace on classic Windows)
		'gray':		'#808080',	# ~gray50
		'white':	'#FFFFFF',	# white
		'maroon':	'#800000',	# ~darkred
		'red':		'#FF0000',	# red
		'purple':	'#800080',	# ~DarkMagenta
		'fuchsia':	'#FF00FF',	# magenta
		'green':	'#008000',	# ~green4
		'lime':		'#00FF00',	# green
		'olive':	'#808000',	# ~Gold4
		'yellow':	'#FFFF00',	# yellow
		'navy':		'#000080',	# navy
		'blue':		'#0000FF',	# blue
		'teal':		'#008080',	# ~turquoise4
		'aqua':		'#00FFFF',	# cyan
		'red1':		'#FA5858', 	# pasteles
		'orange1':	'#FAAC58', 	#
		'yellow1':	'#F4FA58', 	#
		'green1':	'#ACFA58', 	#
		'green11':	'#58FA58', 	#
		'green12':	'#58FAAC', 	#
		'cyan1':	'#58FAF4', 	#
		'blue1':	'#58ACFA', 	#
		'navy1':	'#5858FA', 	#
		'purple1':	'#AC58FA', 	#
		'fuchsia1':	'#FA58F4', 	#
		'rose1':	'#FA58AC', 	#
		'grey1':	'#A4A4A4', 	#
	}
	
	def colorHex(self, nombre):
		return self._color[nombre]
	
	def listaColor(self, nombre, n):
		l = []
		if nombre == 'pastel':
			k = ['red1', 'orange1', 'yellow1', 'green1', 'cyan1', 'green11', 'blue1', 'green12', 'navy1']
		elif nombre == 'lista1':
			k = ['aqua', 'silver', 'lime', 'orange1', 'teal', 'olive', 'yellow1', 'rose1', 'purple']
		elif nombre == 'lista2':
			k = ['black', 'maroon', 'purple', 'green', 'navy', 'red1', 'fuchsia', 'green12']
		for k1 in k:
			l.append(self._color[k1])
		return l[:n]
