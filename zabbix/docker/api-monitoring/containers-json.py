#!/usr/bin/python3
import os
import json
import re


"""
Returns json containers with URL requests that are running on the host and are in the "services" dictionary
"""

# example api requests
services = {
    'some name': 'http://server/service/v1/test/status',
    'some name': 'http://server/service/v1/test/status',
    }

def json_image_name():
    idme_services_name = []
    format_to_json = []

    with os.popen("docker images --format {{.Repository}}:{{.Tag}}") as file:
        for image_name in file:
            if image_name.strip() in idme_services_name:
                continue
            if '<none>' in image_name.strip():
                idme_services_name.append(''.join(image_name.split(':')[:-1]).strip())
            else:
                idme_services_name.append(image_name.strip())

    idme_services_name = [str(re.search('/.*:', i).group(0)).strip('/:') for i in idme_services_name]

    for image_name in idme_services_name:
        try:
            format_to_json.append({'{#NAME}': image_name, '{#STATUSURL}': services[image_name]})
        except:
            continue

    tmp = {
        'data': format_to_json
    }

    json_data = json.dumps(tmp)
    print(json_data)
    return json_data


if __name__ == '__main__':
    json_image_name()