
# 📊 Ultima_CRAM_Stat_py

A Python script to generate basic quality statistics from a CRAM file using pysam.

---

## 🚀 Usage

```bash
python Ultima_CRAM_Stat.py [path_to_cram_file]
# Example:
python Ultima_CRAM_Stat.py sample1.cram
```

---

## 📝 Description

This script processes a CRAM file and outputs a summary of key sequencing quality metrics, including:

- Total number of bases
- Total number of reads
- Base composition (A, T, G, C, N counts)
- N base percentage
- GC content percentage
- Q20 and Q30 base counts and percentages
- Average read length

The results are saved in a text file named `[Sample_Name].sqs`.

---

## 📂 Output Example

The output file will look like:

```
Sample Name: sample1
Total Bases: 1,234,567
Total Reads: 12,345
N Percentage: 0.12%
GC Content: 48.76%
Q20 Percentage: 97.45%
Q30 Percentage: 92.13%
A base count: 300,000
T base count: 310,000
G base count: 310,000
C base count: 300,000
N base count: 1,567
Q20 Bases: 1,203,456
Q30 Bases: 1,137,890
Average Read Length: 100.12
------------------------------------------------------
```

---

## ⚙️ Requirements

- Python 3.x
- [pysam](https://pysam.readthedocs.io/en/latest/)

Install dependencies with:

```bash
pip install pysam
```

---

## 🏷️ Arguments

| Argument           | Description                                 |
|--------------------|---------------------------------------------|
| `[path_to_cram_file]` | Path to the input CRAM file                |

---

## 💡 Notes

- The script expects a single CRAM file as input.
- The output summary file will be created in the same directory as the script.
- Make sure the CRAM file is accessible and not corrupted.

---
