#---------------------------------#
#------- USEFUL EXECUTABLES ------#
#---------------------------------#

#------ /utils/ ------#


#--- ALL MODULES IN THIS DOCUMENT:

# countlinks(FILE)          Gives the number of nodes, links and modules
# getgiant(NET_FILE)        Calculate the biggest node and get the largest weakly connected set
# lapspec(NET_FILE)         Calculate the Laplacian spectrum

# modularbipart(NUMBER_OF_MODULES, MODULE_SIZE, NUMBER_OF_TEAM, TEAM_SIZE, TEAM_HOMOGENEITY, SEED)
#       Create a binet.net file according to parameters i.e. bipartite network with these parameters

# multinetlayout(NET_FILE1, NET_FILE2)
#       Layout the sum network, and print the node coordinates (!!! CAN BE EXTENDED WITH n NET_FILE IN THE .EXE !!!)

# mutualinfo(NET_FILE1, NET_FILE2)
#       Calculate and print out the modularity

# netcompare(NET_FILE1, NET_FILE2)
#       Compare two networks

# netlayout(NET_FILE, SEED, STEP -- default 0.05 --, NUMBER_OF_STEPS, DAMPING -- default 0.05 --, DIMENSION -- 1 or 2 or 3 --)
#       Print coordinates in 1D/2D/3D

# netprop(NET_FILE)
#       Calculate and print a variety of network properties:
#           - Calculate the size of the giant component and the number of components
#           - Number of nodes, links, and so on
#           - Distance, clustering...
#           - Betweeness
#           - Synchronizability

# netrandomize(NET_FILE, SEED)
#       Randomize the network

# nodeprop(NET_FILE)        For each node, it gives its degree and its betweeness


#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#

                                        #----------------------------------#
                                        #--- FAILED: SEGMENTATION FAULT ---#
                                        #----------------------------------#

# bipartitemodularity(NET_FILE, SEED, INVERTING_NETWORK_FACTOR -- 1 to invert, 0 to not invert --)
#       Gives modularity in a bipartite network

# bipartitemodularity_w(NET_FILE, SEED, INVERTING_NETWORK_FACTOR -- 1 to invert, 0 to not invert --)
#       Gives modularity in a bipartite network which weighted (!!! 3rd column nneeded !!!)

#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#

from subprocess import Popen, PIPE, STDOUT

print('Your files and networks should be in the same repository as this python document.\nRecommended values:\n FILE: String value as \'test.dat\'\n SEED (Random number generator seed - positive integer): 1111 \n INVERTING_NETWORK_FACTOR: 1 to invert, 0 nothing')


#--- MODULES

def countlinks(FILE):
    
    p = Popen(['rgraph-2.2.1/utils/countlinks.exe', "'" + str(FILE) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def getgiant(NET_FILE):
    
    p = Popen(['rgraph-2.2.1/utils/getgiant.exe', "'" + str(NET_FILE) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def lapspec(NET_FILE):
    
    p = Popen(['rgraph-2.2.1/utils/lapspec.exe', "'" + str(NET_FILE) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def modularbipart(NUMBER_OF_MODULES, MODULE_SIZE, NUMBER_OF_TEAM, TEAM_SIZE, TEAM_HOMOGENEITY, SEED):
    
    p = Popen(['rgraph-2.2.1/utils/modularbipart.exe', "'" + str(NUMBER_OF_MODULES) + "'", "'" + str(MODULE_SIZE) + "'", "'" + str(NUMBER_OF_TEAM) + "'", "'" + str(TEAM_SIZE) + "'", "'" + str(TEAM_HOMOGENEITY) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def multinetlayout(NET_FILE1, NET_FILE2):
    
    p = Popen(['rgraph-2.2.1/utils/multinetlayout.exe', "'" + str(NET_FILE1) + "'", "'" + str(NET_FILE2) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def mutualinfo(NET_FILE1, NET_FILE2):
    
    p = Popen(['rgraph-2.2.1/utils/mutualinfo.exe', "'" + str(NET_FILE1) + "'", "'" + str(NET_FILE2) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def netcompare(NET_FILE1, NET_FILE2):
    
    p = Popen(['rgraph-2.2.1/utils/netcompare.exe', "'" + str(NET_FILE1) + "'", "'" + str(NET_FILE2) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    

def netlayout(NET_FILE, SEED, STEP, NUMBER_OF_STEPS, DAMPING, DIMENSION):
    
    p = Popen(['rgraph-2.2.1/utils/netlayout.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'", "'" + str(STEP) + "'", "'" + str(NUMBER_OF_STEPS) + "'", "'" + str(DAMPING) + "'", "'" + str(DIMENSION) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    

def netprop(NET_FILE):
    
    p = Popen(['rgraph-2.2.1/utils/netprop.exe', "'" + str(NET_FILE) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    

def netrandomize(NET_FILE, SEED):
    
    p = Popen(['rgraph-2.2.1/utils/netrandomize.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    

def nodeprop(NET_FILE):
    
    p = Popen(['rgraph-2.2.1/utils/nodeprop.exe', "'" + str(NET_FILE) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)

    
def bipartitemodularity(NET_FILE, SEED, INVERTING_NETWORK_FACTOR):
    
    p = Popen(['rgraph-2.2.1/utils/bipartitemodularity.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'", "'" + str(INVERTING_NETWORK_FACTOR) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    
def bipartitemodularity_w(NET_FILE, SEED, INVERTING_NETWORK_FACTOR):
    
    p = Popen(['rgraph-2.2.1/utils/bipartitemodularity_w.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'", "'" + str(INVERTING_NETWORK_FACTOR) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
