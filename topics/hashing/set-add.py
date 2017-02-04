class Set:
  def add(self, item):
    # Hashen
    h = hash(item)

    # Laatste N bits nemen
    i = get_last_bits(h, self.bits)

    # Element toevoegen aan juiste bucket
    self.buckets[i].append(item)
