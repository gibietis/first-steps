#Okay, this isn't working as intended. I'll have to revisit this.
countries = {
    "Latvia" : "LV",
    "Brazil" : "BR"
}

states_country = {
    "LV" : "Vidzeme",
    "LV" : "Kurzeme",
    "LV" : "Latgale",
    "LV" : "Zemgale",
    "LV" : "Pieriiga",
    "LV" : "Riiga",
    "BR" : "São Paulo",
    "BR" : "Santa Catarina",
    "BR" : "Ceará",
    "BR" : "Mato Grosso do Sul",
    "BR" : "Amazonas",
    "BR" : "Distrito Federal"
}

states = {
    "Vidzeme" : "VZ",
    "Kurzeme" : "KZ",
    "Latgale" : "LG",
    "Zemgale" : "ZG",
    "Pieriiga" : "PR",
    "Riiga" : "RI",
    "São Paulo" : "SP",
    "Santa Catarina" : "SC",
    "Ceará" : "CE",
    "Mato Grosso do Sul" : "MS",
    "Amazonas" : "AM",
    "Distrito Federal" : "DF"
}

cities = {
    "ZG" : "Bauska",
    "VZ" : "Ceesis",
    "KZ" : "Ventspils",
    "LG" : "Rezeekne",
    "ZG" : "Jelgava",
    "PR" : "Aadazhi",
    "RI" : "Riiga",
    "SP" : "Presidente Prudente",
    "SC" : "Florianópolis",
    "CE" : "Fortaleza",
    "MS" : "Campo Grande",
    "AM" : "Manaus",
    "DF" : "Brasília",
}

cities["SP"] = "Rio Preto"
cities["SC"] = "Urubici"
cities["CE"] = "Sobral"
cities["MS"] = "Três Lagoas"
cities["AM"] = "Idk lol"
cities["DF"] = "Taguatinga"

print("-" * 20)

print("Latvia has: ", cities[states[countries["Latvia"]]])
print("Brazil has: ", cities[states[countries["Brazil"]]])

print("-" * 20)

for state, abbreviation in list(states.items()):
    print(f"{state} is abbreviated {abbreviation}")

print("-" * 20)

