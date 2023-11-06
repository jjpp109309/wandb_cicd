import wandb

print(f'The version of wandb is {wandb.__version__}')
version = wandb.__version__
assert version == "0.15.12", 'Expected 2.2 got {}'.format(version)
