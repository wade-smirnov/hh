import jsonschema
from framework.schemas.employers import (
    employers_schema,
)


class EmployersVerificator:
    @staticmethod
    def validate_employers_schema(data: dict) -> None:
        jsonschema.validate(data, employers_schema)
