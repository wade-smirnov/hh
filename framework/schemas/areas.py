areas_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "parent_id": {},
            "name": {"type": "string"},
            "areas": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "parent_id": {"type": "string"},
                        "name": {"type": "string"},
                        "areas": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string"},
                                    "parent_id": {"type": "string"},
                                    "name": {"type": "string"},
                                    "areas": {"type": "array", "items": {}},
                                },
                                "required": ["id", "parent_id", "name", "areas"],
                            },
                        },
                    },
                    "required": ["id", "parent_id", "name", "areas"],
                },
            },
        },
        "required": ["id", "parent_id", "name", "areas"],
    },
}

areas_countries_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "url": {"type": "string"},
        },
        "required": ["id", "name", "url"],
    },
}

areas_specific_schema = {
    "type": "object",
    "properties": {
        "areas": {"type": "array", "items": {}},
        "id": {"type": "string"},
        "name": {"type": "string"},
        "parent_id": {"type": ["string", "null"]},
    },
    "required": ["areas", "id", "name", "parent_id"],
}

area_additional_case_schema = {
    "type": "object",
    "properties": {
        "areas": {"type": "array", "items": {}},
        "id": {"type": "string"},
        "name": {"type": "string"},
        "name_prepositional": {"type": "string"},
        "parent_id": {"type": ["string", "null"]},
    },
    "required": ["areas", "id", "name", "name_prepositional", "parent_id"],
}
