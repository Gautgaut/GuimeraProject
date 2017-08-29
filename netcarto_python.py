from subprocess import Popen, PIPE, STDOUT

#---------------------------------#
#------ NETCARTO EXECUTABLES -----#
#---------------------------------#

#------ /netcarto/ ------#

print('Your files and networks should be in the same repository as this python document.\nRecommended values:\n FILE: String value as \'test.dat\'\n SEED (Random number generator seed - positive integer): 1111 \n ITER (Iteration factor): 1.0 \n COOL (Cooling factor): between 0.950-0.995\n PARTITION_FILE: String value as \'partition.dat\'')


#--- A GIVEN NETWORK

def netcarto(FILE, SEED, ITER, COOL):
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-s', "'" + str(SEED) + "'", '-i', "'" + str(ITER) + "'", '-c', "'" + str(COOL) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def netcarto_weighted(FILE, SEED, ITER, COOL): # Needs a 3rd column with weighted modularity
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-s', "'" + str(SEED) + "'", '-i', "'" + str(ITER) + "'", '-c', "'" + str(COOL) + "'", '-w'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def netcarto_modularity(FILE, SEED, ITER, COOL): # Gives a proheminent modularity
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-s', "'" + str(SEED) + "'", '-i', "'" + str(ITER) + "'", '-c', "'" + str(COOL) + "'", '-r'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


#--- PARTITION

def netcarto_modularity_partition(FILE, PARTITION_FILE): # Gives a proheminent modularity
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-p', "'" + str(PARTITION_FILE) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


#--- BIPARTITE NETWORKS
    
def netcarto_bipart_weighted(FILE, SEED, ITER, COOL): # Needs a 3rd column with weighted modularity in a bipartite network
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-s', "'" + str(SEED) + "'", '-i', "'" + str(ITER) + "'", '-c', "'" + str(COOL) + "'", '-w', '-b'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def netcarto_bipart_weighted_2nd(FILE, SEED, ITER, COOL): # Needs a 3rd column with weighted modularity for the 2nd column in a bipartite network
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-s', "'" + str(SEED) + "'", '-i', "'" + str(ITER) + "'", '-c', "'" + str(COOL) + "'", '-w', '-b', '-t'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)

    
def netcarto_bipart_modularity(FILE, SEED, ITER, COOL): # Gives a proheminent modularity in a bipartite network
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-s', "'" + str(SEED) + "'", '-i', "'" + str(ITER) + "'", '-c', "'" + str(COOL) + "'", '-r', '-b'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def netcarto_bipart_modularity_2nd(FILE, SEED, ITER, COOL): # Gives a proheminent modularity for the 2nde column in a bipartite network
    
    p = Popen(['rgraph-2.2.1/netcarto/netcarto.exe', '-f', "'" + str(FILE) + "'", '-s', "'" + str(SEED) + "'", '-i', "'" + str(ITER) + "'", '-c', "'" + str(COOL) + "'", '-r', '-b', '-t'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
