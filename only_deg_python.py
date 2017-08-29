#--------------------------------------------#
#------- ONLY DEGENERATION EXECUTABLES ------#
#--------------------------------------------#

#------ /only_deg/ ------#


#--- ALL MODULES IN THIS DOCUMENT:

# only_degeneration_mb(NET_FILE, SEED)          Gives reliability of all links but considering only degeneration
# only_degeneration_mb_gibbs(NET_FILE, SEED)    Same as previous but with Gibbs method


from subprocess import Popen, PIPE, STDOUT

print('Your files and networks should be in the same repository as this python document.\nRecommended values:\n NET_FILE: String value as \'test.dat\' or \'test.net\' -do not omit the comas-\n SEED (Random number generator seed - positive integer): 1111 recomended')
    
      
#--- MODULES

def only_degeneration_mb(NET_FILE, SEED):
    p = Popen(['rgraph-2.2.1/only_deg/only_degeneration_mb.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    print('The results are in the file '+str(NET_FILE)+'.scores')

def only_degeneration_mb_gibbs(NET_FILE, SEED):
    p = Popen(['rgraph-2.2.1/only_deg/only_degeneration_mb.exe', "'" + str(NET_FILE) + "'", "'" + str(SEED) + "'"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    result = p.communicate(input=b'1 2\n1 3\n1 4\n2 3\n2 4\n4 5\n5 6')[0]

    result_string = result.decode()

    print(result_string)
    print('The results are in the file '+str(NET_FILE)+'.scores')
