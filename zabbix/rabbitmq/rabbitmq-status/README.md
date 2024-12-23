###### rabbit port 5672
1. Type: zabbix agent
2. Item key: rabbit.port
3. Trigger expression: last(/<template_name or host>/rabbit.port)\<\>\<port\>
***
###### rabbit active connections
1. Type: zabbix agent
2. Item key: rabbit.active.connections
3. Trigger expression: last(/<template_name or host>/rabbit.active.connections)\>\<number of connections\>
***
###### rabbit queue count
1. Type: zabbix agent
2. Item key: rabbit.queue.count
3. Trigger expression: last(/<template_name or host>/rabbit.queue.count) \> \<number of queue\>