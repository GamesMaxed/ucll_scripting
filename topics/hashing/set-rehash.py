class Set:
  def add(self, item):
    # ...
    if self.too_many_elts():
      redistribute()

  def redistribute(self):
    buckets = create_buckets( len(self.buckets) * 2 )
    self.bits += 1

    for item in self:
      h = hash(item)
      i = get_last_bits(h, self.bits)
      buckets[i].append(item)

    self.buckets = buckets
