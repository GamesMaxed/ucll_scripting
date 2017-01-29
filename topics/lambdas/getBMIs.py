def get_b_m_is(people):
    result = []

    for p in people:
        result.append(p.weight / p.height ** 2)

    return result
