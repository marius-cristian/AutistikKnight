
import maya.cmds as mc
import maya.mel as mm


melproc = """
global proc portData(string $arg){
    python(("portData(\\"" + $arg + "\\")"));
}
"""
mm.eval(melproc)


def portData(arg):
    """
    Read the 'serial' data passed in from the commandPort
    """
    print "Recieved!: ", arg

    # code that moves Left Arm Controller
    
    
    mappedVal=arg.split(",")
    mappedValx = float(mappedVal[0])
    mappedValy = float(mappedVal[1])
    print "mappedX:", mappedValx    
    mappedValz = float(mappedVal[2])
    if mc.objExists('Left_Arm_Controller'):
        mc.move(mappedValx, mappedValy, mappedValz)


mc.commandPort(name="127.0.0.1:26232", echoOutput=False, noreturn=False,
               prefix="portData", returnNumCommands=True)
mc.commandPort(name=":26232", echoOutput=False, noreturn=False,
               prefix="portData", returnNumCommands=True)