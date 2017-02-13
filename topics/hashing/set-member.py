class Set:
  def contains(self, item):
    h = hash(item)
    i = get_last_bits(h, self.bits)

    # Bucket afgaan
    for x in self.buckets[i]:
      if x == item:
        return True

    return False
