1. Type: zabbix agent
2. Item key: nginx.active.connections
3. Trigger expression: last(/<template_name or host>/nginx.active.connections) \> \<number of connections\>
***
# Добавить в конфиг nginx:
    location /nginx_status {
        access_log off;
	    stub_status;
	    allow 127.0.0.1;
	    deny all;
    }
