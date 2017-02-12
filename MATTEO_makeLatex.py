import os,commands
import sys
from optparse import OptionParser
import subprocess

parser = OptionParser()

parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="em")
parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--category', action="store",type="string",dest="category",default="HP")
parser.add_option('--lumi', action="store",type="float",dest="lumi",default=2300)
#parser.add_option('--jetalgo', action="store",type="string",dest="jetalgo",default="jet_mass_pr")
#parser.add_option('--interpolate', action="store_true",dest="interpolate",default=False)
#parser.add_option('--batchMode', action="store_true",dest="batchMode",default=False)
parser.add_option('--vbf', action="store_true",dest="vbf",default=True)
parser.add_option('--pseudodata', action="store_true",dest="pseudodata",default=False)
parser.add_option('--copyDC', action="store_true",dest="copyDC",default=True)
parser.add_option('--UnBlind', action="store_true",dest="UnBlind",default=False)
(options, args) = parser.parse_args()

currentDir = os.getcwd();

if options.UnBlind:
   pl1 = subprocess.Popen(['python','MATTEO_makeLatexCross.py','--UnBlind']);
   pl1.wait();

   pl2 = subprocess.Popen(['python','MATTEO_makeLatexDeta.py','--UnBlind']);
   pl2.wait();

   pl3 = subprocess.Popen(['python','MATTEO_makeLatexMjj.py','--UnBlind']);
   pl3.wait();


else:


   pl1 = subprocess.Popen(['python','MATTEO_makeLatexCross.py']);
   pl1.wait();

   pl2 = subprocess.Popen(['python','MATTEO_makeLatexDeta.py']);
   pl2.wait();

   pl3 = subprocess.Popen(['python','MATTEO_makeLatexMjj.py']);
   pl3.wait();
           
'''
scp -r mrappo@lxplus.cern.ch:~/work/test/CMSSW_7_1_5/src/boostedWWAnalysis/Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/ /home/matteo/Tesi/LxPlus_Matteo/ControlPlots/
'''
               
