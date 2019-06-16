'''
Created on Jun 12, 2019

@author: adnan
'''

def cost_function(numberofTrainingSet, trainingSet, theta0, theta1):
    sum = 0
    
    for i in range(0, numberofTrainingSet):
        sum += pow((hypothesis(theta0, theta1, trainingSet[i][0]) - trainingSet[i][1]), 2)
    # for i loop
    
    return sum/(2*numberofTrainingSet)

# end of cost_function 
        

def hypothesis(theta0, theta1, x): 
    #hθ(x)=θ0 + θ1x
    return theta0 + (theta1 * x)
# end of hypothesis

trainingSet = [[3,4],[2,1],[4,3],[0,1]]
numberofTrainingSet = 4
theta0 = 0
theta1 = 1;
print(cost_function(numberofTrainingSet, trainingSet, theta0, theta1))