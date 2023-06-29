# find_all_solutions

We need to find solutions to the following equations

```
D^k = p_d * (D - p_d (S+D+I) )^(k-1)
```

If we let `D - p_d (S+D+I) = x`, then we get the following:
```
(S+D+I)*D^k = (D - x) * x^(k-1)
=> x^k - D * x^(k-1) + (S+D+I)*D^k = 0
```

So, the polynomial has `k` degrees. Coefficients are: `1, -D, some 0s, (S+D+I)*D^k`.

After solving, we find `p_d` by following:
```
p_d = (D - x)/(S+D+I)
```
