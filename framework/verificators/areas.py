import jsonschema
from framework.schemas.areas import (
    areas_schema,
    areas_countries_schema,
    areas_specific_schema,
)


class AreasVerificator:
    @staticmethod
    def validate_areas_schema(content: dict):
        jsonschema.validate(content, areas_schema)

    @staticmethod
    def validate_specific_area_schema(content: dict):
        jsonschema.validate(content, areas_specific_schema)

    @staticmethod
    def validate_countries_schema(content: dict):
        jsonschema.validate(content, areas_countries_schema)
