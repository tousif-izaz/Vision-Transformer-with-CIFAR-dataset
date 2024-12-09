import torch
print(torch.version.cuda)
print(torch.cuda.is_available())  # Should return True if CUDA is available
print(torch.cuda.device_count())