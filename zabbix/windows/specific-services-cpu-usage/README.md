1. Discovery rule key: idme.services.cpu.usage
2. Item prototypes key: service.name[{#NAME}]
3. Trigger prototypes expression: last(/<template_name>/service.name[{#NAME}])=10