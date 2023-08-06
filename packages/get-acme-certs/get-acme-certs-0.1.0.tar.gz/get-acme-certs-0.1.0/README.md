# get-acme-certs

Quick and dirty script to pull fullchain and privkey certs from the traefik acme.json file.
Inspiration from https://gist.github.com/JayH5/f9e4dc48635f3faa63c52813ff6d115f

Tested in Python 3 only

## Usage

```bash
python get_acme_certs.py /path/to/acme.json myawesomesite.com /path/to/store/certs
```

```
python get_acme_certs.py -h
usage: get_acme_certs.py [-h] acme_json domain dest_dir

Grab a certificate out of Traefik's acme.json file

positional arguments:
  acme_json   path to the acme.json file
  domain      domain to get certificate for
  dest_dir    path to the directory to store the certificate

optional arguments:
  -h, --help  show this help message and exit
```