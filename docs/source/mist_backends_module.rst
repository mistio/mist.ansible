mist_backends - Manage backends in the mist.io service
++++++++++++++++++++++++++++++++++++++++++++++++++++++

:Author: Mist.io Inc

.. contents::
   :local:
   :depth: 1

Synopsis
--------

.. versionadded:: 1.7.1

Manage multi-cloud backends through mist.io service.
You can add/remove multiple backends from multiple providers through mist.io service.
Before you can provision, monitor etc machines through mist.io, you have to first add a backend to the mist.io service.
Mist.io supports
EC2,
Rackspace,
Openstack,
Linode,
Google Compute Engine,
SoftLayer,
Digital Ocean,
Nephoscale,
Bare metal servers,
Docker containers,
HP Cloud.
*mist_email* and *mist_password* can be skipped if *~/.mist* config file is present.
See mist.client documentation for config file http://mistclient.readthedocs.org/en/latest/cmd/cmd.html

Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
            <tr>
    <td>api_url</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>APIURL needed by Openstack and HP Cloud</td>
    </tr>
            <tr>
    <td>backend</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Can be either he backend's name or id. To be used when listing info for backends.</td>
    </tr>
            <tr>
    <td>backend_key</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>This is either the username, api_key etc, depending on the provider</td>
    </tr>
            <tr>
    <td>backend_secret</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>This is either the password, api_secret token etc, depending on the provider. For Linode and DigitalOcean only this one is needed.</td>
    </tr>
            <tr>
    <td>compute_endpoint</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Needed by some OpenStack installations</td>
    </tr>
            <tr>
    <td>machine_ip</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Ip address needed when adding Bare Metal Server</td>
    </tr>
            <tr>
    <td>machine_key</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Id of ssh key needed when adding Bare Metal Server. The key must have been added first to the mist.io service</td>
    </tr>
            <tr>
    <td>machine_port</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Used when adding a Bare Metal Server</td>
    </tr>
            <tr>
    <td>machine_user</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>User for Bare Metal Server</td>
    </tr>
            <tr>
    <td>mist_email</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Email to login to the mist.io service</td>
    </tr>
            <tr>
    <td>mist_password</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Password to login to the mist.io service</td>
    </tr>
            <tr>
    <td>mist_uri</td>
    <td>no</td>
    <td>https://mist.io</td>
        <td><ul></ul></td>
        <td>Url of the mist.io service. By default https://mist.io. But if you have a custom installation of mist.io you can provide the url here</td>
    </tr>
            <tr>
    <td>name</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>The title you want the backend to have</td>
    </tr>
            <tr>
    <td>provider</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Provider id for the backend you want to add to mist.io. You can see all the providers ids using the <span class='module'>mist_providers</span> module.</td>
    </tr>
            <tr>
    <td>region</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>Necessary only if there is a custom Openstack region</td>
    </tr>
            <tr>
    <td>state</td>
    <td>no</td>
    <td></td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td>If provided it will instruct the module to trigger backend actions, otherwise it will only list information</td>
    </tr>
            <tr>
    <td>tenant_name</td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td>In case of Openstack backend, it may have to be provided</td>
    </tr>
        </table>


.. note:: Requires mist.client


Examples
--------

.. raw:: html

    <br/>


::

    - name: Add NepshoScale backend
      mist_backends:
        mist_email: your@email.com
        mist_password: yourpassword
        name: NephoScale
        provider: nephoscale
        backend_key: 908dfjokjkma0hgj9809uj
        backend_secret: kjhf98y9lkj0909kj90
        state: present
    
    - name: List information about DigitalOcean backend
      mist_backends:
        mist_email: your@email.com
        mist_password: yourpassword
        backend: DigitalOcean
      register: backend

