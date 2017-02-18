import os,commands
import sys
from optparse import OptionParser
import subprocess

parser = OptionParser()

parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="em")
parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--category', action="store",type="string",dest="category",default="HP")
parser.add_option('--lumi', action="store",type="float",dest="lumi",default=2300.0)
parser.add_option('--batchMode', action="store_true",dest="batchMode",default=False)
parser.add_option('--vbf', action="store_true",dest="vbf",default=True)
parser.add_option('--pseudodata', action="store_true",dest="pseudodata",default=False)
parser.add_option('--copyDC', action="store_true",dest="copyDC",default=True)
parser.add_option('--UnBlind', action="store_true",dest="UnBlind",default=False)
parser.add_option('--CrossCuts', action="store_true",dest="CrosCuts",default=True)

(options, args) = parser.parse_args()

currentDir = os.getcwd();


## DeltaEta Cut
DEta_values=[0.0,0.2];
#DEta_values=[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0];



# Mjj Cut
DMjj_values=[0.0];
#DMjj_values=[0.0,20.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,180.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0];



######################################################
##### GLOBAL VARIABLES DEFINITION
######################################################

#Ntuple_Path_lxplus="/afs/cern.ch/user/l/lbrianza/work/public/%s/"%options.ntuple
Samples=["BulkGraviton","Higgs"];
Lumi_float_true=options.lumi;
Luminosities=[Lumi_float_true];
Channel=options.channel;






######################################################
##### FUNCTION DEFINITION
######################################################

def readVBFCutsFile():
    textName="VBF_CutListFile.txt";
    
    if options.UnBlind:
       tmp_blind_dirName_r="UnBlind/";
    
    else:
       tmp_blind_dirName_r="UnBlind/";
    
    
    if options.pseudodata:
       
       if options.vbf:
          in_VBFCutsFile="/afs/cern.ch/user/m/mrappo/work/public/Ntuple_%s/pseudoData/Lumi_%s_VBF/%s_Channel/%s"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName_r)+textName;
       else:
          in_VBFCutsFile="/afs/cern.ch/user/m/mrappo/work/public/Ntuple_%s/pseudoData/Lumi_%s/%s_Channel/%s"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName_r)+textName;
    
    else:
       if options.vbf:
          in_VBFCutsFile="/afs/cern.ch/user/m/mrappo/work/public/Ntuple_%s/trueData/Lumi_%s_VBF/%s_Channel/%s"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName_r)+textName;
       else:
          in_VBFCutsFile="/afs/cern.ch/user/m/mrappo/work/public/Ntuple_%s/trueData/Lumi_%s/%s_Channel/%s"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName_r)+textName;    

    tmp_VBFCutsFile=open(in_VBFCutsFile, 'r');
    readedLines=tmp_VBFCutsFile.readlines();
    
    i=j=0;
    for i in readedLines:
        j=j+1;
    
    totalLineNumber=j;
    
    i=j=0;
    
    tmp_Cuts_Vector= [0 for i in range(totalLineNumber)];
    i=j=0;
    
    for i in range(totalLineNumber):
        tmp_Cuts_Vector[i]=[float((readedLines[i]).split(" ")[0]),float((readedLines[i]).split(" ")[1])];
    
    tmp_VBFCutsFile.close();
    return [totalLineNumber,tmp_Cuts_Vector];


