import os,commands
import sys
from optparse import OptionParser
import subprocess
from MATTEO_LatexFunctions import replace_latex,readVBFCutsFile,selectDEtaEvent,print_lined_string_File,print_boxed_string_File

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
(options, args) = parser.parse_args()

currentDir = os.getcwd();



######################################################
##### GLOBAL VARIABLES DEFINITION
######################################################

#Ntuple_Path_lxplus="/afs/cern.ch/user/l/lbrianza/work/public/%s/"%options.ntuple
Samples=["BulkGraviton","Higgs"];
Lumi_float_true=2300;
Luminosities=[Lumi_float_true];
Channel=options.channel;






######################################################
##### FUNCTION DEFINITION
######################################################


'''

def replace_latex(in_string):
    out1=in_string.replace("&&", "\&\&");
    out2=out1.replace("_", "\_");
    out3=out2.replace(">", "\\texttt{>}");
    out4=out3.replace("<", "\\texttt{<}");
    out5=out4.replace("||", "$||$")
    return out5



def readVBFCutsFile():
    textName="VBF_CutListFile.txt";
    
    if options.UnBlind:
       tmp_blind_dirName="UnBlind";
    
    else:
       tmp_blind_dirName="Blind";
    
    if options.pseudodata:
       
       if options.vbf:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/pseudoData/Lumi_%s_VBF/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;
       else:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/pseudoData/Lumi_%s/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;
    
    else:
       if options.vbf:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s_VBF/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;
       else:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;   

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



def selectDEtaEvent(cutVector):
    Deta=0.0;
    
    i=j=0;
    
    for i in cutVector:
        tmp0=i[0];
        tmp1=i[1];
        
        if tmp1==Deta:
           j=j+1;
           
    vectorLenght=int(j);
    
    i=j=0;
    outVector=[0.0 for i in range(vectorLenght)];
    
    i=j=0;
    for i in cutVector:
        tmp0=float(i[0]);
        tmp1=float(i[1]);
        
        if tmp0==Deta:
           outVector[j]=[tmp0,tmp1];
           print outVector[j]
           j=j+1;    
    return [vectorLenght,outVector];
    
    
    
    
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
    if total_lenght > 140:
       total_lenght=140;


        
    line_empty="\n";
    line_zero=""
    for k in range(offset):
        line_zero=line_zero+" ";
    

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









def print_boxed_string_File(in_string_vector,out_file):
    
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
    if total_lenght > 140:
       total_lenght=140;
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







'''






