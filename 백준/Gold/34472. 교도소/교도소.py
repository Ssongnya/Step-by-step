N = int(input())
rooms = list(map(int, input().split()))
ppr = sum(rooms)//N
for i in range(N): 
    rooms[i] -= ppr
st, ed, prisoner, tot_move = 0, N-1, 0, 0
while st != ed: 
    if st == N: st = 0
    if prisoner < 0: 
        ed = st-1
        prisoner = 0
        tot_move = 0
    prisoner += rooms[st]
    tot_move += prisoner
    st += 1
print(tot_move)