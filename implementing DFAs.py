def abstract_machine(input_list):
     n= len(input_list)
     print('\nStarted abstract machine for L((a|b)*abb)')
     print('\nVerifying string '+input_list)
     print('\nEntered state A')
     for l in range(n-3):
             if input_list[l] == 'a':
                 print("\nPass")
             elif input_list[l] == 'b':
                 print('\nPass')
             else:
                 print('\nUnknown symbol encountered in state A')
                 print('\nTrapped and exited')
                 exit()
     if input_list[n - 3] == 'a':
             print('\nPass')
     else:
             print('\nUnknown or wrong symbol encountered in state A')
             print('\nTrapped and exited')
             exit()
     print('\nExited state A')
     print('\nEntered state B')

     if input_list[n-2] == 'b':
             print('Pass')
     else:
             print('\nUnknown or wrong symbol encountered in state B')
             print('\nTrapped and exited')
             exit()
     print('\nExited state B')
     print('\nEntered state C')
     if input_list[n-1] == 'b':
             print('Pass')
     else:
             print('\nUnknown or wrong symbol encountered in state C')
             print('\nTrapped and exited')
             exit()
     print('\nExited state C')
     print('\nEntered Final state and terminating')
     print('\nString '+input_list+' is accepted')
     exit(0)

if __name__ == "__main__":
    s=input('Enter string ending with abb : ')
    abstract_machine(s)
