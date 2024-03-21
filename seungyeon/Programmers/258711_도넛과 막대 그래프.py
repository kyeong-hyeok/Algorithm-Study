def solution(edges):
    
    arr_input = [0 for _ in range(1000001)]
    arr_output = [0 for _ in range(1000001)]
    
    big,stick,create,eight = -1,0,-1,0
    
    for a,b in edges:
        big = max(big,a,b)
        arr_output[a] += 1
        arr_input[b] += 1
        
    for i in range(1,big+1):
        if arr_input[i] == 0 and arr_output[i] >= 2:
            create = i
        elif arr_input[i] >= 1 and arr_output[i] == 0:
            stick += 1
        elif arr_input[i] >= 2 and arr_output[i]  == 2:
            eight += 1
            
    doughnut = arr_output[create] - stick - eight
    return [create,doughnut,stick,eight]