def print_lined_string_File(in_string_vector,out_file):
    
    offset=3;

    s_number=0;
    for t in in_string_vector:
        s_number=s_number+1;
    
    lenght=0;
    for i in in_string_vector:
        tmp_lenght=len(i);
        if tmp_lenght>lenght:
           lenght=tmp_lenght;
    total_lenght=int(lenght*1.40)
    if total_lenght > 120:
       total_lenght=120;


        
    line_empty="\n";
    line_zero=""
    for k in range(offset):
        line_zero=line_zero+" ";
    
    #out_file = open(in_FileName,'a'); 
    out_file.write("\n"+line_empty);
    out_file.write("\n"+line_empty);
    print line_empty
    print line_empty
    z=0;
    for i in in_string_vector:
        if z:
          
           print_string=line_zero+i;
           out_file.write("\n"+print_string);
           print print_string
        else:
           tmp_len=len(i);
           pos=int((total_lenght-tmp_len)/2);
           tmp_final_space="";
           for k in range(pos):
               tmp_final_space=tmp_final_space+"-";
           
           if not i==" ":
               print_string=tmp_final_space+" "+i+" "+tmp_final_space;
           else:
               print_string=tmp_final_space+"---"+tmp_final_space;
           out_file.write("\n"+line_empty);
           out_file.write("\n"+line_empty);
           out_file.write("\n"+print_string);
           out_file.write("\n"+line_empty);
           
           print line_empty
           print line_empty
           print print_string
           print line_empty
           
           z=1;
    
        
    out_file.write("\n"+line_empty);
    print line_empty
    
    final_line="";
    for k in range(total_lenght+1):
        final_line=final_line+"-";
    
    out_file.write("\n"+final_line);
    out_file.write("\n"+line_empty);
    
    print final_line
    print line_empty
    #out_file.close();








def print_boxed_string_File(in_string_vector,out_file):
    
    
    #out_file = open(in_FileName,'a');
    
    offset_1=3;
    offset_2=4;
    s_number=0;
    t=0;
    for t in in_string_vector:
        s_number=s_number+1;
    
    lenght=0;
    i=0;
    for i in in_string_vector:
        tmp_lenght=len(i);
        if tmp_lenght>lenght:
           lenght=tmp_lenght;
    total_lenght=int(lenght*1.50)
    if total_lenght > 120:
       total_lenght=120;
    line_ext="";
    line_in="";
    zero_space="";
    i=0;
    for i in range(offset_1):
        line_ext=line_ext+" ";
        line_in=line_in+" ";
    i=0;
    for i in range(offset_2):
        zero_space=zero_space+" ";
    line_ext=line_ext+" ";
    
    i=0;
    for i in range(total_lenght):
        line_ext=line_ext+"-";
        
    line_empty=line_in+"|";
    for i in range(total_lenght):
        line_empty=line_empty+" ";
    line_empty=line_empty+"|";
    
    out_file.write("\n");
    out_file.write("\n");
    out_file.write("\n");
    out_file.write("\n"+line_ext);
    out_file.write("\n"+line_empty);
    
    print "\n\n"
    print line_ext
    print line_empty
    
    z=0;
    for i in in_string_vector:
        if z:
           tmp_len=len(i);
           tmp_final_space=""
           for k in range(total_lenght-offset_2-tmp_len):
               tmp_final_space=tmp_final_space+" ";
           print_string=line_in+"|"+zero_space+i+tmp_final_space+"|"
           out_file.write("\n"+print_string);
           print print_string
         
        else:
           tmp_len=len(i);
           tmp_final_space=""
           add=int((total_lenght-tmp_len)/2)
           for k in range(add):
               tmp_final_space=tmp_final_space+" ";
           add_line="";
           if (2*add+tmp_len)<total_lenght:
              add_line=" ";
         
           print_string=line_in+"|"+tmp_final_space+i+tmp_final_space+add_line+"|"
           #out_file.write("\n"+line_empty
           out_file.write("\n"+print_string);
           out_file.write("\n"+line_empty);
           
           print print_string
           print line_empty
           
           z=1;
    
    if (s_number-1): 
       out_file.write("\n"+line_empty);
       print line_empty
    out_file.write("\n"+line_ext);
    out_file.write("\n");
    out_file.write("\n");
    
    print line_ext
    print "\n\n"

    #out_file.close();












