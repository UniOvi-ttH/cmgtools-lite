import os
from multiprocessing import Pool

## this script creates a sub-directory in the tree path for a given module
## and runs the friend tree producer for this module

batch = True
queue = "batch" #"batch" for Oviedo, "8nh" or others for lxplus
path  = "/pool/ciencias/HeppyTrees/ttH/"
#path  = "trees/"
force = True # if the friend tree already exists, module is not run; set to True to still run it
print 'here'
## first: module to run, second: list of modules (comma separated) that are required to run
modules = [
#	["leptonJetReCleanerTTH", ""]
#	["ttH2lss","leptonJetReCleanerTTH"],
	["kinMVA_2D_2lss_3l","leptonJetReCleanerTTH,ttH2lss"]
	
#	["ttHLepMEMFriend", ""],
#	["eventBTagWeight","leptonJetReCleanerTTH"]
	#["fastCombinedObjectRecleaner", ""]
	#["leptonJetReCleanerSusyEWK2L" , ""                            ],
        #  ["leptonJetReCleanerSusyEWK3L" , ""                            ],
          #["WZCRvars"                   , "leptonJetReCleanerSusyEWK2L" ],
          #["leptonBuilderEWK"           , "leptonJetReCleanerSusyEWK3L" ],
          #["leptonJetReCleanerSusyRA7"           , "" ],
          #["leptonBuilderRA7"           , "leptonJetReCleanerSusyRA7" ],
          #["leptonJetReCleanerWZSM"           , "" ],
          #["leptonBuilderWZSM"                , "leptonJetReCleanerWZSM" ],
         ] 

