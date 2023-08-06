[![pipeline status](https://gitlab.com/grautxo/tpyl/badges/master/pipeline.svg)](https://gitlab.com/grautxo/tpyl/commits/master) [![coverage report](https://gitlab.com/grautxo/tpyl/badges/master/coverage.svg)](http://grautxo.pages.grautxo.com/tpyl/)

# TPYL

Simple template CLI using [Jinja2](http://jinja.pocoo.org/docs/).

## Install

Install with pip

~~~bash
pip install tpyl
~~~

Use docker image

~~~bash
docker pull registry.gitlab.com/grautxo/tpyl
docker tag registry.gitlab.com/grautxo/tpyl tpyl
~~~

## Usage

### Simple usage

~~~bash
# Simplest example
echo "{{ foo }}" | tpyl -v foo=bar

# Read a file from stdin
cat my/template.j2 | tpyl -v myvar=myval -v other=val

# Read template from url
tpyl -v myvar=myval http://example.com/my/template.j2

# Write a rendered template to disk
tpyl my/template.j2 -v myvar=myval -v other=val -o rendered-template.html
~~~

### Context

Variables can be defined on different format files (`yaml`/`json`/`toml`/`ini`/`env`/`exec`):

`mycontext.yaml`

~~~yaml
---
myvar: myval
other: val
~~~

`mycontext.json`

~~~json
{
  "myvar": "myval",
  "other": "val"
}
~~~

`mycontext.env`

~~~
myvar=myval
other=val
~~~

Multiple context files are allowed and will be combined:

~~~bash
tpyl -c mycontext.yaml -c mycontext.json -c mycontext.env my/template.j2
~~~

Executable context can also be provided:

`mycontext.py`

~~~python
#!/usr/bin/env python
print('''---
my-var: my-val
foo: bar
''')
~~~

~~~bash
chmod +x mycontext.py
tpyl -c mycontext.py my/template.j2
~~~

Context can also be a url which will be downloaded before rendering the template. It must set the scheme (http/https) explicitly.

### Environment

Environment variables are sent to the template by default. To avoid this behaviour use:

~~~bash
tpyl --no-env
~~~

### Filters

Custom template filters are allowed. Example:

`filters.py`

~~~python
def my_custom_filter(val, num=1):
    return ':'.join([val for _ in range(0, num)])
~~~

~~~bash
echo '{{ foo | my_custom_filter(3) }}' | tpyl -f filters.py -v foo=bar
# bar:bar:bar
~~~

#### Custom filters

A set of custom filters are provided:

`is_truthy`: Returns `True` if the passed value is `True` or the string representation lowercased is one of the following: `true`, `yes`, `1`.

`is_falsy`: Returns `True` if the passed value is `False` or the string representation lowercased is one of the following: `false`, `no`, `0`.


---

## Dev

For local development using virtualenv (debian/ubuntu):

~~~bash
./sys/install.sh
~~~

## Docker image

Build

~~~bash
docker build -t tpyl .
~~~

## Tests

A script is provided to run tests:

~~~bash
# Run tests
./test.sh

# Run specific tests
./test.sh tests.test:TPYLContextTest.test_context_identify_env tests.test:CLITest.test_cli_file_json_ctx_render

# With coverage
./test.sh --cover

# HTML coverage
./test.sh --cover --html

# Exclude tests with attribute "cli"
./test.sh --attr '!cli'

# Tox
tox

# Specific python
tox -e py27
tox -e py36
~~~

Test with docker

~~~bash
# Build image
docker build -t tpyl:test -f Dockerfile.test .

# Run tests
docker run -it --rm tpyl:test ./test.sh
docker run -it --rm tpyl:test tox
~~~

Adding a gitlab runner

~~~bash
NAME="RUNNER-NAME"
TOKEN="CI-TOKEN"
GITLAB="https://gitlab.com/ci"

# Run container
docker run -d --name "${NAME}" \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp/cache:/cache \
  -v /tmp/builds:/builds \
  gitlab/gitlab-runner:alpine

# Register runner
docker exec "${NAME}" \
  gitlab-runner register \
    --non-interactive \
    --url "${GITLAB}" \
    --registration-token "${TOKEN}" \
    --description "${NAME}" \
    --executor docker \
    --docker-image docker \
    --docker-privileged \
    --docker-volumes /var/run/docker.sock:/var/run/docker.sock \
    --docker-volumes /tmp/builds:/builds \
    --docker-cache-dir /tmp/cache
~~~

## Build pypi package

This step will create a `dist` folder with the pypi distributable package.

~~~bash
./sys/build.sh
~~~

## Upload pypi package

Make sure to install requirements-dev.txt

~~~bash
pip install -r requirements-dev.txt
~~~

Test package upload:

~~~bash
rm -rf build
rm -rf dist
./sys/build.sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
~~~

Upload package to pypi:

~~~bash
rm -rf build
rm -rf dist
./sys/build.sh
twine upload dist/*
~~~
