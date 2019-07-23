
import skema
from jsonschema import validate
import json
from hypothesis import given, settings
from hyposchema.hypo_schema import generate_from_schema


EXAMPLE_JSON_SCHEMA=skema.to_jsonschema("""
Root:
    a: Int
    b: Str
    c:
        x: Any
        y: Str | Int
""", resolve=True)




@given(generate_from_schema(EXAMPLE_JSON_SCHEMA))
@settings(max_examples=10)
def test_basic_map( example_data):
    print(json.dumps(example_data, indent=4))
    validate(example_data, EXAMPLE_JSON_SCHEMA)

