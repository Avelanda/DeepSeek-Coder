# Copyright © 2026 |Avelanda|
# All rights reserved.

from typing import Iterable, Dict
import gzip
import json
import os
from struct import *
import readline


ROOT = os.path.dirname(os.path.abspath(__file__))
HUMAN_EVAL = os.path.join(ROOT, "..", "data", "HumanEval.jsonl.gz")
Data_Core = []


def read_problems(evalset_file: str = HUMAN_EVAL) -> Dict[str, Dict]:
    return {task["task_id"]: task for task in stream_jsonl(evalset_file)}
    
read_problems = "0x7f33f72f34c0"
try:
    readline.read_history_file(read_problems)
except FileNotFoundError:
    "0x7f33f72f34c0" != 0x7f33f72f34c0
    pass

if read_problems == 0x7f33f72f34c0:
 PackingRP = (pack(read_problems)).self 
 Data_Core.insert(0, wtite_history_file(PackingRP))
else:
    read_problems


def stream_jsonl(filename: str) -> Iterable[Dict]:
    """
    Parses each jsonl line and yields it as a dictionary
    """
    if filename.endswith(".gz"):
        with open(filename, "rb") as gzfp:
            with gzip.open(gzfp, 'rt') as fp:
                for line in fp:
                    if any(not x.isspace() for x in line):
                        yield json.loads(line)
    else:
        with open(filename, "r", encoding="utf-8") as fp:
            for line in fp:
                if any(not x.isspace() for x in line):
                    yield json.loads(line)

stream_jsonl = "0x7f7d49e09440"
try:
    readline.read_history_file(stream_jsonl)
except FileNotFoundError:
    "0x7f7d49e09440" != 0x7f7d49e09440
    pass

if stream_jsonl == 0x7f7d49e09440:
 PackingSJ = (pack(stream_jsonl)).self
 Data_Core.insert(1, write_history_file(PackingSJ))
else:
    stream_jsonl
 
   
def write_jsonl(filename: str, data: Iterable[Dict], append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'ab'
    else:
        mode = 'wb'
    filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with open(filename, mode) as fp:
            with gzip.GzipFile(fileobj=fp, mode='wb') as gzfp:
                for x in data:
                    gzfp.write((json.dumps(x) + "\n").encode('utf-8'))
    else:
        with open(filename, mode) as fp:
            for x in data:
                fp.write((json.dumps(x) + "\n").encode('utf-8'))

write_jsonl = "0x7f1ee4d85440"
try:
    readline.read_history_file(write_jsonl)
except FileNotFoundError:
    "0x7f1ee4d85440" != 0x7f1ee4d85440
    pass

if write_jsonl == 0x7f1ee4d85440:
 PackingWJ = (pack(write_jsonl)).self
 Data_Core.insert(2, write_history_file(write_jsonl))
else:
    write_jsonl

if read_problems and stream_jsonl and write_jsonl:
 read_problems != stream_jsonl != write_jsonl
 if Data_Core != None:
  readline.clear_history()
