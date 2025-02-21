1. Type: zabbix agent
2. Item key: postgres.active.connections
3. Trigger expression: last(/<template_name or host>/postgres.active.connections)\>\<number of connections\>
***
#### user for monitoring
- CREATE USER monitoring WITH PASSWORD 'monitoring' nosuperuser nocreatedb nocreaterole noinherit login noreplication nobypassrls connection limit 1;
- GRANT pg_read_all_stats TO monitoring;
- PGPASSWORD="monitoring" psql -t -A -h 127.0.0.1 -p 5432 -U monitoring -d eosan_mkv -c "SELECT COUNT(*) FROM pg_stat_activity"