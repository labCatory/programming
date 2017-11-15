st = list(input())
stlengh=len(st)
print(st)
for i in range(stlengh-1):
        st.append(st[0])
        del(st[0])
        print(st)
