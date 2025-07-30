from django.utils.translation import gettext_lazy


class SortType:
    def __init__(self, name, value, sorting):
        self.name = gettext_lazy(name)
        self.value = value
        self.sorting = sorting

    def sort(self): return self.sorting


productSortTypes = {
    'new': SortType('ProductspageSortByDate', 'new', '-addingTime'),
    'a-z': SortType('ProductspageSortByName', 'a-z', 'name'),
    'z-a': SortType('ProductspageSortByMName', 'z-a', '-name'),
}
