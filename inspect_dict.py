import pickle
import sys

checkpoint = 'REMI-tempo-chord-checkpoint'
dictionary_path = '{}/dictionary.pkl'.format(checkpoint)

try:
    event2word, word2event = pickle.load(open(dictionary_path, 'rb'))
    
    print("--- Tempo Classes ---")
    tempos = [k for k in event2word.keys() if 'Tempo Class' in k]
    print(sorted(tempos)[:10]) # Show first 10
    
    print("\n--- Tempo Values ---")
    tempo_vals = [k for k in event2word.keys() if 'Tempo Value' in k]
    print(sorted(tempo_vals))
    
    print("\n--- Chords ---")
    chords = [k for k in event2word.keys() if 'Chord' in k]
    print(sorted(chords)[:20])

except Exception as e:
    print(e)
