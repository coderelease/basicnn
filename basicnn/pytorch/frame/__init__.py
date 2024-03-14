import torch


def find_device():
    if torch.has_mps:
        return "mps"
    if torch.has_cuda and torch.cuda.is_available():
        return "cuda"

    return "cpu"
