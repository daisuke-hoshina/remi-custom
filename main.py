import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from model import PopMusicTransformer
import argparse

def main():
    parser = argparse.ArgumentParser(description='Pop Music Transformer Generation')
    parser.add_argument('--checkpoint', type=str, default='REMI-tempo-chord-checkpoint', help='Checkpoint path')
    parser.add_argument('--bars', type=int, default=16, help='Number of bars to generate')
    parser.add_argument('--bpm', type=int, default=None, help='Initial BPM (e.g. 120)')
    parser.add_argument('--chord', type=str, default=None, help='Initial chord (e.g. C:maj)')
    parser.add_argument('--output', type=str, default='./result/result.midi', help='Output path')
    parser.add_argument('--prompt', type=str, default=None, help='Path to prompt midi file')
    parser.add_argument('--temperature', type=float, default=1.2, help='Temperature')
    parser.add_argument('--topk', type=int, default=5, help='Top K')
    args = parser.parse_args()

    # declare model
    model = PopMusicTransformer(
        checkpoint=args.checkpoint,
        is_training=False)
    
    print(f"Generating {args.bars} bars to {args.output}...")
    if args.bpm:
        print(f"Initial BPM: {args.bpm}")
    if args.chord:
        print(f"Initial Chord: {args.chord}")

    # generate
    model.generate(
        n_target_bar=args.bars,
        temperature=args.temperature,
        topk=args.topk,
        output_path=args.output,
        prompt=args.prompt,
        initial_chord=args.chord,
        initial_bpm=args.bpm)
        
    # close model
    model.close()

if __name__ == '__main__':
    main()
