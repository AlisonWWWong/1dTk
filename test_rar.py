import torch
state_dict = torch.load("./models/rar_b.bin", map_location="cpu")
print(state_dict.keys())