## in case you want to run only specific samples
accept = ['SingleElectron_Run2016B_23Sep2016_v3_runs_273150_275376_part8'
#'MuonEG_Run2016H-PromptReco-v2_runs_281613_284035'
	#'TTTT',
	  #"WZTo3LNu",
        #"WGToLNuG",
        #"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part1",
        #
        #"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part2",
        #
        #"DoubleMuon_Run2016F_23Sep2016_v1_runs_271036_284044_part2",
        #
        #"DoubleMuon_Run2016G_23Sep2016_v1_runs_271036_284044_part5",
        #@@"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part2",
        #@@"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part3",
        #@@"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part4",
        #@@"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part5",
        #@@"DoubleMuon_Run2016F_23Sep2016_v1_runs_271036_284044_part2",
        #@@"DoubleMuon_Run2016G_23Sep2016_v1_runs_271036_284044_part3",
        ##"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part3",
        #
        #"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part4",
        #
        #
        #"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part5",
        #
        #"DoubleMuon_Run2016G_23Sep2016_v1_runs_271036_284044_part3",
         #"DoubleEG_Run2016G_23Sep2016_v1_runs_271036_284044_part5",
        ###"JetHT_Run2016B_23Sep2016_v3_runs_273150_275376_part1",
        ###"MET_Run2016H-PromptReco-v3_runs_284036_284044",
        ###"SingleMuon_Run2016H-PromptReco-v3_runs_284036_284044",
        #"DoubleMuon_Run2016G_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleMuon_Run2016G_23Sep2016_v1_runs_271036_284044_part5",
        #"DoubleMuon_Run2016G_23Sep2016_v1_runs_271036_284044_part7",
        #"DoubleMuon_Run2016G_23Sep2016_v1_runs_271036_284044_part7",
        #
        #"DoubleEG_Run2016B_23Sep2016_v3_runs_273150_275376_skimmed_part1",
        #"DoubleEG_Run2016D_23Sep2016_v1_runs_271036_284044_part4",
        #"DoubleEG_Run2016E_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleEG_Run2016H-PromptReco-v2_runs_281613_284035_part4",
        #"DoubleMuon_Run2016B_23Sep2016_v3_runs_273150_275376_skimmed_part1",
        #"DoubleMuon_Run2016B_23Sep2016_v3_runs_273150_275376_skimmed_part3",
        #"DoubleMuon_Run2016B_23Sep2016_v3_runs_273150_275376_skimmed_part6",
        #"DoubleMuon_Run2016H-PromptReco-v2_runs_281613_284035_part10",
        #"TTJets_SingleLeptonFromTbar_part2",
        #"TTJets_SingleLeptonFromTbar_part3",
        #"Run2016G",
        #"Run2016F",
        #"DoubleEG_Run2016E_23Sep2016_v1_runs_271036_284044_part2"
        #"DYJetsToLL_M50_LO_part2",
        #"TTJets_SingleLeptonFromT_part3",
        #"TTJets_SingleLeptonFromTbar_part1",
        #"SingleLeptonFromTbar_part2",
        #"SingleLeptonFromTbar_part3",
        #"DoubleEG_Run2016B_23Sep2016_v3_runs_273150_275376_part1",
        #"DoubleEG_Run2016B_23Sep2016_v3_runs_273150_275376_part3",
        #"DoubleEG_Run2016B_23Sep2016_v3_runs_273150_275376_part4",
        #"DoubleEG_Run2016C_23Sep2016_v1_runs_271036_284044_part1",
        #"DoubleEG_Run2016D_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleEG_Run2016D_23Sep2016_v1_runs_271036_284044_part4",
        #"DoubleEG_Run2016E_23Sep2016_v1_runs_271036_284044_part1",
        #"DoubleEG_Run2016E_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleEG_Run2016H-PromptReco-v2_runs_281613_284035_part4",
        #"DoubleEG_Run2016H-PromptReco-v2_runs_281613_284035_part5",
        #"SingleElectron_Run2016E_23Sep2016_v1_runs_271036_284044",
        #"DoubleEG_Run2016B_23Sep2016_v3_runs_273150_275376_part1",
        #"DoubleEG_Run2016B_23Sep2016_v3_runs_273150_275376_part3",
        #"DoubleEG_Run2016B_23Sep2016_v3_runs_273150_275376_part4",
        #"DoubleEG_Run2016C_23Sep2016_v1_runs_271036_284044_part1",
        #"DoubleEG_Run2016D_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleEG_Run2016D_23Sep2016_v1_runs_271036_284044_part4",
        #"DoubleEG_Run2016E_23Sep2016_v1_runs_271036_284044_part1",
        #"DoubleEG_Run2016E_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleEG_Run2016H-PromptReco-v2_runs_281613_284035_part4",
        #"DoubleEG_Run2016H-PromptReco-v2_runs_281613_284035_part5",
        #"DoubleMuon_Run2016B_23Sep2016_v3_runs_273150_275376_part10",
        #"DoubleMuon_Run2016B_23Sep2016_v3_runs_273150_275376_part9",
        #"DoubleMuon_Run2016C_23Sep2016_v1_runs_271036_284044_part2",
        #"DoubleMuon_Run2016C_23Sep2016_v1_runs_271036_284044_part1",
        #"DoubleMuon_Run2016D_23Sep2016_v1_runs_271036_284044_part1",
        #"DoubleMuon_Run2016D_23Sep2016_v1_runs_271036_284044_part6",
        #"DoubleMuon_Run2016E_23Sep2016_v1_runs_271036_284044_part1",
        #"MuonEG_Run2016H-PromptReco-v2_runs_281613_284035",
        #"SingleElectron_Run2016E_23Sep2016_v1_runs_271036_284044",
        #"SingleMuon_Run2016H-PromptReco-v3_runs_284036_284044",
        #"WWZ"
          #"TChiNeuSlepSneu_mCh450_mChi300",
          #"TChiNeuSlepSneu_mCh300_mChi270",
          #"TChiNeuSlepSneu_mCh750_mChi100"
          #"TChiNeuWZ_mCh150_mChi120",
          #"TChiNeuWZ_mCh200_mChi100",
          #"TChiNeuWZ_mCh350_mChi100",
          #"TChiNeuWZ_mCh350_mChi20"
          #  "TChiNeuWZ_mCh350_mChi20"
          # "T6ttWW_mG_1000_mN_100",
          #"T6ttWW_mG_1200_mN_100",
          #"T1tttt_mG_1200_mN_900",
          #"T1tttt_mG_1300_mN_1000",
          #"T1tttt_mG_1400_mN_1100",
          #"T1tttt_mG_1500_mN_1200",
          #"T1tttt_mG_1600_mN_1300",
          #"1250_mN_950",
          #"800_mN_700",
          #"DYJets"
          #"TGJets",
          #"TTGJets",
          #"TTJets_Di",
          #"TTJets_Single",
          #"TTLL",
          #"TTW",
          #"TTZ",
          #"TTW",
          #"TTWTo",
          #"TTZTo",
          #"TTH",
          #"TBar",
          #"TTHnobb_pow",
          #"tZq",
          #"VH",
          #"WG",
          #"ZG",
          #"WWZ",
          #"WZZ",
          #"ZZZ",
          #"ZZTo4L",
          #"WWTo2L2Nu",
          #"TTTT",
          #"FromTbar",
          #"romT",
          #"WZTo3LNu",
          #"T5qqqqVV_noDM_mG_1000_mN_100",
          #"MuonEG_Run2016B",
          #"GGHZZ",
          #"Run",
          #"DYJetsToLL_M10to50_LO",
          #"DYJetsToLL_M50_LO",
          #"DoubleMuon_Run2016B_PromptReco_v2_runs_275126_275783",
          #"T1tttt",
          #"T5qqqq",
          #"T6ttWW",
         ]

