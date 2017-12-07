from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue


class Heapify(HeapPriorityQueue):
  def __init__(self, contents=()):
    """Crea una nuova PriorityQueue con tuT gli elemenK contents. """
    super().__init__()
    self._data = [self._Item(k, v) for k, v in contents]
    if len(self._data) > 1:
      self._heapify()

  def _heapify(self):
    """Trasforma un array in una heap. """
    start = self._parent(len(self)-1)
    for j in range(start, -1, -1):
      self._downheap(j)