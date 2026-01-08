n=int(input())
sum_of_N_harmonic_terms=0
for i in range(1, n+1):
    sum_of_N_harmonic_terms+=1/i
print(round(sum_of_N_harmonic_terms, 2))