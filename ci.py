import wandb

print(f'The version of wandb is {wandb.__version__}')
version = wandb.__version__

assert version == "0.13.5", 'Expected 0.13.5 got {}'.format(version)