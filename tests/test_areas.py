from framework.handlers.areas import AreasClient


class TestAreas:
    def test_get_areas(self):
        result = AreasClient.get_areas()

        assert result
        pass