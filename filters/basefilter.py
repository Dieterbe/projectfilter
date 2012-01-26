class BaseFilter:
    """
    Base class for filters.
    """

    def __init__(self, src):
        self.src = src

    def __iter__(self):
        """
        Yield item, if it matches the filter
        """
        for entry in self.src:
            if self.match(entry):
                yield entry

    def match(self, entry):
        """
        Check whether entry matches this filter
        When implementing this function, make it return asap to improve performance
        """
        raise NotImplementedError('cannot instantiate base class')
