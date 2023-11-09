import wandb

print(f'The version of wandb is {wandb.__version__}')
version = wandb.__version__

assert version == "0.16.0", 'Expected 0.16.0 got {}'.format(version)
