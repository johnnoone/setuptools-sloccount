from .utils import check_output
import setuptools, sys

class SloccountCommand(setuptools.Command):

    description = "run clonedigger on all your modules"

    exec_options = [
        ('sloccount-cached', None, 'Do  not  recalculate. Instead, use cached '
                    'results from a previous execution. Without the --cached '
                    'or --append option, sloccount automatically removes the '
                    'data directory and recreates it'),
        ('sloccount-append', None, 'Do not remove previous calculations from '
                    'the data directory; instead, add the analysis to the '
                    'current contents of the data directory'),
        ('sloccount-datadir=', None, '<directory> Store or use cached data in '
                    'the given data directory; default value is "~/.slocdata"'),
        ('sloccount-follow', None, 'Follow symbolic links'),
        ('sloccount-duplicates', None, 'Count all duplicates. Normally, if '
                    'files have equal content (as determined using MD5 hash '
                    'values), only one is counted'),
        ('sloccount-crossdups', None, 'Count duplicates if they occur in '
                    'different portions of the breakdown. Thus, if the top '
                    'directory contains many different projects, and you want '
                    'the duplicates in different projects to count in each '
                    'project, choose this option'),
        ('sloccount-autogen', None, 'Count source code files that appear to '
                    'be automatically generated. Normally these are excluded'),
        ('sloccount-multiproject', None, "The different directories represent "
                    "different projects. Otherwise, it's assumed that all of "
                    "the source code belongs to a single project. This "
                    "doesn't change the total number of files or SLOC values, "
                    "but it does affect the effort and schedule estimates. "
                    "Given this option, effort is computed separately for "
                    "each project (and then summed), and the schedule is the "
                    "estimated schedule of the largest project"),
        ('sloccount-filecount', None, 'Display counts of files instead of SLOC'),
        ('sloccount-wide', None, 'Display in the "wide" (tab-separated) format'),
        ('sloccount-details', None, 'Display details, that is, results for '
                    'every source code file'),
        ('sloccount-effort=', None, 'F E Change the factor and exponent for '
                    'the effort model.  Effort (in person-months) is computed '
                    'as F*(SLOC/1000)^E'),
        ('sloccount-schedule=', None, 'F E Change the factor and exponent for '
                    'the schedule model. Schedule (in months) is computed as '
                    'F*(effort)^E'),
        ('sloccount-personcost=', None, 'Change the average annual salary to '
                    'cost'),
        ('sloccount-overhead=', None, 'Change the overhead value to overhead. '
                    'Estimated cost is computed as effort * personcost * '
                    'overhead'),
        ('sloccount-addlang=', None, 'Add a language not considered by '
                    'default to be a ``language'' to be reported. Currently '
                    'the only legal values for language are "makefile", '
                    '"sql", and "html". These files are not normally included '
                    'in the SLOC counts, although their SLOCs are internally '
                    'calculated and they are shown in the file counts. If you '
                    'want to include more than one such language, do it by '
                    'passing --addlang more than once, e.g., --addlang '
                    'makefile --addlang sql'),
        ('sloccount-addlangall', None, 'Add all languages not normally '
                    'included in final reports'),
    ]

    user_options = exec_options + [
        # ('exclude-files=', None, 'exclude files? .git by default'),
        ('sloccount-output=', None, "write into this file"),
    ]

    boolean_options = [
        'sloccount-cached', 'sloccount-append', 'sloccount-follow',
        'sloccount-duplicates', 'sloccount-crossdups', 'sloccount-autogen',
        'sloccount-multiproject', 'sloccount-filecount', 'sloccount-wide',
        'sloccount-details', 'sloccount-addlangall'
    ]

    def initialize_options(self):
        for longopt, shortopt, desc in self.exec_options:
            setattr(self, longopt.replace('-', '_').rstrip('='), None)
        # self.exclude_files = '.git'
        self.sloccount_output = None

    def finalize_options(self):
        if self.sloccount_output:
            self.sloccount_output = open(self.sloccount_output, 'w')

    def run(self):
        options = []
        for longopt, shortopt, desc in self.exec_options:
            value = getattr(self, longopt.replace('-', '_').rstrip('='))
            realopt = longopt.lstrip('sloccount-').rstrip('=')
            if value == 1 and longopt in self.boolean_options:
                options.append('--{0}'.format(realopt))
            elif value is not None:
                options.append('--{0}={1}'.format(realopt, value))

        check_output(['sloccount'] + options + ["src"],
            stdout=self.sloccount_output, stderr=self.sloccount_output)

