nix
***
1. Change timeout in /etc/zabbix/zabbix_agent2.conf Timeout=15
2. All scripts in /etc/zabbix/scripts do "chmod +x"
3. Add zabbix user to docker group
4. pip install psutil
5. apt install jq
6. systemctl restart zabbix-agent2.service
7. apt install network-tools

win
***
1. Press Win + R, type services.msc, and press Enter.
2. Find Zabbix Agent 2 in the list.
3. Right-click → Properties.
4. A window will open with the following tabs: "General", "Log On", "Recovery", and "Dependencies".
5. Switch to the "Log On" tab.
6. Select "This account" and enter an administrator account.
7. Enter the password and click OK.
8. Restart the service:
    - Go back to the "General" tab.
    - Click "Stop", then "Start".
