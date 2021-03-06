python makeShapeCardsSusy.py RunII_SM_WZ/2016/mca_wz_v5.txt RunII_SM_WZ/2016/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2016/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 35.9 -f  -E SRWZ -o 2016eee --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E eee --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2016/mca_wz_v5.txt RunII_SM_WZ/2016/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2016/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 35.9 -f  -E SRWZ -o 2016eem --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E eem --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2016/mca_wz_v5.txt RunII_SM_WZ/2016/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2016/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 35.9 -f  -E SRWZ -o 2016mme --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E mme --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2016/mca_wz_v5.txt RunII_SM_WZ/2016/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2016/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 35.9 -f  -E SRWZ -o 2016mmm --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E mmm --asimov


python makeShapeCardsSusy.py RunII_SM_WZ/2017/mca_wz_v5.txt RunII_SM_WZ/2017/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2017/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 41.5 -f  -E SRWZ -o 2017eee --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E eee --asimov


python makeShapeCardsSusy.py RunII_SM_WZ/2017/mca_wz_v5.txt RunII_SM_WZ/2017/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2017/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 41.5 -f  -E SRWZ -o 2017eem --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E eem --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2017/mca_wz_v5.txt RunII_SM_WZ/2017/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2017/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 41.5 -f  -E SRWZ -o 2017mme --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E mme --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2017/mca_wz_v5.txt RunII_SM_WZ/2017/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2017/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -l 41.5 -f  -E SRWZ -o 2017mmm --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E mmm --asimov



python makeShapeCardsSusy.py RunII_SM_WZ/2018/mca_wz_v5.txt RunII_SM_WZ/2018/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2018/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/  --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom' --obj Events -j 96 -l 59.8 -f  -E SRWZ -o 2018eee --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E eee --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2018/mca_wz_v5.txt RunII_SM_WZ/2018/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2018/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/  --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom' --obj Events -j 96 -l 59.8 -f  -E SRWZ -o 2018eem --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E eem --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2018/mca_wz_v5.txt RunII_SM_WZ/2018/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2018/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/  --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom' --obj Events -j 96 -l 59.8 -f  -E SRWZ -o 2018mme --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E mme --asimov

python makeShapeCardsSusy.py RunII_SM_WZ/2018/mca_wz_v5.txt RunII_SM_WZ/2018/cuts_wzsm.txt "(abs(LepZ1_pdgId)+abs(LepZ2_pdgId)+abs(LepW_pdgId)-33)/2" "4,-0.5,3.5" RunII_SM_WZ/2018/systs_wz.txt  --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/  --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --FMCs {P}/bosonPolarization/ --FMCs {P}/bosonPolarizationGEN/  -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc -L RunII_SM_WZ/functionsWZ.cc -W 'getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2])*puWeight*bTagWeightDeepCSVT_nom' --obj Events -j 96 -l 59.8 -f  -E SRWZ -o 2018mmm --od ./cards/ --ms --neg --plotgroup data_fakes+=promptsub --xp data --plotgroup data_fakes_fakes_Dn+=promptsub_fakes_Dn --plotgroup data_fakes_fakes_Up+=promptsub_fakes_Up -E mmm --asimov