######################################################
##### MAIN CODE
######################################################
if __name__ == '__main__':
    

    Ntuple_dir_name="Ntuple_%s"%(options.ntuple)
    if not os.path.isdir(Ntuple_dir_name):
           os.system("mkdir "+Ntuple_dir_name);
   
    
    
    ##### VBF PROCESS
    if options.vbf:
       CutInputValues_tmp=readVBFCutsFile();
       CutInputNumber_tmp=CutInputValues_tmp[0];
       CutInputVector_tmp=CutInputValues_tmp[1];
       
       CutInputValues=selectDEtaEvent(CutInputVector_tmp);
       CutInputNumber=CutInputValues[0];
       CutInputVector=CutInputValues[1];
    
       CutValue=[0.0,0.0];
       
       ## Cycle over all     
       for lumi_float_value in Luminosities:
           
           lumi_str=str("%.0f"%lumi_float_value);
                     
           if options.pseudodata:
              lumi_dir=Ntuple_dir_name+"/pseudoData/Lumi_%s_VBF"%lumi_str;

           else:
              lumi_dir=Ntuple_dir_name+"/trueData/Lumi_%s_VBF/"%lumi_str;
              
           LatexFileName = lumi_dir+"ExclusionLimits_lumi_%.0f_VBF_Mjj.tex"%lumi_float_value;
           LatexFile = open(LatexFileName,'w+');
           LatexFile.write("\documentclass{beamer}\n");
           LatexFile.write("\usetheme{Boadilla}\n");
           LatexFile.write("\usecolortheme{seahorse}\n");
           LatexFile.write("\\title{ControlPlots}\n");
           LatexFile.write("\\author{Matteo Rappo}\n");
           LatexFile.write("\setbeamertemplate{navigation symbols}{}\n");
           LatexFile.write("\usepackage[latin1]{inputenc}\n");
           LatexFile.write("\usepackage[english,italian]{babel}\n");
           LatexFile.write("\usepackage{amsmath}\n");
           LatexFile.write("\usepackage{enumerate}\n");
           LatexFile.write("\usepackage{amsfonts}\n");
           LatexFile.write("\usepackage{amssymb}\n");
           LatexFile.write("\usepackage{float}\n");
           LatexFile.write("\usepackage{placeins}\n");
           LatexFile.write("\usepackage{subfig}\n");
           LatexFile.write("\usepackage{multirow,makecell}\n");
           LatexFile.write("\usepackage{array,booktabs}\n");
           LatexFile.write("\usepackage{comment}\n");
           LatexFile.write("\usepackage{scrextend}\n");
           LatexFile.write("\usepackage{verbatim,longtable}\n");
           LatexFile.write("\setbeamertemplate{caption}[numbered]\n");
           LatexFile.write("\\newcolumntype{P}[1]{>{\centering\\arraybackslash}p{#1}}\n");
           LatexFile.write("\\newcolumntype{M}[1]{>{\centering\\arraybackslash}m{#1}}\n");
           LatexFile.write("\\newcolumntype{D}[1]{>{\\arraybackslash}m{#1}}\n");
           LatexFile.write("\\newcolumntype{C}[1]{>{\centering\let\\newline\\\\arraybackslash\hspace{0pt}}m{#1}}\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
           LatexFile.write("\changefontsizes{9pt}\n");
           LatexFile.write("\\begin{document}\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
           
           
           
           # Ntuple Name in \texttt{} environment
           tmp_ntuple_texttt=replace_latex(options.ntuple);
           Ntuple_Name_texttt="\\texttt{"+tmp_ntuple_texttt+"}";

           if options.channel=="mu":
              channel_latex_mm="$\mu$";
    
           elif options.channel=="em":
                channel_latex_mm="e$\mu$";
    
           else:
                channel_latex_mm="e" 
           
           lumi=lumi_float_value/1000.0;
           #LatexFile.write("\graphicspath{{/home/matteo/Tesi/LxPlus_Matteo/ControlPlots/Lumi_2300_VBF/}}\n");
           
           LatexFile.write("\\begin{frame}\n");
           LatexFile.write("\\frametitle{Exclusion Plots - Settings }\n");   
           #LatexFile.write(latex_FrameSubtitle);
           LatexFile.write("\changefontsizes{11pt}\n");
           LatexFile.write("\\begin{itemize}\n");
           LatexFile.write("\item Luminosit\`a:%.1f ${fb}^{-1}$\n"%lumi);
           LatexFile.write("\item Ntuple: %s\n"%Ntuple_Name_texttt);
           LatexFile.write("\item Channel: %s\n"%channel_latex_mm);
           #LatexFile.write("\item W+Jets Scale Factor: %s\n"%Scale_W_Factor_global_str);
           #LatexFile.write("\item TTBar Scale Factor: %s\n"%TTBar_Scale_Factor_mm_str);
           LatexFile.write("\end{itemize}\n");
           LatexFile.write("\end{frame}\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
           LatexFile.write("\n");
    

           
           
           
 
           
           for sample in Samples:
               LatexFile.write("\\begin{frame}[allowframebreaks]\n");
               LatexFile.write("\\frametitle{Exclusion Plots - %s - Scan in $M_{jj}$}\n"%sample);
               LatexFile.write("\\framesubtitle{Ntuple %s \\vspace{6pt} Channel: %s \\vspace{6pt} Luminosity: %.1f ${fb}^{-1}$}\n"%(Ntuple_Name_texttt,channel_latex_mm,lumi));
               
               k=0;
               for CutValue in CutInputVector:  
                   tmp0=CutValue[0];
                   tmp1=CutValue[1];
                   Mjj=float(tmp1);
                   Deta=float(tmp0);
                   
                   Plots_dir="DEta%1.3f_Mjj_%.0f/cards_%s_%s_VBF/%s/limitFigs"%(Deta,Mjj,options.channel,options.category,sample);
                   
                   if k:
                      LatexFile.write("\\framebreak\n");
                   
                   
                   LatexFile.write("\\begin{center}\n");
                   LatexFile.write("\\begin{minipage}{0.4\\textwidth}\n");
                   LatexFile.write("\\begin{block}{}\n");
                   LatexFile.write("\centering\n");
                   LatexFile.write("$\Delta\eta_{jj}=%1.3f$ \\hspace{10pt} $M_{jj}>%.0f$\n"%(CutValue[0],CutValue[1]));
                   LatexFile.write("\end{block}\n");
                   LatexFile.write("\end{minipage}\n");
                   LatexFile.write("\end{center}\n");
                   LatexFile.write("\n");
                   LatexFile.write("\setcounter{subfigure}{0}\n");
                   LatexFile.write("\\begin{figure}[h]\n");
                   LatexFile.write("\\begin{center}\n");
                   LatexFile.write("\subfloat[][\emph{\\texttt{SMLim\_em\_HP.pdf}}]\n");
                   LatexFile.write("{\includegraphics[width=.4\columnwidth]{%s/SMLim_em_HP.pdf}} \quad\n"%(Plots_dir));
                   LatexFile.write("\subfloat[][\emph{\\texttt{SMXsec\_em\_HP.pdf}}]\n");
                   LatexFile.write("{\includegraphics[width=.4\columnwidth]{%s/SMXsec_em_HP.pdf}}\n"%(Plots_dir));
                   #ofile_gi.write("\%\caption{$\mu$-channel: Input Variables for Cut Optimization.}\n");
                   #LatexFile.write("\label{}\n");
                   LatexFile.write("\end{center}\n");
                   LatexFile.write("\end{figure}\n");
                   
                   
                   
                   LatexFile.write("\\begin{center}\n");
                   LatexFile.write("\\begin{minipage}{0.4\\textwidth}\n");
                   LatexFile.write("\\begin{block}{}\n");
                   LatexFile.write("\centering\n");
                   LatexFile.write("$\Delta\eta_{jj}=%1.3f$ \\hspace{10pt} $M_{jj}>%.0f$\n"%(CutValue[0],CutValue[1]));
                   LatexFile.write("\end{block}\n");
                   LatexFile.write("\end{minipage}\n");
                   LatexFile.write("\end{center}\n");
                   LatexFile.write("\n");
                   LatexFile.write("\setcounter{subfigure}{0}\n");
                   LatexFile.write("\\begin{figure}[h]\n");
                   LatexFile.write("\\begin{center}\n");
                   LatexFile.write("\subfloat[][\emph{\\texttt{m\_lvj\_sb\_lo\_WJets0}}]\n");
                   LatexFile.write("{\includegraphics[width=.48\columnwidth]{DataCardsPlot/DEta%1.3f_Mjj_%.0f/plots_em_HP_VBF/%s/m_lvj_fitting/%s1000/m_lvj_sb_lo_WJets0_xww__with_pull.pdf}} \quad\n"%(Deta,Mjj,sample,sample));
                   LatexFile.write("\subfloat[][\emph{\\texttt{m\_j\_sb\_lo\_WJets0}}]\n");
                   LatexFile.write("{\includegraphics[width=.48\columnwidth]{DataCardsPlot/DEta%1.3f_Mjj_%.0f/plots_em_HP_VBF/%s/m_j_fitting/%s1000/m_j_sideband_WJets0_xww__with_pull.pdf}}\n"%(Deta,Mjj,sample,sample));
                   #ofile_gi.write("\%\caption{$\mu$-channel: Input Variables for Cut Optimization.}\n");
                   #LatexFile.write("\label{}\n");
                   LatexFile.write("\end{center}\n");
                   LatexFile.write("\end{figure}\n");
                   
                   
                   k=k+1


               LatexFile.write("\end{frame}\n");
               
           LatexFile.write("\end{document}\n");
           LatexFile.close();
           
           
           
           
           
           
'''
scp -r mrappo@lxplus.cern.ch:~/work/test/CMSSW_7_1_5/src/boostedWWAnalysis/Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/ /home/matteo/Tesi/LxPlus_Matteo/ControlPlots/
'''
               
