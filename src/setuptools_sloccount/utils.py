from pkg_resources import DistributionNotFound

try:
    from subprocess import check_output
except ImportError:
    # pre2.7 compatibility
    from subprocess import Popen, CalledProcessError
    def check_output(args):
        try:
            return Popen(args).communicate()[0]
        except OSError as e:
            raise CalledProcessError(*e)

def check_requirement():
    try:
        check_output(['which', 'sloccount'])
    except CalledProcessError:
        raise DistributionNotFound('sloccount')