###### without scripts

1. Type: zabbix-agent
2. Item prototypes key: memory.total
3. Trigger prototypes expression: last(/<template_name or host>/cpu.total) \> \<number of percent\>