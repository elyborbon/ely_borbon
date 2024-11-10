
class Animal:
#atributos de la clase 
    especie = "perro"
    edad = 0 
    
#Crear varios objetos 
perro = Animal ()
perro.especie = "Perro"
perro.edad = " 1 año"

#Atributos de instancia / constructor 

gato = Animal ()
gato.especie = "Gato"
gato.edad = " 3 año"
#acceder al calor de los atributos 
print (perro.especie)
print (gato.especie)
print (Animal.especie )