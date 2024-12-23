1. Type: zabbix agent
2. Item key: nginx.active.connections
3. Trigger expression: last(/<template_name or host>/nginx.active.connections) \> \<number of connections\>