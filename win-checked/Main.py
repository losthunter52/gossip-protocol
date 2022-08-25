from bin.Menu import ControlPainel

#---------------------------------------------------------------------------
# Main Class
#---------------------------------------------------------------------------

# main method
def Main():
    # responsible for starting and ending the p2p model

    #params------------------------------------------------------------
    HOST = '192.168.1.95'
    neighborhood = ['192.168.1.10', '192.168.1.10']
    #------------------------------------------------------------------


    #init app
    launcher = ControlPainel(HOST, neighborhood)
    launcher.start()

    launcher.join()

# program launcher
if __name__ == '__main__':
    Main()