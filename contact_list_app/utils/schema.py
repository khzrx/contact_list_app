import os
from pathlib import Path
import json
import allure
import jsonschema


root_path = Path(__file__).parent.parent

def load_schema(file_name: str) -> dict:
    schema_path = os.path.join(root_path, 'json_schemas', file_name)

    with open(schema_path, 'r', encoding='utf-8') as file:
        return json.load(file)


@allure.step('Валидация схемы JSON ответа.')
def validate_schema(response, schema_name):
    jsonschema.validate(response.json(), load_schema(schema_name))