#annot open file evVarFriend_SingleMuon_Run2016D_PromptReco_v2_runs_276284_276811.chunk68.root  cannot open file evVarFriend_DoubleEG_Run2016D_PromptReco_v2_runs_276284_276811.chunk14.root

## in case you want to exclude specific samples
exclude = [#"_SS",
           #"_OS",
           #"_TD",
           #"_LO",
           #"Tau",
           #"TChi",
           #"WZTo3LNu",
           #"DoubleEG",
           #"DoubleMuon",
           #"MuonEG",
           #"ZToMuMu",
           #"QCD",
           #"50to",
           #"amcatnlo",
           #"Run",
           #"runs_273150_275125",
           #"TTW","TTZ",
           #"WZTo3LNu"
           #"amcatnlo",
          ]

## --------------- do not touch beyond this line ---------------

def cmd(cmd):
	print cmd
	os.system(cmd)

def mkdir(path):
	if os.path.isdir(path): return
	cmd("mkdir " + path)

def submit(sample, module):
	print 'meh'
	global batch, queue, path
	super = "python prepareEventVariablesFriendTree.py " + path + " " + path + "/" + module[0] + " -d " + sample + "   --tra2     --tree treeProducerSusyMultilepton -m " + module[0]
	if not module[1].strip() == "":
		sm = module[1].strip().split(",")
		for f in sm: super += " -F sf/t " + path + "/" + f + "/evVarFriend_" + sample + ".root"
	if batch:
		#super += " --env cern -q " + queue + " -N 50000 --log " + path + "/" + module[0] + "/log"
		super += " -q " + queue + " -N 5000000 --env oviedo"
	cmd(super)


path = path.rstrip("/")
listdir = os.listdir(path)

def parallelSubmission(module_d):
	module = module_d[0]
	d = module_d[1]

	if not os.path.isdir(path + "/" + d): return None
	if not ( os.path.exists(path + "/" + d + "/treeProducerSusyMultilepton/tree.root") or os.path.exists(path + "/" + d + "/treeProducerSusyMultilepton/tree.root.url") ): return None
	if not force and os.path.exists(path + "/" + module[0] + "/evVarFriend_" + d + ".root"): return None
	if accept  != [] and all([d.find(a) == -1 for a in accept ]): return None
	if exclude != [] and any([d.find(e) >  -1 for e in exclude]): return None 
	submit(d, module)

for module in modules:
	mkdir( module[0])
	listJobs = []
	pool = Pool(1)
	for d in listdir: 
		listJobs.append( [module, d] )
	pool.map(parallelSubmission, listJobs)
	# for d in listdir: 
	# 	if not os.path.isdir(path + "/" + d): continue
	# 	if not ( os.path.exists(path + "/" + d + "/treeProducerSusyMultilepton/tree.root") or os.path.exists(path + "/" + d + "/treeProducerSusyMultilepton/tree.root.url") ): continue
	# 	if not force and os.path.exists(path + "/" + module[0] + "/evVarFriend_" + d + ".root"): continue
	# 	if accept  != [] and all([d.find(a) == -1 for a in accept ]): continue
	# 	if exclude != [] and any([d.find(e) >  -1 for e in exclude]): continue
	# 	submit(d, module)

