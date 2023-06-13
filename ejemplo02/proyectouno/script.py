from administrativo.models import Pais

file_path = 'data/usuario_migrar.csv'

locations = [('Argentina', 'Buenos Aires'),
             ('Perú', 'Lima'),
             ('Colombia', 'Bogotá'),
             ('Venezuela', 'Caracas'),
             ('Uruguar', 'Montivideo')]

for country, capital in locations:
    print(f"The capital of {country} is {capital}.")
    countryEntity = Pais.objects.create()
    countryEntity.nombre = country
    countryEntity.capital = capital
    countryEntity.save()
