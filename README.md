# Spaminator 📨

**Spaminator** is a simple Python-based spam detection tool.  
It uses keyword matching and scoring rules to classify an email as **spam** or **not spam**.

## ✨ Features
- Detects spammy phrases like *"win"*, *"lottery!"*, *"click here"*, *"viagra"* and more.
- Recognizes "ham-like" (legitimate) phrases such as *"meeting"*, *"project"*, *"thank you"* to reduce false positives.
- Scores suspicious elements like:
  - Excessive exclamation marks
  - All-caps words
  - URLs or domain names
- Lightweight, no external dependencies.

---

## ⚙️ How It Works
1. Reads email content from `email.txt`.
2. Calculates a **spam score**:
   - Increases score for spammy keywords or suspicious formatting.
   - Decreases score for ham-like words.
3. Compares score against a **threshold** (default = `1`).
   - Score ≥ 1 → Classified as **spam**.
   - Score < 1 → Classified as **not spam**.

---
