

#pisanie do pliku
plik = open('plik.txt', 'w')
plik.write('Hello world!\n')
plik.write("and another line\n")
plik.close()



#odczytanie wartosci pliku plik.txt na konsole
plik = open('plik.txt')
try:
	tekst = plik.read()
finally:
	plik.close()

print tekst

#wpisanie listy 
lista = ["bla ", "bla ", "yyy "]

plik = open('plik.txt', 'w')
plik.writelines(lista)
plik.close()