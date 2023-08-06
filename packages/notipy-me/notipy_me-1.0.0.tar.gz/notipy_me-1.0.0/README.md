# Notipy
A simple python package to send you and any other receiver an email when a portion of code is done running.

## Setup
Just run:
```bash
pip install notipy_me
```

## Usage example
### Creating the configuration file
Firstly you would have to setup a file, by default called `notipy_me.json`.

I **strongly** advise for you to keep this file out of the repository and generally DO NOT make it public, as it must contain your chosen email password.

Obviously `https` is used.

#### Minimal setup
To receive the notification email to the same address as the sender just write:

```json
{
    "from":{
        "email":"your@email.com",
        "password":"your password here",
        "server":"smtp.yourserver.com"
    }
}
```

With this setup the port used by default is `465`.

#### Full setup
To receive the notification email to the same address as the sender just write:

```json
{
    "from":{
        "email":"your@email.com",
        "password":"your password here",
        "server":"smtp.yourserver.com",
        "port":465
    },
    "to": [
        "receiver1@immabereceiver.com",
        "another_receiver@immabereceiver.com",
        "yet_another_receiver@immabereceiver.com",
    ]
}
```

With this setup the port used by default is `465`.

#### Where should I put the file?
Put in the same directory as the script you plan to run:

```bash
your_script_directory/
    > your_script.py
    > your_config_file.json
```

### A basic example script
In these examples it automatically loads the configuration from the path `"./notipy_me.json"`.

#### Using notipy_me as a context manager

```py
from notipy_me import Notipy

with Notipy():
    foo()
```

#### Using notipy_me as a decorator

```py
from notipy_me import Notipy

@Notipy()
def foo():
    """Do things here..."""

```

### Loading from custom path
#### Using notipy_me as a context manager

```py
from notipy_me import Notipy

with Notipy("./path/to/my/file.json"):
    foo()
```

#### Using notipy_me as a decorator

```py
from notipy_me import Notipy

@Notipy("./path/to/my/file.json")
def foo():
    """Do things here..."""

```

## Known issues
### Gmail
I cannot manage to get gmail to work, but it keeps rising an error logging in with the credentials, even though they are correct. With the other mail providers it works fine.
