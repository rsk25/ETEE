import json
from multiprocessing import Process, Manager
from typing import List, Dict, Any


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


def get_text(data: List[Dict[Any]]) -> List[str]:
    """
    Get text from the
    :param data: a list of dict type data containing text within each 'text' key
    :return: list of the text
    """
    with Manager() as manager:
        text_data = manager.list()
        processes = []
        for q in data:
            text = q['text']  # 'q' is dictionary consisted of text, equations, explanations etc.
            p = Process(target=list_append_str, args=(text_data, text))
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
    return text_data

