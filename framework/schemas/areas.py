areas_schema = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "parent_id": {},
      "name": {
        "type": "string"
      },
      "areas": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "parent_id": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "areas": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "parent_id": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "areas": {
                    "type": "array",
                    "items": {}
                  }
                },
                "required": [
                  "id",
                  "parent_id",
                  "name",
                  "areas"
                ]
              }
            }
          },
          "required": [
            "id",
            "parent_id",
            "name",
            "areas"
          ]
        }
      }
    },
    "required": [
      "id",
      "parent_id",
      "name",
      "areas"
    ]
  }
}