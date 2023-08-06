# Dat daemon client

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
