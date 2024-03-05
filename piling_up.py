data = [[2], [6], [4,3,2,1,3,4], [3], [1,3,2]]

num_of_tests = data[0][0]

num_of_rows = (num_of_tests * 2) + 1
# starts at 1 because skipping initial test count number


i = 1



while i < num_of_rows - 1:
    
    j = 0
    piled_cube = 0
    
    num_of_cubes = data[i][0]
    cube_list = data[i+1]
    
    # logic
    
    cube_list_original_length = len(cube_list)
    
    while len(cube_list) > 0:
              
        left_most = cube_list[0]
        right_most = cube_list[len(cube_list)-1]
        
        if left_most <= right_most:
            if piled_cube > 0:
                if right_most > piled_cube:
                    print("No")
                    break
            
            piled_cube = cube_list[len(cube_list)-1]
            cube_list.pop(len(cube_list)-1)
        else:
            if piled_cube > 0:
                if left_most > piled_cube:
                    print("No")
                    break
                    
            piled_cube = cube_list[0]
            cube_list.pop(0)
        j += 1
        
        if len(cube_list) == 0:
            print("Yes")
    
    
    i += 2