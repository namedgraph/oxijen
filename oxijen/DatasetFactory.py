from oxijen import Dataset
from oxijen.impl import DatasetStoreImpl
from pyoxigraph import Store

class DatasetFactory:

    @staticmethod
    def create_dataset(store: Store) -> Dataset:
        return DatasetStoreImpl(store)