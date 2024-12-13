import json

class PersonalData:
    def __init__(self, first_name, last_name, address, postal_code, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.pesel = pesel

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            postal_code=data["postal_code"],
            pesel=data["pesel"]
        )

person = PersonalData("Jan", "Kowalski", "ul. Kwiatowa 15, Warszawa", "00-123", "12345678901")

person_json = person.to_json()
print("JSON representation:")
print(person_json)

loaded_person = PersonalData.from_json(person_json)
print("\nWczytane dane:")
print(f"Imię: {loaded_person.first_name}")
print(f"Nazwisko: {loaded_person.last_name}")
print(f"Adres: {loaded_person.address}")
print(f"Kod pocztowy: {loaded_person.postal_code}")
print(f"PESEL: {loaded_person.pesel}")
