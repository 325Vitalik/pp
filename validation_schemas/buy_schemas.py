create_buy_schema = {
	"$schema": "https://json-schema.org/draft/2019-09/schema",
    "type": "object",
    "additionalProperties": False,
    "required": ["user_id", "medicine_id", "amount"],
    "properties": {
      "user_id": {
        "type": "string",
        "pattern": "[a-zA-Z0-9]{8}(-[a-zA-Z0-9]{4}){3}-[a-zA-Z0-9]{12}"
      },
      "medicine_id": {
        "type": "string",
        "pattern": "[a-zA-Z0-9]{8}(-[a-zA-Z0-9]{4}){3}-[a-zA-Z0-9]{12}"
      },
      "amount": {
        "type": "number"
      }
    }
}