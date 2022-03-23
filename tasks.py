from invoke import task
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))

@task
def start(ctx):
    ctx.run(f'cd {dir_path}/src && flask run')

@task
def dev(ctx):
    ctx.run(f'FLASK_APP=src/app.py FLASK_ENV=development flask run')

@task
def robot(ctx):
    ctx.run(f'robot {dir_path}/src/tests')

@task
def lint(ctx):
    ctx.run(f'pylint {dir_path}/src')

@task
def format(ctx):
    ctx.run(f'autopep8 --in-place --recursive {dir_path}/src')