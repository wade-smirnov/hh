import jsonschema
from framework.schemas.areas import (
    areas_schema,
    areas_countries_schema,
    areas_specific_schema,
    area_additional_case_schema,
)


class AreasVerificator:
    @staticmethod
    def validate_areas_schema(data: dict):
        jsonschema.validate(data, areas_schema)

    @staticmethod
    def validate_specific_area_schema(data: dict):
        jsonschema.validate(data, areas_specific_schema)

    @staticmethod
    def validate_countries_schema(data: dict):
        jsonschema.validate(data, areas_countries_schema)

    @staticmethod
    def validate_additional_case_schema(data: dict):
        jsonschema.validate(data, area_additional_case_schema)
