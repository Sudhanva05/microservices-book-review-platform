## Architecture Overview

This project follows a microservices architecture where each service is responsible for a single domain.

- API Gateway acts as the entry point.
- Each service has its own database.
- Services communicate over HTTP.
- Authentication is centralized.

This design improves scalability, maintainability, and fault isolation.
