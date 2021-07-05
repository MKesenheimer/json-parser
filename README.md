# JSON-Parser
Extract a JSON object from a JSON string directly on the command line.

## Example usage
```
$ json-parser -o "object" file.json

$ json-parser -o "address" -f person.json

$ json-parser -o "address.appartment.note" -j '{"name": "Bob", "languages": ["English", "Fench"], "address": {"street": "Cross", "number": "1", "appartment": {"note": "south", "position": "10"}}}'
```
