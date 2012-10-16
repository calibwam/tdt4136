/* Source: http://rosettacode.org/wiki/Evaluate_binomial_coefficients#C */
#include <limits.h>
#include "binomial.h"

ULONG binomial(ULONG n, ULONG k)
{
    ULONG r = 1, d = n - k;

    /* choose the smaller of k and n - k */
    if (d > k) { k = d; d = n - k; }

    while (n > k) {
        if (r >= UINT_MAX / n) return 0; /* overflown */
        r *= n--;

        /* divide (n - k)! as soon as we can to delay overflows */
        while (d > 1 && !(r % d)) r /= d--;
    }
    return r;
}
