from random import randint
import sys

def generate_start_state(k):
    state = [0]*k
    for i,_ in enumerate(state):
        state[i] = randint(0,k-1)
    return state

def get_hits(col, row, k, state):
    hits = 0
    for i in range(k):
        if i == row:
            continue
        if state[i] == row:
            hits += 1
        elif state[i] == i - row + col:
            hits += 1
        elif state[i] == -i + col + row :
            hits += 1
    return hits

def generate_num_conflicts(state, k, row):
    num_conflicts = [0]*k
    current_queen = state[row]
    for i in range(k):
        num_conflicts[i] = get_hits(state[i], i,k, state)

    return num_conflicts

def is_solution(state, k):
    for i in range(k):
        for j in range(k):
            if get_hits(i,j,k,state):
                return False
    return True


def main(k):
    state = generate_start_state(k)
    current_row = 0
    state = [7,0,3,2,3,0,7,2]
    counter = 0
    while not is_solution(state,k):
        num_conflicts = generate_num_conflicts(state, k, current_row)
        print(state)
        print(num_conflicts)
        break
        lowest = k+1
        lowest_index = 0
        for i,n in enumerate(num_conflicts):
            if n < lowest:
                lowest = n
                lowest_index = i
        state[current_row] = lowest_index
        current_row = randint(0,k-1)

        print(state)
        print(num_conflicts)
        """
        counter += 1
        if counter > 5:
            break
        """


main(8)
