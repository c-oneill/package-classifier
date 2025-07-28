# package-classifier
thoughtful.ai code screening

# Package Classification Script

## Overview

This Python script classifies packages into three categories — `STANDARD`, `SPECIAL`, or `REJECTED` — for use in Thoughtful’s robotic automation factory. It uses basic dimension and mass rules to determine how each package should be sorted.

The classification is intended to simulate part of a robotic decision-making pipeline for package handling.

## Classification Rules

Each package is described by its width, height, length (in **centimeters**), and mass (in **kilograms**).

### Criteria

- **Bulky**: A package is considered bulky if:
  - Any single dimension (width, height, or length) is **≥ 150 cm**, or
  - The **volume** (width × height × length) is **≥ 1,000,000 cm³**

- **Heavy**: A package is considered heavy if its mass is **≥ 20 kg**

### Categories

- `STANDARD`: Package is **not heavy** and **not bulky**
- `SPECIAL`: Package is **heavy XOR bulky** (only one of the two)
- `REJECTED`: Package is **both heavy and bulky**

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/package-classifier.git
cd package-classifier
```

### 2. Run the Script

```bash
python3 package_classifier.py
```

### 2. Sample Output

```
Dimensions: (2, 2, 2), Mass: 15, Category: STANDARD
Dimensions: (1, 2, 3), Mass: 25, Category: SPECIAL
Dimensions: (1, 2, 3), Mass: 20, Category: SPECIAL
Dimensions: (100, 100, 100), Mass: 5, Category: SPECIAL
Dimensions: (1, 1, 150), Mass: 5, Category: SPECIAL
Dimensions: (1, 151, 1), Mass: 22, Category: REJECTED
Dimensions: (100, 120, 100), Mass: 22, Category: REJECTED
```

## Testing

```bash
python3 -m unittest test_package_classifier.py
```

## Disclosure
I used OpenAI’s ChatGPT to assist with structuring, documenting, and reviewing parts of this script. All logic, testing, and final implementation decisions are my own.
