1. Type: zabbix agent
2. Item key: postgres.active.connections
3. Trigger expression: last(/<template_name or host>/postgres.active.connections)\>\<number of connections\>