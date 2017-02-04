class Set:
  def __init__(self):
    self.buckets = create_buckets(8)
    self.bits = 3

  def create_buckets(n):
    return [ [] for _ in range(0, n) ]

