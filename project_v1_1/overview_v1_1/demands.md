### all demands and changes for project v1.1

## VPC/EC2 servers.
- The webserver can no longer be public and should not have a public IP adress
- The webserver should do a regular health check.
- If the health check fails, the webserver should reset.
- The webserver should get a LB so if the usage gets high a new temporary server should be created
    - Product owner says 3 servers should be the max.


## Connection
- If a user HTTP connects to the load balancer the connection has to be automatically upgraded to HTTPS.
- All connections should be protected with TLS 1.2 minimaly.