import os, re

from basefilter import BaseFilter
from lib.backend import debug, warning, critical, run_cmd

class AuthorFilter(BaseFilter):
    """"
    Match at least one commit for the given author.  Only supports git.
    """

    def __init__(self, src, expr):
        BaseFilter.__init__(self,src)
        self.expr = re.compile(expr)

    def match(self, entry):
        if os.path.isdir(os.path.join(entry, '.git')):
            oldcwd = os.getcwd()
            os.chdir(entry)
            stdout = run_cmd(['git', 'shortlog', '-s'])[0]
            os.chdir(oldcwd)
            if re.search(self.expr, stdout):
                return True
        else:
            warning ("AuthorFilter: no supported VCS found. skipping %s" % entry)
        return False