######################################################
##### MAIN CODE
######################################################
if __name__ == '__main__':
    
    
    
    dirFullCLsFileName="DirectoryForFullCLs.txt";
    dirFullCLsFile=open(dirFullCLsFileName,'w+');
    
    Ntuple_dir_name="Ntuple_%s"%(options.ntuple)
    if not os.path.isdir(Ntuple_dir_name):
           #os.system("mkdir "+Ntuple_dir_name);
           pd1 = subprocess.Popen(['mkdir',Ntuple_dir_name]);
           pd1.wait();
    
    
    if options.UnBlind:
       tmp_blind_dirName="UnBlind";
    
    else:
       tmp_blind_dirName="Blind";
    
    ##### VBF PROCESS
    if options.vbf:
       
       
       # Count number of DeltaEtajj Cuts
       n_eta=0;
       i=0;
       for i in DEta_values:
           n_eta=n_eta+1;
           print "Deta: %f \t\t n_eta: %.0f"%(i,n_eta)
       
       n_eta=int(n_eta);
       
       
         
    
       # Count number of Mjj Cuts
       n_mjj=0;
       i=0;
       for i in DMjj_values:
           n_mjj=n_mjj+1;
           print "DMjj: %f \t\t n_mjj: %.0f"%(i,n_mjj)
        
       n_mjj=int(n_mjj);
       
       
       
       
       
       
       
       
       # Store all cuts in a Vector: index 0 -> DEltaEta Cut
       #                             index 1 -> Mjj Cut
       if options.CrosCuts:
          print "\nCROSS CUTS\n"
          i=j=0;
          range_value=int((n_mjj*n_eta));
          print range_value
          VBF_cut_values=[0.0 for i in range(range_value)];
                    
          i=j=0;
          for i in range(n_mjj):
                 j=0;
                 for j in range(n_eta):
                     tmp=(i*(n_eta)+j);
                     VBF_cut_values[tmp]=[float("%1.3f"%DEta_values[j]),float("%.0f"%DMjj_values[i])];
                     #tmp_TTB_SF=get_ScaleFactor(float("%1.3f"%DEta_values[j]),float("%.0f"%DMjj_values[i]),ControlP_Dir_2,outputFileName);
                     #VBF_cut_values[tmp]=tmp_TTB_SF;

           
           
      
              
       else:
          print "\nSINGLE CUTS\n"
          i=j=0;

          range_value=int(n_mjj+n_eta-1);
          VBF_cut_values=[0.0 for i in range(range_value)];          

          i=j=0;
          for i in range(n_eta):
              #tmp_TTB_SF=get_ScaleFactor(float("%1.3f"%DEta_values[i]),0.0,ControlP_Dir_2,outputFileName);
              #print "\n"
              #print tmp_TTB_SF
              VBF_cut_values[i]=[float("%1.3f"%DEta_values[i]),0.0];
          
          for j in range(n_mjj-1):
              #tmp_TTB_SF=get_ScaleFactor(0.0,float("%.0f"%DMjj_values[j+1]),ControlP_Dir_2,outputFileName);
              #print "\n"
              #print tmp_TTB_SF
              VBF_cut_values[n_eta+j]=[0.0,float("%.0f"%DMjj_values[j+1])];
       
       
       

       

       # Check the CutsVector
       i=0;
       print "\n\nVector of Cut Values:\n"
       print "Total CutsNumber: %.0f"%range_value
       print "\n"
       for i in range(range_value):
           i=int(i);
           tmp=VBF_cut_values[i];
           DEta_tmp=tmp[0];
           Mjj_tmp=tmp[1];
           DEta_local=float(DEta_tmp);
           Mjj_local=float(Mjj_tmp);
           print " %.0f)  DEta: %1.3f \t\t Mjj: %.1f\n"%((i+1),DEta_local,Mjj_local)
       
       
       
       

       
       #CutInputValues=readVBFCutsFile();
       CutInputNumber=range_value
       CutInputVector=VBF_cut_values
       
       #CutInputVector=[[0.0,0.0],[1.0,0.0]];
       
       CutValue=[0.0,0.0];
       Sample=["BulkGraviton","Higgs"]
       ## Cycle over all     
       for lumi_float_value in Luminosities:
           lumi_str=str("%.0f"%lumi_float_value);
           
           for CutValue in CutInputVector:
            
               if options.pseudodata:
                  pseudodata_dir=Ntuple_dir_name+"/pseudoData"
                  if not os.path.isdir(pseudodata_dir):
                         #os.system("mkdir "+pseudodata_dir);
                         pd2P = subprocess.Popen(['mkdir',pseudodata_dir]);
                         pd2P.wait();
                             
                  datacards_dir_in="/afs/cern.ch/user/m/mrappo/work/public/Ntuple_%s/Lumi_%s_VBF/DEta%1.3f_Mjj_%.0f/cards_%s_%s_VBF"%(options.ntuple,lumi_str,options.channel,CutValue[0],CutValue[1],options.category,sample);
                  lumi_dir=Ntuple_dir_name+"/pseudoData/Lumi_%s_VBF"%lumi_str;
                  if not os.path.isdir(lumi_dir):
                         #os.system("mkdir "+lumi_dir);
                         pd2PL = subprocess.Popen(['mkdir',lumi_dir]);
                         pd2PL.wait();
             
             
               else:
                  truedata_dir=Ntuple_dir_name+"/trueData"
                  if not os.path.isdir(truedata_dir):
                         #os.system("mkdir "+truedata_dir);
                         pd2T = subprocess.Popen(['mkdir',truedata_dir]);
                         pd2T.wait();
          
                  #../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/
                  datacards_dir_in="/afs/cern.ch/user/m/mrappo/work/public/Ntuple_%s/trueData/Lumi_%s_VBF/%s_Channel/UnBlind/DEta%1.3f_Mjj_%.0f/cards_%s_%s_VBF"%(options.ntuple,lumi_str,options.channel,CutValue[0],CutValue[1],options.channel,options.category);
                  #datacards_dir_in="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s_VBF/%s_Channel/%s/DEta%1.3f_Mjj_%.0f/cards_%s_%s_VBF"%(options.ntuple,lumi_str,options.channel,tmp_blind_dirName,CutValue[0],CutValue[1],options.channel,options.category);
                  lumi_dir=Ntuple_dir_name+"/trueData/Lumi_%s_VBF"%lumi_str;
                  if not os.path.isdir(lumi_dir):
                         #os.system("mkdir "+lumi_dir);
                         pd2TL = subprocess.Popen(['mkdir',lumi_dir]);
                         pd2TL.wait();

  
               datacards_dir_out_tmp1=lumi_dir+"/%s_Channel"%(options.channel);
               if not os.path.isdir(datacards_dir_out_tmp1):
                         #os.system("mkdir "+lumi_dir);
                         pd2TL1 = subprocess.Popen(['mkdir',datacards_dir_out_tmp1]);
                         pd2TL1.wait();
               
               datacards_dir_out_tmp2=datacards_dir_out_tmp1+"/%s"%(tmp_blind_dirName);
               if not os.path.isdir(datacards_dir_out_tmp2):
                         #os.system("mkdir "+lumi_dir);
                         pd2TL2 = subprocess.Popen(['mkdir',datacards_dir_out_tmp2]);
                         pd2TL2.wait();
               

               datacards_dir_out_tmp22=datacards_dir_out_tmp2+"/M2_fullCLs";
               if not os.path.isdir(datacards_dir_out_tmp22):
                      #os.system("mkdir "+lumi_dir);
                      pd2TL22 = subprocess.Popen(['mkdir',datacards_dir_out_tmp22]);
                      pd2TL22.wait();
               

               
                  
               
               
               datacards_dir_out_tmp3=datacards_dir_out_tmp22+"/DEta%1.3f_Mjj_%.0f"%(CutValue[0],CutValue[1]);
               if not os.path.isdir(datacards_dir_out_tmp3):
                         #os.system("mkdir "+lumi_dir);
                         pd2TL3 = subprocess.Popen(['mkdir',datacards_dir_out_tmp3]);
                         pd2TL3.wait();
               
               
                  
               
               datacards_dir_out=datacards_dir_out_tmp3;
               
               
               
               
               
                           
               if not options.copyDC:
                      if not os.path.isdir(datacards_dir_out):
                             print datacards_dir_in  
                             print "\n\nDatacard Mancanti. Uscita. \n\n"
                             sys.exit();
        
        
               SummaryFileName=lumi_dir+"SummaryLimitsFile.txt";
               if os.path.isfile(SummaryFileName):
                  pRM = subprocess.Popen(['rm',SummaryFileName]);
                  pRM.wait(); 
               SummaryFile=open(SummaryFileName, 'w+');
               SummaryFile.write("\nEVALUATING EXCLUSION LIMITS\n\n");
        
               ### COPY DATACARD
               if options.copyDC:
                  if not os.path.isdir(datacards_dir_out):
                         #os.system("mkdir "+datacards_dir_out);
                         pd3 = subprocess.Popen(['mkdir',datacards_dir_out]);
                         pd3.wait();
   
                  pCD = subprocess.Popen(['cp','-r',datacards_dir_in,datacards_dir_out]);
                  pCD.wait();
                  
                  fileName1="MATTEO_runLocal_fullCLs.py";
                  fileName2="MATTEO_makeROOTfile.py";
                  fileName3="MATTEO_HaddForFullCLs.py";
                  
                  for sm in Sample:
                      dirFullCLsFile.write(datacards_dir_out+"/cards_em_HP_VBF/%s/\n"%(sm));
                      FinalFileName1=datacards_dir_out+"/cards_em_HP_VBF/%s/"%(sm)+fileName1;
                      FinalFileName2=datacards_dir_out+"/cards_em_HP_VBF/%s/"%(sm)+fileName2;
                      FinalFileName3=datacards_dir_out+"/cards_em_HP_VBF/%s/"%(sm)+fileName3;


                      pCfile1 = subprocess.Popen(['cp',fileName1,FinalFileName1]);
                      pCfile1.wait();
           
                      pCfile2 = subprocess.Popen(['cp',fileName2,FinalFileName2]);
                      pCfile2.wait();
                      
                      pCfile3 = subprocess.Popen(['cp',fileName3,FinalFileName3]);
                      pCfile3.wait();                      
                      
                      tmp_string=["COPY FILES",
                              " ",
                              "Copy File 1 from: %s"%fileName1,
                              " ",
                              "Copy File 1 to: %s"%FinalFileName1,
                              " ",
                              "Copy File 2 from: %s"%fileName2,
                              " ",
                              "Copy File 2 to: %s"%FinalFileName2,
                              " ",
                              "Copy File 3 from: %s"%fileName3,
                              " ",
                              "Copy File 3 to: %s"%FinalFileName3];
                      print_lined_string_File(tmp_string,SummaryFile);
                      
     
                  
                  
                  
                  tmp_string=["COPY DATACARDS",
                              " ",
                              "COPY DC FROM: %s"%datacards_dir_in,
                              " ",
                              "COPY DC TO: %s"%datacards_dir_out];
                  print_lined_string_File(tmp_string,SummaryFile);
                  
                  
                  
                   
  
  
               
  
               # Close the SummaryFile
               SummaryFile.close(); 
    dirFullCLsFile.close();
  
  
  
  
  
  
  
 
    
# hadd -f higgisCombin_mu_unbin.root higgsCombinemuHWWlvjj_unbin.Asymptotic.mH600.root higgsCombinemuHWWlvjj_unbin.Asymptotic.mH700.root higgsCombinemuHWWlvjj_unbin.Asymptotic.mH800.root higgsCombinemuHWWlvjj_unbin.Asymptotic.mH900.root higgsCombinemuHWWlvjj_unbin.Asymptotic.mH1000.root  
    
    
#python MATTEO_LimitsCode.py -b --computeLimits --channel em --datacardDIR Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/DEta2.500_Mjj_200/cards_em_HP_VBF/BulkGraviton --makeSMLimitPlot 1 --plotLimits 1 --systematics 1 --sample BulkGraviton --vbf TRUE --blindObservedLine 1 --jetBin _2jet > Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/DEta2.500_Mjj_200/cards_em_HP_VBF/BulkGraviton/Log_VBF/log_VBF_BulkGraviton.log   
       
