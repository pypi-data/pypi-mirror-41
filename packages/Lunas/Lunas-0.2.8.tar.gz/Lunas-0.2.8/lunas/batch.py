from typing import List, Iterable, Dict, Callable, Any, Tuple

import numpy
from lunas.persistable import Persistable
from lunas.utils import get_state_dict, load_state_dict
from overrides import overrides


class Batch(Persistable):
    def __init__(self, max_size: int, size_fn: Callable[[Any], int] = None):
        super().__init__()
        self._max_size = max_size
        self._size_fn = size_fn
        self._samples: List[Tuple] = []
        self._sort_idx: numpy.ndarray = None
        self._exclusions = ['_size_fn']
        self._data = None

    @property
    def data(self):
        return self._data

    @property
    def samples(self):
        return [sample for sample, size in self._samples]

    @property
    def sizes(self):
        return [size for sample, size in self._samples]

    def pop_all(self):
        samples = self.samples
        self._samples.clear()
        return samples

    def pop(self, idx: int = -1):
        sample, size = self._samples.pop(idx)
        return sample

    def push(self, sample):
        size = 1
        if self._size_fn is not None:
            size = self._size_fn(sample)
        sample = (sample, size)
        self._samples.append(sample)

    def effective_size(self):
        return sum(self.sizes)

    def from_iter(self, sample_iter, size: int = None, raise_when_stopped: bool = False):
        """
        Fills batch from an iterable object. Enables dynamic batch size if size is not None.
        Args:
            sample_iter:
            size:
            raise_when_stopped:

        """
        size = size or self._max_size
        # Approximate
        while self.effective_size() < size:
            try:
                self.push(next(sample_iter))
            except StopIteration as e:
                if raise_when_stopped:
                    raise e
                else:
                    break

    def from_list(self, sample_list: List, size: int = None):
        size = size or self._max_size
        while self.effective_size() < size:
            try:
                self.push(sample_list.pop(0))
            except IndexError:
                break

    def strip_batch_by_size(self, size: int = None):
        """
        Ensure effective batch size is limited.
        Args:
            size:

        Returns:

        """
        size = size or self._max_size
        rv = []
        while self.effective_size() > size and len(self._samples) > 1:
            rv.append(self.pop(-1))
        return rv

    def sort(self, key_fn: Callable[[Any], int]):
        if key_fn is not None:
            keys = numpy.array(list(map(key_fn, self.samples)))
            indices = numpy.argsort(keys)
            self._sort_idx = indices
            indices = list(indices)
            self._samples = [self._samples[i] for i in indices]

    def revert(self, samples: List[Any]):
        if len(samples) != len(self._sort_idx):
            raise RuntimeError(
                f'Number of samples ({len(samples)}) must match '
                f'the number of indices ({len(self._sort_idx)}).'
            )
        indices = numpy.argsort(self._sort_idx)
        indices = list(indices)
        samples = [samples[i] for i in indices]
        return samples

    def process(self, collate_fn):
        self._data = collate_fn(self.samples)

    @overrides
    def state_dict(self) -> Dict:
        return get_state_dict(self, exclusions=self._exclusions)

    @overrides
    def load_state_dict(self, state_dict: Dict) -> None:
        load_state_dict(self, state_dict)


class Cache(Batch, Iterable):
    def __init__(self, max_size: int, size_fn: Callable[[Any], int] = None):
        super().__init__(max_size, size_fn)

    def __next__(self):
        if self._samples:
            return self.pop(0)
        raise StopIteration

    def __iter__(self):
        return self
