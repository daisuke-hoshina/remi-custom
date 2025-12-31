#!/bin/bash
set -e

for i in {1..50}
do
   echo "Generating batch $i/50..."
   python main.py --bars 128 --bpm 120 --chord C:maj --topk 5 --temperature 0.8 --output "data/midi/odstruct_eval/pmt_t0.8_k5/gen_$i.midi" > /dev/null
   python main.py --bars 128 --bpm 120 --chord C:maj --topk 5 --temperature 1.2 --output "data/midi/odstruct_eval/pmt_t1.2_k5/gen_$i.midi" > /dev/null
   python main.py --bars 128 --bpm 120 --chord C:maj --topk 5 --temperature 1.6 --output "data/midi/odstruct_eval/pmt_t1.6_k5/gen_$i.midi" > /dev/null
done
echo "All generations completed."
