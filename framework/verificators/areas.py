import jsonschema
from framework.schemas.areas import areas_schema


class AreasVerificator:
    @staticmethod
    def validate_schema(content):
        jsonschema.validate(content, areas_schema)
