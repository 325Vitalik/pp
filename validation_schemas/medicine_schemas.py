create_medicine_schema = {
	"$schema": "https://json-schema.org/draft/2019-09/schema",
    "type": "object",
    "additionalProperties": False,
    "required": ["name", "price", "amount"],
    "properties": {
      "name": {
        "type": "string",
        "maxLength": 1000
      },
      "price": {
        "type": "number"
      },
      "amount": {
        "type": "number"
      }
    }
}