import torch
model = torch.load("./models/maskgit-vqgan-imagenet-f16-256.bin", map_location="cpu")
print(model.keys())  # 查看加载的内容
