from dataclasses import dataclass, asdict
import json

@dataclass
class PersonalData:
    first_name: str
    last_name: str
    address: str
    postal_code: str
    pesel: str

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return PersonalData(**data)

person = PersonalData(
    first_name="Jan",
    last_name="Kowalski",
    address="ul. Przykładowa 10",
    postal_code="00-001",
    pesel="12345678901"
)

json_data = person.to_json()
print("JSON representation:", json_data)

new_person = PersonalData.from_json(json_data)
print("Restored dataclass:", new_person)
