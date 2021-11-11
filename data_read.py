import json
from typing import List, Dict, Any
import pickle

def list_append_str(lst: List[Any], s: str):
    lst.append(s)


def read_json(path) -> List[Any]:
    """
    Read text from json file
    :param path: the path to json file
    :return: list type data
    """
    with open(path, 'r+', encoding='utf-8') as data_reader:
        data = json.load(data_reader)

    return data


def write_text_only(text_data: List[str], path: str='./resource/dataset/', filename: str='pen_text_only.pkl'):
    with open(path+filename, 'wb') as pickle_writer:
        pickle.dump(text_data, pickle_writer)


if __name__ == '__main__':
    data = read_json('./resource/dataset/pen.json')

    text_data = []
    for q in data:
        text = q["text"]
        text_data.append(text)

    write_text_only(text_data)



