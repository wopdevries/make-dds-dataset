DDS Dataset Generator
This repository provides a standalone tool to generate a dataset of bridge deals in Portable Bridge Notation (PBN) format with corresponding Double Dummy Solver (DDS) results. It is derived from the make-dds-dataset component of the pgx project, designed for reproducibility and public use.
Overview
The repository includes:

make_dds_results.py: Generates random bridge deals and computes DDS results, outputting to results.tsv.
to_bytes.py: Converts results.tsv to a NumPy binary file (results.npy).
ddstable.py: Interfaces with the DDS library (libdds.so).
libdds.so: Precompiled DDS library for Linux x86_64.

The output dataset is suitable for machine learning tasks, such as training models for bridge play.
Prerequisites

Operating System: Tested on Ubuntu 24.04 (Linux x86_64). For other systems, recompile libdds.so (see below).
Python: 3.12.3
Dependencies: numpy, tqdm (listed in requirements.txt).
System Libraries: libgomp1 for libdds.so:sudo apt update
sudo apt install libgomp1



Recompiling libdds.so (Non-Linux Systems)
For macOS, Windows, or other Linux architectures:
git clone https://github.com/dds-bridge/dds.git
cd dds
make
cp libdds.so ~/make-dds-dataset/

Installation

Clone the Repository:
git clone https://github.com/wopdevries/make-dds-dataset.git
cd make-dds-dataset


Set Up Virtual Environment:
python3 -m venv venv
source venv/bin/activate


Install Dependencies:
pip install -r requirements.txt


Set LD_LIBRARY_PATH:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)



Usage

Generate DDS Results:Generate results.tsv with PBN deals and DDS results:
python3 make_dds_results.py --seed 8 --num 100 > results.tsv


--seed: Random seed for reproducibility (e.g., 8).
--num: Number of deals to generate (e.g., 100).
Output: results.tsv (each line: PBN,dds_results).


Convert to NumPy Format:Convert results.tsv to results.npy:
python3 to_bytes.py results.tsv


Output: results.npy (NumPy arrays of keys and values).


Inspect Results:View results.tsv:
head results.tsv

Load results.npy:
import numpy as np
keys, values = np.load('results.npy', allow_pickle=True)
print("Keys shape:", keys.shape)
print("Values shape:", values.shape)
print("First 5 keys:", keys[:5])
print("First 5 values:", values[:5])



File Structure

ddstable.py: Python interface to libdds.so.
libdds.so: Precompiled DDS library (Linux x86_64).
make_dds_results.py: Generates PBN deals and DDS results.
to_bytes.py: Converts results.tsv to results.npy.
requirements.txt: Python dependencies.
.gitignore: Ignores temporary files (e.g., results.tsv, results.npy, tmp.tsv).

Dataset Details

Format: results.tsv contains lines with PBN strings (e.g., N:A2.KT.T763.AKQ87 ...) followed by 20 comma-separated integers representing DDS tricks for each player (N, E, S, W) and denomination (C, D, H, S, NT).
Size: ~11,293 bytes for 100 deals.
Reproducibility: Use --seed for consistent results.

License
MIT License (see LICENSE file, add via GitHub interface if not present).
Citation
If you use this dataset, please cite:

The original pgx repository: github.com/sotetsuk/pgx
The DDS library: github.com/dds-bridge/dds

Contributing
Contributions are welcome! Open an issue or pull request on GitHub.
Contact
For questions, open an issue on GitHub.# make-dds-dataset
