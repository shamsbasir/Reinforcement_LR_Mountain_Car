from environment import MountainCar
import sys
import random
import numpy as np


def sparse_dot_product(Weight_a,state):
	
	result = 0
	for index in state:
		result += state[index]*Weight_a[index] 
	return result


def next_best_action(Weight, bias, state):
	
	[state_size,action_size] = Weight.shape
	Q = np.zeros(action_size)
	for i in range(action_size):
	        Q[i] = sparse_dot_product(Weight[:,i],state) + bias 
	return np.argmax(Q)


def epsilon_greedy(epsilon,Weights,current_state,bias):

        if random.uniform(0,1) < epsilon:
                action = random.choice([0,1,2])
        else:
                action = next_best_action(Weights,bias,current_state)
        return action

def calculate_gradient(gradient,current_state):
	for index in current_state:
		gradient[index]  = current_state[index]
	return gradient
	
def update_weights(Weights,gamma,alpha,current_state,next_state,action,reward,bias):
	# 0) calculate Q[current_state][action]
	# 1) grab the best_next_action for nex_state 
	# 2) calculate Q[next_state][best_action]
	# 3) TD = reward + gamma * Q[next_state][best_action]
	# 4) TD_delta= TD - Q[state][action]
	# 5) Delta_Weight_action = 
	# 6) Weights[state][action] += alpha * TD_delta * Delta_Weight_action
	[state_size,_]     = Weights.shape
	gradient 	   = np.zeros(state_size)

	Q_current   	   = sparse_dot_product(Weights[:,action],current_state) + bias
	
	best_action 	   = next_best_action(Weights,bias,next_state)	
	Q_next 	    	   = sparse_dot_product(Weights[:,best_action],next_state) + bias 	

	TD 	    	   = reward + gamma * Q_next
	TD_delta    	   = TD - Q_current
	
	gradient 	   = calculate_gradient(gradient, current_state)
	Weights[:,action] += alpha * TD_delta * gradient
	
	bias 		  += alpha * TD_delta

 
	return Weights, bias 

def writeToConsole(cumulative_R,Weights,bias):
	print("<weight_out>")
	print("{}".format(bias))
	[row,col] = Weights.shape
	for i in range(row):
		for j in range(col):
			print("{}".format(Weights[i][j]))



	print("\n<returns_out>")
	for i in range(len(cumulative_R)):
		print("{}".format(cumulative_R[i]))

def writeToFile(weight_out,returns_out,cumulative_R,Weights,bias):
	
	f = open(weight_out,"w")
	f.write("{}\n".format(bias))
	[row,col] = Weights.shape
	for i in range(row):
		for j in range(col):
			f.write("{}\n".format(Weights[i][j]))
	f.close()

	f = open(returns_out,"w")
	for i in range(len(cumulative_R)):
		f.write("{}\n".format(cumulative_R[i]))
	f.close()

	
def main(args):
	# python  q_learning.py raw  weight.out  returns.out  4 200  0.05  0.99  0.01     	
	mode  		= args[1]		
	weight_out	= args[2]
	returns_out	= args[3]
	episodes        = int(args[4])
	maxiterations   = int(args[5])
	epsilon         = float(args[6])
	gamma           = float(args[7])
	alpha 	        = float(args[8])


	
	my_car 		= MountainCar(mode)
	cumulative_R 	= np.zeros(episodes)
	state_size 	= my_car.state_space
	action_size 	= my_car.action_space	
	Weights		= np.zeros([state_size,action_size])
	bias 		= 0
	
	for episode in range(episodes):
		current_state = my_car.reset()
		for step in range(maxiterations):
			
			# take a step
			action = epsilon_greedy(epsilon,Weights,current_state,bias) 
			next_state, reward, done = my_car.step(action)
	
			# update w
			Weights,bias  = update_weights(Weights,gamma,alpha,current_state,next_state,action,reward,bias)	
			current_state = next_state	 
	
			# update statistics 
			cumulative_R[episode] += reward
			if step % 100 == 0:
				my_car.render()
			# render and check if done
			if done:
				break
	
	my_car.close()
	#writeToConsole(cumulative_R,Weights,bias)
	writeToFile(weight_out,returns_out,cumulative_R,Weights,bias)

if __name__ == "__main__":
	main(sys.argv)
