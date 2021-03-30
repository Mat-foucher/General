import numpy as np

A = np.array([[0,0],[1,2],[4,3],[3,1],[5,4],[6,3]])



capacity = 10

table = np.zeros((6,11))

def buildTable(dArray, items, cap):
    for i in np.arange(0,6):
        
        for j in np.arange(0,11):
            if(i == 0 or j == 0):
                dArray[i][j] = 0
            else:
                if j - items[i][0] < 0:
                    dArray[i][j] = dArray[i-1][j]
                if j - items[i][0] >= 0:
                    dArray[i][j] = max(dArray[i-1][j] , items[i][1] + dArray[i-1][j - items[i][0]])
                    
                    #print(dArray[i-1][j] , items[i][1] + dArray[i-1][j - items[i][0]], "j - items[i][0]=",j - items[i][0] )

def printTable(dArray,items):
    visitedColumns = list()
    for i in range(6):
        isPrint = True
        for j in range(11): 
            if( i!=0 and j!=0):
                if(j - items[i][0] >=0):
                    if(isPrint == True and items[i][1] + dArray[i-1][j - items[i][0]] == max(dArray[i-1][j] , items[i][1] + dArray[i-1][j - items[i][0]])):
                        isFound = False
                        for p in range(len(visitedColumns)):
                            if(visitedColumns[p] == j):
                                # Check if column already was visited:
                                isFound = True

                        if(isFound == False):
                            print(items[i], " ",i,j)
                            visitedColumns.append(j)
                        # Ensure no multiple prints on the same line    
                        isPrint = False
        print(" ")


buildTable(table, A, capacity)
printTable(table,A)