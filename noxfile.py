import nox

@nox.session
def lint(session:nox.Session):
    session.install('black', 'isort')
    session.run('isort', 'playfair/')
    session.run('black', 'playfair/')

@nox.session
def tests(session:nox.Session):
    session.install('pytest')
    session.run('pytests','tests/')

@nox.session
def coverage(session:nox.Session):
    session.install('pytest-cov')
    session.run('pytest', '--cov=lockless', 'tests/')