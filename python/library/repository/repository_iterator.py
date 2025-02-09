class RepositoryIterator:
    def __init__(self, items: list) -> None:
        """
        Constructor for RepositoryIterator class
        :param items: list of items to iterate over
        """
        self._items = items
        self._index = 0

    def __iter__(self) -> 'RepositoryIterator':
        """
        Iterator method
        :return: RepositoryIterator object
        """
        return self

    def __next__(self) -> 'object':
        """
        Returns the next item in a sequence
        :raises StopIteration: if there are no more items to iterate over
        :return: the next item in the sequence
        """
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
