#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bar = {"imie" : "jurek", "nazwisko" : "lepper"}
# # wyswietlenie "jurek" po nazwa_słownika["nazwa_klucza"].
# print bar["imie"]  
# for i in bar:
# 	print i + " - " +bar[i]

# #---------------------------------------------------------
bar = {
	"imie" : "jurek",
	"nazwisko" : "lepper"
	 }

# # tworzymy liste kluczy i wyswietlamy
# lista = bar.keys()
# for i in lista:
# 	print i



#kasujemy jeden z kluczy
del bar["imie"]
print ""

# tworzymy nową listę, tym razem nie ma klucza "imie"
lista = bar.keys()
for i in lista:
	print i