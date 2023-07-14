employers_schema = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "url": {"type": "string"},
                    "alternate_url": {"type": "string"},
                    "logo_urls": {},
                    "vacancies_url": {"type": "string"},
                    "open_vacancies": {"type": "number"},
                },
                "required": [
                    "id",
                    "name",
                    "url",
                    "alternate_url",
                    "logo_urls",
                    "vacancies_url",
                    "open_vacancies",
                ],
            },
        },
        "found": {"type": "number"},
        "pages": {"type": "number"},
        "per_page": {"type": "number"},
        "page": {"type": "number"},
    },
    "required": ["items", "found", "pages", "per_page", "page"],
}
