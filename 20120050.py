T = int(input())

for t in range(0,T) :

    RA = input().split()
    RA = [int(ra) for ra in RA]
    Ra = []
    RB = input().split()
    RB = [int(rb) for rb in RB]
    Rb = []
    RC = input().split()
    RC = [int(rc) for rc in RC]
    Rc = [RC[2]]
    RD = input().split()
    RD = [int(rd) for rd in RD]
    Rd = []
    RE = input().split()
    RE = [int(re) for re in RE]
    Re = []

    CA = [RA[0],RB[0],RC[0],RD[0],RE[0]]
    Ca = []
    CB = [RA[1],RB[1],RC[1],RD[1],RE[1]]
    Cb = []
    CC = [RA[2],RB[2],RC[2],RD[2],RE[2]]
    Cc = [RC[2]]
    CD = [RA[3],RB[3],RC[3],RD[3],RE[3]]
    Cd = []
    CE = [RA[4],RB[4],RC[4],RD[4],RE[4]]
    Ce = []

    DA = [RA[0],RB[1],RC[2],RD[3],RE[4]]
    Da = [RC[2]]
    DB = [RA[4],RB[3],RC[2],RD[1],RE[0]]
    Db = [RC[2]]
    VA = [RA[0],RA[4],RC[2],RE[0],RE[4]]
    Va = [RC[2]]

    BINGO = input().split()
    BINGO = [int(bingo) for bingo in BINGO]
    b = len(BINGO)
    A = []
    C = 0

    for i in range(0,b) :
        A.append(BINGO[i])

        for j in range(0,5) :

            if BINGO[i] == RA[j] :
                if Ra.count(BINGO[i])==1 :
                    Ra.remove(BINGO[i])
                Ra.append(BINGO[i])
                if len(RA) == len(Ra) :
                    if C == 0 :
                        C = len(A)
                        break
                    
            if BINGO[i] == RB[j] :
                if Rb.count(BINGO[i])==1 :
                    Rb.remove(BINGO[i])
                Rb.append(BINGO[i])
                if len(RB) == len(Rb) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == RC[j] :
                if Rc.count(BINGO[i])==1 :
                    Rc.remove(BINGO[i])
                Rc.append(BINGO[i])
                if len(RC) == len(Rc) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == RD[j] :
                if Rd.count(BINGO[i])==1 :
                    Rd.remove(BINGO[i])
                Rd.append(BINGO[i])
                if len(RD) == len(Rd) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == RE[j] :
                if Re.count(BINGO[i])==1 :
                    Re.remove(BINGO[i])
                Re.append(BINGO[i])
                if len(RE) == len(Re) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == CA[j] :
                if Ca.count(BINGO[i])==1 :
                    Ca.remove(BINGO[i])
                Ca.append(BINGO[i])
                if len(CA) == len(Ca) :
                    if C == 0 :
                        C = len(A)
                        break
                
            if BINGO[i] == CB[j] :
                if Cb.count(BINGO[i])==1 :
                    Cb.remove(BINGO[i])
                Cb.append(BINGO[i])
                if len(CB) == len(Cb) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == CC[j] :
                if Cc.count(BINGO[i])==1 :
                    Cc.remove(BINGO[i])
                Cc.append(BINGO[i])
                if len(CC) == len(Cc) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == CD[j] :
                if Cd.count(BINGO[i])==1 :
                    Cd.remove(BINGO[i])
                Cd.append(BINGO[i])
                if len(CD) == len(Cd) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == CE[j] :
                if Ce.count(BINGO[i])==1 :
                    Ce.remove(BINGO[i])
                Ce.append(BINGO[i])
                if len(CE) == len(Ce) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == DA[j] :
                if Da.count(BINGO[i])==1 :
                    Da.remove(BINGO[i])
                Da.append(BINGO[i])
                if len(DA) == len(Da) :
                    if C == 0 :
                        C = len(A)
                        break

            if BINGO[i] == DB[j] :
                if Db.count(BINGO[i])==1 :
                    Db.remove(BINGO[i])
                Db.append(BINGO[i])
                if len(DB) == len(Db) :
                    if C == 0 :
                        C = len(A)
                        break
                    
            if BINGO[i] == VA[j] :
                if Va.count(BINGO[i])==1 :
                    Va.remove(BINGO[i])
                Va.append(BINGO[i])
                if len(VA) == len(Va) :
                    if C == 0 :
                        C = len(A)
                        break

    print(C)
