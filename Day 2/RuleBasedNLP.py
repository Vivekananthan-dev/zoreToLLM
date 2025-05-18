import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import torch.nn.functional as F

# Sample dataset
data = [
    ("I love this movie", 1),
    ("This is amazing", 1),
    ("I hate this", 0),
    ("This is terrible", 0),
]

# Simple tokenizer and vocabulary
vocab = set(word for sentence, _ in data for word in sentence.lower().split())
word2idx = {word: idx + 1 for idx, word in enumerate(vocab)}  # start indexing from 1
word2idx["<PAD>"] = 0

# Hyperparameters
max_len = 6
embedding_dim = 10
hidden_dim = 16
output_dim = 2
lr = 0.01
epochs = 20

# Encode text
def encode(sentence):
    tokens = sentence.lower().split()
    idxs = [word2idx.get(word, 0) for word in tokens]
    return idxs + [0] * (max_len - len(idxs))  # pad to fixed length

# Custom Dataset
class TextDataset(Dataset):
    def __init__(self, data):
        self.data = data
        self.X = torch.tensor([encode(x) for x, _ in data])
        self.y = torch.tensor([y for _, y in data])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_loader = DataLoader(TextDataset(data), batch_size=2, shuffle=True)

# Simple Model
class SentimentModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc1 = nn.Linear(embed_dim * max_len, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.embedding(x)  # (batch, seq_len, embed_dim)
        x = x.view(x.size(0), -1)  # flatten
        x = F.relu(self.fc1(x))
        return self.fc2(x)

model = SentimentModel(len(word2idx), embedding_dim, hidden_dim, output_dim)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

# Training
for epoch in range(epochs):
    for X_batch, y_batch in train_loader:
        preds = model(X_batch)
        loss = loss_fn(preds, y_batch)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

def predict(text):
    model.eval()
    encoded = torch.tensor([encode(text)])
    with torch.no_grad():
        output = model(encoded)
        pred = torch.argmax(output, dim=1).item()
    return "Positive" if pred == 1 else "Negative"

print(predict(" it love movie "))       # → Positive
print(predict("This is bad"))     # → Negative
