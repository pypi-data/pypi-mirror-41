# sanic-templates

Templates support for the Python microframework Sanic.


## Installation

`pip install sanic-templates`

## Usage

``` python

## main.py

from sanic_templates import set_templates_env, render_template

env = set_templates_env(filename="main", templates_dir="/templates")
app = Sanic()


@app.route('/')
async def main(request):
    return render_template(env=env, template_name='main')

```
