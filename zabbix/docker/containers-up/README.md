1. Discovery rule key: docker.image_names
2. Item prototypes key: docker.image_name[{#NAME}]
3. Item prototypes name: Docker container is not running with image[{#NAME}]
4. Trigger prototypes expression: last(/<template_name>/docker.image_name[{#NAME}])=0 
5. Trigger protorypes name: Docker container is not running with image [{#NAME}]
