"""
Paver tasks
"""

from paver.tasks import task, needs
from paver.easy import sh


@task
def project1():
    # Unit tests
    sh('py.test --cov-report term-missing --cov project1/ test/project1/')

    # Syntax
    sh('pylint project1/ test/project1/')


@needs('project1')
@task
def default():
    pass
