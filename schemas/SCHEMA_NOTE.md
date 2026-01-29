Schema Philosophy

- Schemas are auto-derived from source JSON using pandas.json_normalize.
- Flattening is applied to nested objects.
- High-cardinality nested collections (arrays) are retained as JSON arrays.
- Further normalization into separate datasets can be performed if required
  by analytical use cases.
