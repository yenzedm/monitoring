1. Discovery rule key: satellite.names
2. Item prototypes key: satellite.name[{#NAME},{#PORT}]
3. Trigger prototypes expression: last(/<template_name>/satellite.name[{#NAME},{#PORT}])=0