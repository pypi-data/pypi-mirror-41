# Python client for xenvman

This is a Python client library for [xenvman](https://github.com/syhpoon/xenvman).

## Installation

Installing is a simple as running:

```bash
pip install xenvman
```

## Usage

The very first thing to do is to create a client:

```python
import xenvman

cl = xenvman.Client()
```

if `address` argument is not provided, the default `http://localhost:9876`
will be used. Also if shell environment variable `XENV_API_SERVER` is set,
it will be used instead.

Once you have a client, you can create environment:

```python
env = cl.new_env(xenvman.InputEnv(
    "python-test",
    description="Python test!",
    templates=[
        xenvman.Tpl("db/mongo")
    ],
))
```

And that's it! Once `new_env()` returns, you have an environment which you can
start using in your integration tests.

```python
cont = env.get_container("db/mongo", 0, "mongo")

# Get the full mongo url with exposed port
mongo_url = "{}:{}".format(env.external_address(), cont.ports["27017"])
```

Don't forget to terminate your env after you're done:

```python
env.terminate()
```

