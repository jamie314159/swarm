#!/usr/bin/python3

# birds{id:{'pos':[x,y], 'ori':[x,y]}}
pos = 'pos'
ori = 'dir'
X = 0
Y = 1
swarmSize = 1
swarm = {1:{pos:[0,0], ori:[0,0]}}


def updatePos(target):
	target[pos] = [target[pos][X]+target[ori][X], target[pos][Y]+target[ori][Y]]




for target in swarm:
	force = [0,0]

	for neighbor in repulsionZone(target):
		force += target[param[repulsion]] * vector(target, neighbor) * (1/distance(target, neighbor))

	for neighbor in alignmentZone(target):
		force += target[param[alignment]] * neighbor[ori] * (1/distance(target, neighbor))

	for neighbor in attractionZone(target):
		force += target[param[attraction]] * vector(target, neighbor) * (1/distance(target, neighbor))

	dx = force[X]
	dy = force[Y]

	target[ori] = [dx,dy]

