mist.ansible
============

Ansible module for mist.io service

Installation
============
Requires `mist.client` package

```pip install mist.client```

```
cd path/to/toplevel/directory/where/your/playbooks/are
mkdir library
git clone https://github.com/mistio/mist.ansible
```

Simple Example of Provisioning
==============================
```
---
- name: Provisioning playbook for digitalocean
  hosts: localhost
  tasks:
  - name: nephoscale is present
    mist_backends:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      provider: digitalocean
      state: present
      backend_key: digital_client_id
      backend_secret: digital_secret_key
      name: DigitalBackend
  - name: Create Machine
    mist:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      backend: DigitalBackend
      key: UploadedKey
      location_id: id_of_chosen_location
      size_id: id_of_machine_size
      image_id: id_of_image
      name: digimachine
```

Full Example Playbook
=====================
