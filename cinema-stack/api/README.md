# API Movie
## Versions
- v1.0 : movies
- v2.0 : persons
- v2.1 : probes liveness and readyness
- v3.0 : director
- v4.0 : actors

## DB dependency
The API has thr requirements to work with:
- sqlite: included in python
- postgresql: dependency psycopg2-binary

To work with another SGBDR, rebuild image with the right dependency (pymysql, ...)