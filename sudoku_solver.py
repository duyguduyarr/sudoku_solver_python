#!/usr/bin/env python
# coding: utf-8

# In[1]:


board =[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def solve(bo):
    find = find_empty(bo)
    #if no empty box then its the solution
    if not find:
        return True 
    else:
        row,col = find #initializing positions
        
    for i in range(1,10):
        #calling valid func, if its valid put them in box
        if valid(bo, i,(row,col)):
            bo[row][col] = i
            #print_board(bo)# Added for debugging
            #recursively solve, güncellenmiş tahtayı eski tahtayla karşılaştırır
            if solve(bo):
                return True
            bo[row][col] = 0
            
    return False #eğer hiçbir sayı işe yaramazsa yani for döngüsünde hiçbir sayıyı koyamadıysak bunu döndürürüz.

def print_board(bo):
    for i in range(len(bo)): #its important that i is length, not values
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(len(bo[0])): #bo[0] means each row, in this example full row
            if j % 3 == 0 and j != 0:
                print("|", end =" ") #no \n needed
            if j == 8:
                print(bo[i][j]) #self \n in printing in python
            else:
                print(str(bo[i][j]) +" ", end="") #we distracted \n of other columns
                
def find_empty(bo):
    for i in range(len(bo)): #checks from 1 to 9
        for j in range(len(bo[0])): #bo[0] means length of each row
            if bo[i][j]==0:
                return (i,j) #return the empty elements position
    return None
def valid(bo,num,pos):
    #checking rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: #if our guess(num) is on the row
            return False
# pos[1]!=i ---> Bunun nedeni biz diğer satırlar için bakıyoruz, boşluk olan satırı zaten kontrol etmemize gerek yok,
#pos[i][j]---> üst satırdaki 1 demek, column demek. Yani target sütunu kontrol edemeyiz çünkü zaten boş
#pos[0]->rows & pos[1]->columns in tuples 

    #checking columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i: #reverse 0 and ones. 
            return False
    #checking boxes with floor division
    box_columns = pos[1] // 3 #finds index number of boxes for columns
    box_rows = pos[0] // 3 #finds index number of boxes for rows
    for i in range(box_rows*3,box_rows*3+3): 
        for j in range(box_columns*3,box_columns*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True

print("Initial Board:")
print_board(board)

# Solve the board
solve(board)
print("____________")
# Solved board
print("\nSolved Board:")
print_board(board)


# In[ ]:





# In[ ]:





# In[ ]:




