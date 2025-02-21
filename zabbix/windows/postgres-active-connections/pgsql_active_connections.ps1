$env:PGPASSWORD="monitoring"
$result = & "C:\RECFACES\AUX_APP\SRV\pgsql\bin\psql.exe" -t -A -h 127.0.0.1 -p 5432 -U monitoring -d eosan_mkv -c "SELECT COUNT(*) FROM pg_stat_activity"
$result -replace '\D', '' | Out-Host