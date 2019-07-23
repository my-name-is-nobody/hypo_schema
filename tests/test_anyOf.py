import unittest

from jsonschema import validate
import json
from hypothesis import given, settings
from hyposchema.hypo_schema import generate_from_schema


EXAMPLE_JSON_SCHEMA= {
    "title": "Example Schema",
    "type": "object",
    "properties": {
                "firstName": {
                    "type": "string"
                },
                "lastName": {
                    'anyOf': [
                        {"type": "string"},
                        {'type': 'number'}
                    ]
                },
                "age": {
                    "description": "Age in years",
                    "type": "integer",
                    "minimum": 0
                },
                "listOfElements": {
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                },
                "listOfRandom": {
                    "min": 4,
                    "max": 10,
                    "type": "array"
                },
                "type": {
                    "type": "string",
                    "enum": ["string", "int", "bool"]
                },
                "nestedMap": {
                    "type": "object",
                    "properties": {
                        "firstProp": {
                            "type": "string"
                        }
                    },
                    "required": ["firstProp"]
                }
            },
            "required": ["firstName", "lastName", "nestedMap", "listOfElements"]
}




@given(generate_from_schema(EXAMPLE_JSON_SCHEMA))
@settings(max_examples=10)
def test_basic_map( example_data):
    print(json.dumps(example_data, indent=4))
    validate(example_data, EXAMPLE_JSON_SCHEMA)

