bits sum(bits xs) {
    bits total = 0;

    for (bits i = 0; i < xs.length; ++i)
        total += xs[i];

    return total;
}
