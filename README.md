# Python lab

You need pyenv or python 3.7.7 and poetry installed on your machine

## Execute in project directory:
1. poetry env use {pathToPython}
2. poetry install
3. poetry run server
4.(6)Create .env file in root folder
5.(6)Add variables to this file URL=mysql+pymysql://root:root@localhost:3306/farmacy_db

## Useful commands:
1. Run Virtual Environment: poetry shell
2. Check python version: python --version
3. Check location of python: which python (Windows: where python)
4. [Install poetry](https://python-poetry.org/docs/)
5.(6)Apply migration: alembic upgrade head
6.(6)Add migration: alembic revision --autogenerate -m "{Name}"
