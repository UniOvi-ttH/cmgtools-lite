import ROOT
import os

base = "python makeShapeCardsSusy.py RunII_SM_WZ/2018/mca_wz_v5.txt RunII_SM_WZ/2018/cuts_wzsm.txt '[VAR]' '[BINS]' RunII_SM_WZ/2018/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/  --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/jet25Cleaned/ --Fs {P}/trigger_2018/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom' --obj Events -j 88 -l 59.8 -f  -E SRWZ -o 2018_[OVAR] --od ./cards_unblinding_forpostfit/ --ms --neg --plotgroup data_fakes+=promptsub  --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up"
plotfile = open("RunII_SM_WZ/common/plots_wz.txt","r")

for line in plotfile.readlines():
  if line[0] == "#" or len(line.split(":")) < 3: continue
  words = line.split(":")
  name = words[0].replace(" ","")
  var  = words[1].replace(" ","")
  bins = words[2].split(";")[0].replace(" ","")
  #if os.path.exists("cards_unblinding_forpostfit/common/2018_%s.input.root"%name): continue
  print base.replace("[OVAR]", name).replace("[VAR]", var).replace("[BINS]",bins)
  print "" 
