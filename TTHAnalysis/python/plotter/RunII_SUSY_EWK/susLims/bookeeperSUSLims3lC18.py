import os

base183l = "python makeShapeCardsNew.py RunII_SUSY_EWK/2018/3l/mca_ewkino_v5.txt RunII_SUSY_EWK/2018/3l/cuts_3l.txt '[VAR]' '[BINS]' --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_estructure/ -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_signals/ --FFulls {P}/leptonPtCorrections/ --FFasts {P}/puWeight/ --Fs {P}/leptonJetReCleanerEWK_NEWID/ --Fs {P}/leptonBuilderEWK_NEWID/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights_NEWID/  -L RunII_SM_WZ/functionsWZ.cc -L RunII_SUSY_EWK/functionsSF.cc -L RunII_SUSY_EWK/functionsMCMatch.cc -L RunII_SUSY_EWK/functionsWZ.cc --plotgroup data_fakes+=.*promptsub.* --neglist .*promptsub.* --neg -W 'puWeight*($MC{bTagWeightDeepCSVT_nom} $FASTSIM{bTagWeightDeepCSVT})*getLeptonSF_v5(2,0,2018,LepSel_conePt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v5(2,0,2018,LepSel_conePt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v5(2,0,2018,LepSel_conePt[2],LepSel_eta[2],LepSel_pdgId[2])' --obj Events -j 8 -f --od [OD] -l 59.8 -E [SRCUT] [EXCLUDERS] -L ./RunII_SUSY_EWK/functionsEWKcorr.cc --unc RunII_SUSY_EWK/systs/systs_wz18_forplot.txt  --ms --mcc RunII_SUSY_EWK/2018/mcc_triggerdefs.txt"


allSignals = ['sig_TChiWZ.*', 'sig_TChiWH.*', 'sig_TChiZZ.*', 'sig_TChiHH.*', 'sig_TChiHZ.*', 'sig_TChiSlep.*', 'sig_TChiTESlep.*', 'sig_TChiStau.*']
vetoSignals = ['sig_TChiWZ.*', 'sig_TChiSlep.*']
varsandbins = {'SRC_new(MET_pt_nom, mt_2(pt_2(LepSel_conePt[mll_i1[0]],LepSel_phi[mll_i1[0]],LepSel_conePt[mll_i2[0]],LepSel_phi[mll_i2[0]]), phi_2(LepSel_conePt[mll_i1[0]],LepSel_phi[mll_i1[0]],LepSel_conePt[mll_i2[0]],LepSel_phi[mll_i2[0]]),MET_pt_nom,MET_phi_nom),mT2L_3l)' :'9,0.5,9.5'} 
oCARD = 'SR3lC_2018'
oDir  = {'SRC_new(MET_pt_nom, mt_2(pt_2(LepSel_conePt[mll_i1[0]],LepSel_phi[mll_i1[0]],LepSel_conePt[mll_i2[0]],LepSel_phi[mll_i2[0]]), phi_2(LepSel_conePt[mll_i1[0]],LepSel_phi[mll_i1[0]],LepSel_conePt[mll_i2[0]],LepSel_phi[mll_i2[0]]),MET_pt_nom,MET_phi_nom),mT2L_3l)':'cards_3lC18_SRnew'}

for sigs in allSignals:
  if sigs in vetoSignals: continue
  for vb in varsandbins:
     excluders = ""
     for v in allSignals:
       if v != sigs:
          excluders = excluders + " --xp " + v
     command = base183l.replace("[VAR]", vb).replace("[BINS]",varsandbins[vb]).replace("[SRCUT]","SR3lC").replace("[OCARD]",oCARD).replace("[OD]", oDir[vb]+ sigs.replace("sig_","").replace(".*","")).replace("[EXCLUDERS]", excluders)
     print command
     os.system("sbatch -c 8 -p batch -J" + sigs + " --wrap \"" + command.replace("$","\$") + "\"")
