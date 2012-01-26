import os, glob
from fnmatch import fnmatch

from basefilter import BaseFilter
from lib.backend import debug, warning, critical

class FnameFilter(BaseFilter):
    """
    Filter by checking whether a file in the repo matches the glob expression.
    """

    def __init__(self, src, expr):
        BaseFilter.__init__(self,src)
        self.expr = expr

    def match(self, entry):
        # first look in current dir and subdirs (breadth-first), but if that doesn't yield anything, do exhaustive depth-first search
        for matched_file in glob.iglob(os.path.join(entry, self.expr)):
            debug ("matched file %s" % matched_file)
            return True
        for matched_file in glob.iglob(os.path.join(entry, '*', self.expr)):
            debug ("matched file %s" % matched_file)
            return True
        for root, subFolders, files in os.walk(entry):
            for fname in files:
                if fnmatch(fname, self.expr):
                    debug ("matched file %s" % fname)
                    return True
