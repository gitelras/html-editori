from invoke import task

@task
def start(ctx):
    ctx.run("cd src && python -m ui.gui", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task(coverage_report)
def show_report(ctx):
    ctx.run("open htmlcov/index.html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)
