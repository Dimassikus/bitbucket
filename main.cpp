double my_pow(double base, unsigned int exp) {
    double result = 1.0;
    for (unsigned int i = 0; i < exp; ++i) {
        result *= base;
    }
    return result;
}
