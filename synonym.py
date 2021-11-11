from typing import List
import pickle

import nltk
import nlpaug.augmenter.word as naw


def read_pickle(pickle_path='./resource/dataset/', pickle_file='pen_text_only.pkl') -> List[str]:
    with open(pickle_path + pickle_file, 'rb') as pickle_reader:
        text_data = pickle.load(pickle_reader)

    return text_data


if __name__ == '__main__':
    nltk.download('wordnet')
    aug = naw.SynonymAug(aug_src='wordnet')
    text_data = read_pickle()

    text = text_data[0]
    augmented_text = aug.augment(text)
    print("Original: ", text)
    print("Augmented Text: ", augmented_text)

