# API Design Best Practices

Designing robust APIs involves consistency, scalability, and clarity. Follow these principles:

- Use RESTful conventions
- Version your APIs using `/v1/`
- Return proper HTTP status codes
- Document using OpenAPI/Swagger
- Avoid nesting resources too deeply

Example:
```
GET /v1/users/{id}
```

Always keep the consumer in mind.