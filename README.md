## For run project after generating from this template
copy `config_dist` into `config`
fill config files
install requirements:
```shell
python -m pip install -r requirements.txt
```
run migrations:
```shell
python -m alembic upgrade head
```
run project:
```shell
python -m app
```
