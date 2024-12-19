###### without scripts

1. Type: zabbix-agent
2. Item prototypes key: idme.services.memory.usage
3. Trigger prototypes expression: last(/<template_name or host>/idme.services.memory.usage) \> \<number of mb\>