all: 
	clear 
	# python src/main.py --config=ltscg --env-config=gather with seed=100 use_cuda=False 
	# CUDA_VISIBLE_DEVICES=1 python src/main.py --config=ltscg --env-config=gather with seed=100 use_cuda=True 
	CUDA_VISIBLE_DEVICES=2 python src/main.py --config=ltscg --env-config=gymma with env_args.key="pz-mpe-simple-tag-v3" seed=100 use_cuda=True 
