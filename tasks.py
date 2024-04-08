from invoke import task

#@task
#def start(ctx):
#    ctx.run("python3 src/index.py", pty=True)

@task
def start(ctx):
    ctx.run("cd src && python -m ui.experimental_gui", pty=True)

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