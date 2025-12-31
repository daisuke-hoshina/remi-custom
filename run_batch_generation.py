import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from model import PopMusicTransformer
import argparse

def main():
    print("Initializing model...")
    checkpoint = 'REMI-tempo-chord-checkpoint'
    model = PopMusicTransformer(
        checkpoint=checkpoint,
        is_training=False)
    
    # Conditions
    conditions = [
        {'temp': 0.8, 'dir': 'data/midi/odstruct_eval/pmt_t0.8_k5'},
        {'temp': 1.2, 'dir': 'data/midi/odstruct_eval/pmt_t1.2_k5'},
        {'temp': 1.6, 'dir': 'data/midi/odstruct_eval/pmt_t1.6_k5'}
    ]
    
    n_files = 3
    bars = 16
    # bpm 120, chord C:maj
    initial_bpm = 120
    initial_chord = 'C:maj'
    topk = 5
    
    for i in range(1, n_files + 1):
        print(f"Generating set {i}/{n_files}...")
        for cond in conditions:
            temp = cond['temp']
            out_dir = cond['dir']
            output_path = f"{out_dir}/gen_{i}.midi"
            
            # Skip if already exists (optional, but good for resuming)
            # if os.path.exists(output_path):
            #     continue
            
            print(f"  - Temp {temp} -> {output_path}")
            model.generate(
                n_target_bar=bars,
                temperature=temp,
                topk=topk,
                output_path=output_path,
                prompt=None,
                initial_chord=initial_chord,
                initial_bpm=initial_bpm)
            
    model.close()
    print("Done.")

if __name__ == '__main__':
    main()
