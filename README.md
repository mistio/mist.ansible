mist.ansible
============

Ansible module for mist.io service

Installation
============
```
pip install mist.ansible```

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
```
---
- name: Provisioning playbook for nephoscale
  hosts: localhost
  tasks:
  - name: Ensure NephoScale backend is present
    mist_backends:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      provider: nephoscale
      state: present
      backend_key: nepho_username
      backend_secret: nepho_password
      name: Nepho
  - name: Generate Key and save locally
    mist_keys:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      name: NephoKey
      auto_generate: true
      save_locally: true
      local_save_path: /home/user/.ssh/NephoKey
  - name: Search for Ubuntu images
    mist_images:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      backend: Nepho
      search_term: Ubuntu
    register: images
  - name: List available sizes
    mist_sizes:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      backend: Nepho
    register: sizes
  - name: List available locations
    mist_locations:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      backend: Nepho
    register: locations
  - name: Create Machine
    mist:
      mist_email: yourmist@account.com
      mist_password: yourmistpassword
      backend: Nepho
      key: NephoKey
      location_id: "{{ locations['locations'][0]['id'] }}"
      size_id: "{{ sizes['sizes'][0]['id'] }}"
      image_id: "{{ images['images'][0]['id'] }}"
      name: nephomachine
```
