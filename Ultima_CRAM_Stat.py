# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import time
import os
import pysam

if len(sys.argv) != 2:
    raise ValueError("Usage: python Ultima_CRAM_Stat.py [path of cram file]")

# Set CRAM File path and sample name
cram_file_path = sys.argv[1]
sample_name = os.path.splitext(os.path.basename(cram_file_path))[0]

def process_cram_file_with_pysam(cram_file_path):
    # Calculating CRAM file stat 
    total_bases = 0
    total_reads = 0
    total_length = 0
    base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'N': 0}
    q20_bases = 0
    q30_bases = 0

    # USE PYSAM
    with pysam.AlignmentFile(cram_file_path, "rc", check_sq=False) as cramfile:
        for read in cramfile.fetch(until_eof=True):
            seq = read.query_sequence or ""  
            qual = read.query_qualities or []
            total_reads += 1
            read_length = len(seq)
            total_length += read_length
            total_bases += read_length
            for base in seq:
                if base in base_counts:
                    base_counts[base] += 1
            for quality_score in qual:
                if quality_score >= 20:
                    q20_bases += 1
                if quality_score >= 30:
                    q30_bases += 1

    if total_reads > 0:
        avg_read_length = total_length / total_reads
    else:
        avg_read_length = 0

    return (total_bases, total_reads, base_counts, q20_bases, q30_bases, avg_read_length)

def print_summary_to_file(sample_name, total_bases, total_reads, base_counts, q20_bases, q30_bases, avg_read_length):
    output_file = "{}.sqs".format(sample_name)
    with open(output_file, "w") as f:
        if total_bases > 0:
            q_20p = round(q20_bases * 100.0 / total_bases, 2)
            q_30p = round(q30_bases * 100.0 / total_bases, 2)
            Np = round(base_counts['N'] * 100.0 / total_bases, 2)
            gc_content = round((base_counts['G'] + base_counts['C']) * 100.0 / total_bases, 2)
        else:
            q_20p = 0
            q_30p = 0
            Np = 0
            gc_content = 0

        f.write("Sample Name: {}\n".format(sample_name))
        f.write("Total Bases: {:,}\n".format(total_bases))
        f.write("Total Reads: {:,}\n".format(total_reads))
        f.write("N Percentage: {}%\n".format(Np))
        f.write("GC Content: {}%\n".format(gc_content))
        f.write("Q20 Percentage: {}%\n".format(q_20p))
        f.write("Q30 Percentage: {}%\n".format(q_30p))
        for base in ['A', 'T', 'G', 'C', 'N']:
            f.write("{} base count: {:,}\n".format(base, base_counts[base]))
        f.write("Q20 Bases: {:,}\n".format(q20_bases))
        f.write("Q30 Bases: {:,}\n".format(q30_bases))
        f.write("Average Read Length: {:.2f}\n".format(avg_read_length))
        f.write("------------------------------------------------------\n")

start_time = time.time()
total_bases, total_reads, base_counts, q20_bases, q30_bases, avg_read_length = process_cram_file_with_pysam(cram_file_path)
print_summary_to_file(sample_name,total_bases=total_bases,total_reads=total_reads,base_counts=base_counts,q20_bases=q20_bases,q30_bases=q30_bases,avg_read_length=avg_read_length)
end_time = time.time()
execution_time = end_time - start_time
print("Execution Time: {:.2f} seconds".format(execution_time))
