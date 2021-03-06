#python mcPlots.py RunII_SM_WZ/2016/mca_wz_polW.txt RunII_SM_WZ/2016/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_skimWZ//bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2016_v5_blind_polW_withtaus/ --showRatio -E SRWZ -l 35.9 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data


#python mcPlots.py RunII_SM_WZ/2017/mca_wz_polW.txt RunII_SM_WZ/2017/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/trigger_2017/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2017_v5_blind_polW_withTaus/ --showRatio -E SRWZ -l 41.5 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt


#python mcPlots.py RunII_SM_WZ/2018/mca_wz_polW.txt RunII_SM_WZ/2018/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/ --Fs {P}/leptonJetReCleanerWZSM/  --Fs {P}/trigger_2018/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2018_v5_blind_polW_withtaus/ --showRatio -E SRWZ -l 59.8 --sP pol.*cos.* --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt



#python mcPlots.py RunII_SM_WZ/2016/mca_wz_polZ.txt RunII_SM_WZ/2016/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_skimWZ//bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2016_v5_blind_polZ_withtaus/ --showRatio -E SRWZ -l 35.9 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data


#python mcPlots.py RunII_SM_WZ/2017/mca_wz_polZ.txt RunII_SM_WZ/2017/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/trigger_2017/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2017_v5_blind_polZ_withTaus/ --showRatio -E SRWZ -l 41.5 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt


#python mcPlots.py RunII_SM_WZ/2018/mca_wz_polZ.txt RunII_SM_WZ/2018/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/ --Fs {P}/leptonJetReCleanerWZSM/  --Fs {P}/trigger_2018/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2018_v5_blind_polZ_withtaus/ --showRatio -E SRWZ -l 59.8 --sP pol.*cos.* --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt

python mcPlots.py RunII_SM_WZ/2016/mca_wz_polWp.txt RunII_SM_WZ/2016/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_skimWZ//bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2016_v5_blind_polWp_withtaus/ --showRatio -E SRWZ -l 35.9 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data


python mcPlots.py RunII_SM_WZ/2017/mca_wz_polWp.txt RunII_SM_WZ/2017/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/trigger_2017/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2017_v5_blind_polWp_withTaus/ --showRatio -E SRWZ -l 41.5 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt


python mcPlots.py RunII_SM_WZ/2018/mca_wz_polWp.txt RunII_SM_WZ/2018/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/ --Fs {P}/leptonJetReCleanerWZSM/  --Fs {P}/trigger_2018/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2018_v5_blind_polWp_withtaus/ --showRatio -E SRWZ -l 59.8 --sP pol.*cos.* --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt


python mcPlots.py RunII_SM_WZ/2016/mca_wz_polWm.txt RunII_SM_WZ/2016/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_skimWZ//bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2016_v5_blind_polWm_withtaus/ --showRatio -E SRWZ -l 35.9 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data


python mcPlots.py RunII_SM_WZ/2017/mca_wz_polWm.txt RunII_SM_WZ/2017/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/trigger_2017/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2017_v5_blind_polWm_withTaus/ --showRatio -E SRWZ -l 41.5 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt


python mcPlots.py RunII_SM_WZ/2018/mca_wz_polWm.txt RunII_SM_WZ/2018/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/ --Fs {P}/leptonJetReCleanerWZSM/  --Fs {P}/trigger_2018/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2018_v5_blind_polWm_withtaus/ --showRatio -E SRWZ -l 59.8 --sP pol.*cos.* --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt


python mcPlots.py RunII_SM_WZ/2016/mca_wz_polZm.txt RunII_SM_WZ/2016/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_skimWZ//bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2016_v5_blind_polZm_withtaus/ --showRatio -E SRWZ -l 35.9 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data


python mcPlots.py RunII_SM_WZ/2017/mca_wz_polZm.txt RunII_SM_WZ/2017/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/trigger_2017/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2017_v5_blind_polZm_withTaus/ --showRatio -E SRWZ -l 41.5 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt


python mcPlots.py RunII_SM_WZ/2018/mca_wz_polZm.txt RunII_SM_WZ/2018/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/ --Fs {P}/leptonJetReCleanerWZSM/  --Fs {P}/trigger_2018/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2018_v5_blind_polZm_withtaus/ --showRatio -E SRWZ -l 59.8 --sP pol.*cos.* --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt

python mcPlots.py RunII_SM_WZ/2016/mca_wz_polZp.txt RunII_SM_WZ/2016/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2016_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --Fs {P}/trigger_2016/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs /pool/cienciasrw/HeppyTrees/RA7/nanoAODv5_2016_skimWZ//bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2016,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2016,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2016,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2016_v5_blind_polZp_withtaus/ --showRatio -E SRWZ -l 35.9 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data


python mcPlots.py RunII_SM_WZ/2017/mca_wz_polZp.txt RunII_SM_WZ/2017/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2017_skimWZ/ --Fs {P}/leptonPtCorrections/ --FMCs {P}/trigger_prefiring/ --Fs {P}/trigger_2017/ --Fs {P}/leptonJetReCleanerWZSM/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2017,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2017,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2017,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))*weight_PrefiringJets*weight_PrefiringPhotons' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2017_v5_blind_polZp_withTaus/ --showRatio -E SRWZ -l 41.5 --sP pol.*cos.*  --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2017/mcc_triggerdefs.txt


python mcPlots.py RunII_SM_WZ/2018/mca_wz_polZp.txt RunII_SM_WZ/2018/cuts_wzsm.txt RunII_SM_WZ/2016/plots_wz.txt --tree treeProducerSusyMultilepton -P /pool/ciencias/HeppyTrees/RA7/nanoAODv5_2018_skimWZ/ --Fs {P}/leptonPtCorrections/ --Fs {P}/leptonJetReCleanerWZSM/  --Fs {P}/trigger_2018/ --Fs {P}/leptonBuilderWZSM/ --FMCs {P}/leptonMatcher/ --FMCs {P}/bTagEventWeights/ --Fs {P}/bosonPolarization/ --FMCs {P}/bosonPolarization_withTaus/ -L RunII_SM_WZ/functionsWZ.cc -L RunII_SM_WZ/functionsSF.cc -L RunII_SM_WZ/functionsMCMatch.cc --maxRatioRange 0. 1.0 --ratioYLabel Pol/Total --fixRatioRange --print C,pdf,png,txt --legendWidth 0.23 --legendFontSize 0.036 --showMCError --showRatio --perBin -W 'puWeight*bTagWeightDeepCSVT_nom*(getLeptonSF_v4(0,0,2018,LepSel_pt[0],LepSel_eta[0],LepSel_pdgId[0])*getLeptonSF_v4(0,0,2018,LepSel_pt[1],LepSel_eta[1],LepSel_pdgId[1])*getLeptonSF_v4(0,0,2018,LepSel_pt[2],LepSel_eta[2],LepSel_pdgId[2]))' --obj Events -j 96 -f --pdir /nfs/fanae/user/carlosec/www/wz/Legacy/SMWZ_2018_v5_blind_polZp_withtaus/ --showRatio -E SRWZ -l 59.8 --sP pol.*cos.* --ratioNums prompt_WZ_WfL,prompt_WZ_WfR,prompt_WZ_WfO --ratioDen signal --neg --plotgroup data_fakes+=promptsub --xp data --mcc RunII_SM_WZ/2018/mcc_triggerdefs.txt

