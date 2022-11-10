
def lfsr_task_a(state):
    start_state = state
    period = 1
    while True:
        bit = int(state[0], 2) ^ int(state[1], 2) ^ int(state[2], 2) ^ int(state[3], 2)
        state = str(bit) + state[:-1]
        if state == start_state:
            return period
        period += 1
        
def lfsr_task_b(state):
    start_state = state
    period = 1
    while True:
        bit = int(state[0], 2) ^ int(state[3], 2)
        state = str(bit) + state[:-1]
        if state == start_state:
            return period
        period += 1

key1 = "1000"
key2 = "0011"
key3 = "1111"
print(f"a)\nK = {key1}, period = {lfsr_task_a(key1)}\nK = {key2}, period = {lfsr_task_a(key2)}\nK = {key3}, period = {lfsr_task_a(key3)}")

print(f"\nb)\nK = {key1}, period = {lfsr_task_b(key1)}\nK = {key2}, period = {lfsr_task_b(key2)}\nK = {key3}, period = {lfsr_task_b(key3)}")
