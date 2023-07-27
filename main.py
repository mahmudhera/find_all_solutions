import numpy as np

S, D, I, K1, K2, k, S_smaller_orig = 134587, 68030, 87550, 999980, 1010298, 21, 176591

S_norm = 1.0 * S / (K1 * k)
D_norm = 1.0 * D / (K1 * k)
I_norm = 1.0 * I / (K1 * k - K1)

observed_pd_diff_d = 1.0 - 1.0 * (K2 + k - 1) / (K1 + k - 1)
print(observed_pd_diff_d)

coeffs = [0 for i in range(k+1)]
coeffs[0] = (S_norm + D_norm + I_norm) * D_norm**k
coeffs[-1] = 1
coeffs[-2] = -D_norm

roots = np.polynomial.polynomial.polyroots(coeffs)
p_ds = (D_norm - roots)/(S_norm + D_norm + I_norm)
p_ds = [np.real(p_d) for p_d in p_ds if not np.iscomplex(p_d)]
p_ds.sort()

d_s = [ (D_norm - (S_norm + D_norm) * p_d)/(D_norm - (S_norm + D_norm + I_norm) * p_d) - 1.0 for p_d in p_ds ]
p_ss = [ (S_norm * p_d)/(D_norm) for p_d in p_ds ]

print( f'(d-i)/(s+d+i) = {(D_norm - I_norm)/(S_norm + D_norm + I_norm)}' )

print('---TRY---')
print( 4*k*S_smaller_orig*S_smaller_orig/( K1*(k+1)*S*(k+1) ) )
print('---')

print('Solutions with k degree polynomial:')

all_solutions = list( zip(p_ss, p_ds, d_s) )
for p_s, p_d, d in all_solutions:
    if p_s < 0 or p_d < 0 or d < 0:
        continue
    print(p_s, p_d, d, p_d-d)
    k2 = int(k/2)
    S_smaller = K1*(k2)*(1 - p_s - p_d) ** (k2-1) * p_s * (d + 1.0)**(-k2+1)
    S_norm_est = (1 - p_s - p_d) ** (k-1) * p_s * (d + 1.0)**(-k+1)
    D_norm_est = (1 - p_s - p_d) ** (k-1) * p_d * (d + 1.0)**(-k+1)
    I_norm_est = (1 - p_s - p_d) ** (k) * d * (d + 1.0)**(-k)
    #print(S_norm_est, S_norm)
    #print(D_norm_est, D_norm)
    #print(I_norm_est, I_norm)
    #print(S_smaller, S_smaller_orig)
    print('--------')

print('Solutions with quadratic:')
a = S_norm + D_norm + I_norm
b = I_norm - observed_pd_diff_d * (S_norm + D_norm + I_norm) - D_norm
c = observed_pd_diff_d * D_norm

p_ds = [ (-b + (b*b - 4*a*c)**0.5)/(2*a), (-b - (b*b - 4*a*c)**0.5)/(2*a) ]
print(p_ds)
