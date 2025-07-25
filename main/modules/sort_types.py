class SortType:
    def __init__(self, name, value, sorting):
        self.name = name
        self.value = value
        self.sorting = sorting

    def sort(self): return self.sorting


productSortTypes = {
    'new': SortType('За датою розміщення', 'new', '-addingTime'),
    'a-z': SortType('За назвою (A-Z)', 'a-z', 'name'),
    'z-a': SortType('За назвою (Z-A)', 'z-a', '-name'),
}
