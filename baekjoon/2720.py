N = int(input())

Q = 25
D = 10
Ni = 5
P = 1

for _ in range(N) :
    C = int(input())
    
    Qc = C // Q
    C -= Q*Qc
    
    Dc = C // D
    C -= D*Dc
    
    Nic = C // Ni
    C -= Ni*Nic
    
    print(Qc, Dc, Nic, C)
    