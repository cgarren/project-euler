max_chain = 0
max_num = 0
for i in range(1, 1000000):
    current_num = i
    chain = [i]
    while i != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = 3*i + 1
        chain.append(i)
        #print(current_num, len(chain))
    if len(chain) > max_chain:
        max_chain = len(chain)
        max_num = current_num
print(max_num, "Chain Lenth:", max_chain)
