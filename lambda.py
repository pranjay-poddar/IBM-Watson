people = [
    {"name":"Pranjay","house":"jabalpur"},
    {"name":"Rohan","house":"delhi"},
    {"name":"Aia","house":"dhanbad"},
    {"name":"nishant","house":"bokaro"}
]

people.sort(key=lambda people:people["house"])

print(people)