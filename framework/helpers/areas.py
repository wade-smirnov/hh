from random import choice


class AreasHelper:
    @staticmethod
    def get_random_area(areas_data: dict) -> dict:
        selected_variant = choice(areas_data)
        if len(selected_variant.get("areas")) > 0:
            return AreasHelper.get_random_area(areas_data=selected_variant.get("areas"))
        else:
            return selected_variant

    @staticmethod
    def get_nonexistent_area_id(areas_data: dict) -> int:
        all_area_ids = AreasHelper.get_all_area_ids(areas_data=areas_data)
        nonexistent_id = max(all_area_ids) + 1000
        return nonexistent_id

    @staticmethod
    def get_all_area_ids(areas_data: dict) -> list[int]:
        ids_list = []
        for element in areas_data:
            if len(element.get("areas")) > 0:
                temp_ids_list = AreasHelper.get_all_area_ids(
                    areas_data=(element.get("areas"))
                )
                ids_list += temp_ids_list + [int(element.get("id"))]
            else:
                ids_list.append(int(element.get("id")))
        return ids_list

    @staticmethod
    def get_area_by_country_name(areas_countries_data: dict, name: str) -> dict:
        for area in areas_countries_data:
            if area.get("name") == name:
                return area
