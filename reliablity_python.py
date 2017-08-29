#--------------------------------------#
#------- RELIABILITY EXECUTABLES ------#
#--------------------------------------#

#------ /reliability/ ------#


#--- ALL MODULES IN THIS DOCUMENT:

# reliability_links(NET_FILE, SEED)
# reliability_links_gibbs(NET_FILE, SEED)
# reliability_links_gibbs_sparse(NET_FILE, SEED)

#--- BROKEN:

# reliability_links_k(K, NET_FILE, SEED)    Works with missing.dat or spurious.dat
# reliability_reconstruct(NET_FILE, SEED)

from subprocess import Popen, PIPE, STDOUT

print('Your files and networks should be in the same repository as this python document.\nRecommended values:\n NET_FILE: String value as \'test.dat\' or \'test.net\' -do not omit the comas-\n SEED (Random number generator seed - positive integer): 1111 recomended')
    
      
#--- MODULES

def reliability_links(NET_FILE, SEED):
    p = Popen(['rgraph-2.2.1/reliability/reliability_links.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    print('Two documents are created: missing.out and spurious.out')
    

def reliability_links_gibbs(NET_FILE, SEED):
    p = Popen(['rgraph-2.2.1/reliability/reliability_links_gibbs.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    

def reliability_links_gibbs_sparse(NET_FILE, SEED):
    p = Popen(['rgraph-2.2.1/reliability/reliability_links_gibbs_sparse.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    

def reliability_links_k(K, NET_FILE, SEED):
    p = Popen(['rgraph-2.2.1/reliability/reliability_links_k.exe', "'" + str(K) + "'", "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    

def reliability_reconstruct(NET_FILE, SEED):
    p = Popen(['rgraph-2.2.1/reliability/reliability_reconstruct.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)


def prettyprint(DAT_FILE):
    with open(DAT_FILE, 'rU') as fp:
        lines = fp.read().split('0.')
    lines.pop(0)
    with open(DAT_FILE +'.clean', 'w') as fout:
        for l in lines:
            fout.write('0.'+l)
