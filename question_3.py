def create_door_mat(N, M):
    pattern = [('.|.' * (2*i + 1)).center(M, '-') for i in range(N//2)]
    welcome_line = 'WELCOME'.center(M, '-')
    door_mat = pattern + [welcome_line] + pattern[::-1]
    
    for line in door_mat:
        print(line)

# Define the size of the door mat (N x M)
N = 11
M = 33

create_door_mat(N, M)