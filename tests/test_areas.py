from framework.handlers.areas import AreasClient
from framework.verificators.areas import AreasVerificator


class TestAreas:
    def test_get_areas(self):
        content = AreasClient.get_areas()
        AreasVerificator.validate_schema(content=content)
        assert content
        pass