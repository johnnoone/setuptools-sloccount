from subprocess import Popen, PIPE, CalledProcessError
from pkg_resources import DistributionNotFound

def check_output(args, stdout=None, stderr=None):
    try:
        if stdout is None:
            stdout = PIPE
        return Popen(args, stdout=stdout, stderr=stderr).communicate()[0]
    except OSError as e:
        raise CalledProcessError(*e)

def check_requirement():
    try:
        check_output(['which', 'sloccount'])
    except CalledProcessError:
        raise DistributionNotFound('sloccount')