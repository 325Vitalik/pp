create_user_schema = {
	"$schema": "https://json-schema.org/draft/2019-09/schema",
    "type": "object",
    "required": ["first_name", "last_name", "email", "password"],
    "additionalProperties": False,
    "properties": {
        "first_name": {
          "type": "string",
          "maxLength": 1000
        },
        "last_name": {
          "type": "string",
          "maxLength": 1000
        },
        "birthday": {
          "type": "string",
          "format": "date"
        },
        "email": {
          "type": "string",
          "format": "email",
          "maxLength": 365
        },
        "phone_number": {
          "type": "string",
          "pattern": "^([+][0-9]{2})?[0-9]{10}$"
        },
        "password": {
          "type": "string",
          "maxLength": 100,
          "minLength": 8
        }
    }
}