def dot(vector01,vector02):
  '''
  This function calculates the dot product of the two vectors. This algorithim makes sure the lengths are equal to each other and if they do not equal each other, then the function does not run the code. This takes the lengths of vector01 and vector02 and multiplies each element together and creates a new list. This then takes the list and each element in the list and adds them together and comes up with a single integer.
  '''
  C = [ ]
  #C is an empty list.
  if len(vector01) != len(vector02):
    print('error')
    return None
    #If the lengths of the vectors are not equal to each other, then the algorithim does not compute and returns none.
  for i in range(len(vector01)):
   #For the length of the vector i.
    C.append(vector01[i] * vector02[i])
    #multiplies each element together and creates a list C.
  D = 0
  #A new integer D is made.
  for i in range(len(C)):
    D = D + C[i]
  return D
  #The function then adds the elements in C toghether to get a single integer, D.

def vecSubtraction(vector01,vector02):
  '''
  This function adds to vectors together. This algorithim makes sure the lengths of the vectors are equal to each other. If the vector lengths are not equal to each other, then this function does not compute the outcome. This takes the vectors and subtract each element from the list and creates a single vector.
  '''
  A = [ ]
  #A is an empty list.
  if len(vector01) != len(vector02):
    print('error')
    return None
    #If the lengths of the lists vector01 and vector02 do not equal each other, then this prints an error and returns none.
  for i in range(len(vector01)):
    A.append(vector01[i] - vector02[i])
    #This subtracts the lengths of vector01 and vector02 and adds each element of the list together.
  return A
  #This returns the list A.

def scalarMultVec(scalar,vector):
  '''
  This function takes a scalar and a vector and multiplies them together to create a single vector. If the scalar is equal to a list, the function does not run and computes and error. This takes the scalar and multiplies each element in the vector. This function 
  then creates a new vector.
  '''
  if type(scalar) != int and type(scalar) != float and type(scalar) != complex:
    print('error')
    return None
    #If the scalar is a list, then the algorithim will print error and return none.
  A = [ ]
  #A is an empty list.
  for i in range(len(vector)):
    #For the length of the vector.
    A.append(vector[i] * scalar)
    #For each element in length i, multiply by the scalar.
  return A
  #This creates a new list for A and returns A.

def norm2(vector):
  '''
  This function calculates the two norm. The result is the norm of the vector. This takes the absolute value of every element and squares them. This adds the result of the after each element is squared. Then, the function takes the square root of the result to return
  the two norm.
  '''
  result = 0
  for i in range(len(vector)):
    result = result +abs(vector[i])**2
    #Takes each element and squares the element and adds them together.
  result = result**.5
  #This takes the result and raises it to the half power, which is equivalent to a square root.
  return result

def modGramSchmidt(A):
  n = len(A)
  m = len(A[0])
  r = [[0]*n for row in range(n)]
  q = [ ]
  for i in range(n):
    r[i][i] = norm2(A[i])
    scalar = 1/r[i][i]
    qi = scalarMultVec(scalar,A[i])
    q.append(qi)
    for j in range(i + 1,n):
      r[i][j] = dot(q[i],A[j])
      B = scalarMultVec(r[i][j],q[i])
      A[j] = vecSubtraction(A[j],B)
  return q, r

A = [[1,0,1],[2,1,0]]
q, r = modGramSchmidt(A)
print(q)
print(r)
