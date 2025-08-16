from clases.animales import*

animales = Animal("Max", 12.5, "Camilo", "2020-03-15", "2025-07-20")

print("Nombre:", animales.get_nombre())
print("Peso:", animales.get_peso())
print("Propietario:", animales.get_propietario())
print("Fecha de cumpleaños:", animales.get_fecha_cumpleaños())
print("Fecha última vacuna:", animales.get_fecha_ultima_vacuna())

animales.set_peso(13.2)
print("Nuevo peso:", animales.get_peso())
