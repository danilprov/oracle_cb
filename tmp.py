with open('results/mslr_T=1000_L=3_e=0.0/lin_0.10000_rewards_1.out') as f:
    rewards = f.read()
rewards = rewards.split('\n')

with open('results/mslr_T=1000_L=3_e=0.0/lin_0.10000_time_1.out') as f:
    time = f.read()
#time = time.split('\n')

with open('results/mslr_T=1000_L=3_e=0.0/lin_0.10000_validation_1.out') as f:
    validation = f.read()
#validation = validation.split('\n')

print('a')