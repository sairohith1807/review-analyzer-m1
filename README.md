# Review Analyzer

A lightweight Python tool for classifying customer product reviews.

## Purpose
Classify short customer reviews as `positive`, `negative` or `unknown` using
simple keyword rules. It is a teaching project for Git/GitHub workflows; no
machine-learning training is involved.

## Prerequisites
- Python 3.8 or newer
- Git

No third-party packages are required.

## Installation
```bash
git clone https://github.com/sairohith1807/review-analyzer-m1.git
cd review-analyzer-m1
```

## Run
```bash
python3 app.py        # prints the classification of a sample review
python3 test_app.py   # runs the assertions
```

## Example input / output
| Input                              | Output     |
|------------------------------------|------------|
| `"Good product"`                   | `positive` |
| `"Bad quality, broke after a day"` | `negative` |
| `"It arrived on time"`             | `unknown`  |

## Project structure
```
review-analyzer/
├── app.py         # normalize_review() and classify_review()
├── test_app.py    # assertions for normalization and classification
├── README.md      # this file
└── .gitignore     # excludes caches, virtual environments and .env
```
