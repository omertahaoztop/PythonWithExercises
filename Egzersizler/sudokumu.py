# -*- coding: utf-8 -*-
def sudoku_mu(sudoku):
    sudoku=[i for x in  sudoku for i in x]
    return sorted(sudoku)==[1,2,3,4,5,6,7,8,9]
           
    
    
    
    
print(sudoku_mu([[1, 5, 2], [8, 9, 8], [3, 5, 6]]))
