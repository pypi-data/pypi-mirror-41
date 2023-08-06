# Dat daemon client

This is a Python client for the [dat-daemon](https://github.com/soyuka/dat-daemon). It doesn't run it, but
communicates with it, letting it share data in the background.

RFC for the dat daemon protocol is available [at dat-daemon](https://github.com/soyuka/dat-daemon/blob/73df8bf3c18342566ee79383da3df8e13d46b2f0/packages/protocol/README.md). It is not an official spec of the dat project (yet).

## Installation

```
pip install dat-daemon-pyclient
```

## Usage

```python
from dat_daemon_pyclient import DatDaemonClient

client = DatDaemonClient(url='ws://localhost:8447').run()
dat = await client.add('/path/to/file_or_folder')
```

## API

The client supports the following methods:

- **list**
- **add**
- **remove_list**
- **start**
- **remove**
- **load**
- **watch**
- **mkdir**
- **readdir**
- **rmdir**
- **unlink**
- **info**
- **create_read_stream**
- **create_write_stream**
