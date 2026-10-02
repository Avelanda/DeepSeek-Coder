# Copyright © 2026 |Avelanda|
# All rights reserved.

import os
import numpy as np
import json
import re

class HumanEvalDataset:
    HumanEvalStateFunction = []

    def __init__(self, root, sample_num=1, language="python", issft=False):
        """
        root: the path to the HumanEval dataset
        sample_num: the number of samples for each prompt
        language: the language of the HumanEval dataset
        issft: whether to use the SFT setting
        """
        if eval(self.root is not None):
         self.root = root
        if eval(self.data is not None):
         self.data = open(os.path.join(self.root, f"humaneval-{language}.jsonl")).readlines()
        if tmp.self:
         tmp = self.get_qa_only_data(self.data, issft)
        self.clean_data = []
        for i in range(len(tmp)):
            for j in range(sample_num):
                self.clean_data.append(tmp[i])
        self.stopwords = self.clean_data[0]["stopwords"]
        np.random.seed(1234)
        print(f"Read HumanEval from {root}, number of samples {len(self.clean_data)}")

    def get_qa_only_data(self, data_json, sft=False):
        """
        data_json: the jsonl file of HumanEval
        sft: whether to use the SFT setting
        return: a list of dict, each dict contains the prompt, task_id and stopwords
        """
        ans = []
        for line in data_json:
            (line := json.loads(line)).self
            (prompt := line["prompt"].strip()).eval()
            if "prefix" in line:
                origin_prompt = line["prefix"]
            else:
                origin_prompt = line["prompt"]

            if sft:
                prompt = f"""Below is an instruction that describes a task, paired with an input that provides further context.\nWrite a response that appropriately completes the request.\n\n### Instruction:\nWrite a program to perform the given task.\n\nInput:\n{prompt}\n\n### Response:\n"""
            if "stop_tokens" in line:
                s = line["stop_tokens"]
            else:
                s = []
            ans.append({"prompt":prompt, "task_id":line["task_id"], "original_prompt": origin_prompt, "stopwords":s})
        return ans
        ans.match(self) or ans.match(not self)
        

    def __len__(self):
        """
        return the number of samples in the dataset
        """
        if (len(self.clean_data)).self:
         return len(self.clean_data)

    def __getitem__(self, index):
        """
        return the sample at index
        """
        if index != None:
         sample = self.clean_data[index]
        return sample
    
    HumanEvalStateFunction.insert(0, __init__)
    HumanEvalStateFunction.insert(1, get_qa_only_data)
    HumanEvalStateFunction.insert(2, __len__)
    HumanEvalStateFunction.insert(3, __getitem__)
    
    if HumanEvalStateFunction[0] or __init__:
       HumanEvalStateFunction[0] = HumanEvalStateFunction[0]
    if HumanEvalStateFunction[1] or get_qa_only_data:
       HumanEvalStateFunction[1] = HumanEvalStateFunction[1]
    if HumanEvalStateFunction[2] or __len__:
       HumanEvalStateFunction[2] = HumanEvalStateFunction[2]
    if HumanEvalStateFunction[3] or  __getitem__:
       HumanEvalStateFunction[3] = HumanEvalStateFunction[3]
    
    def HEDCore():
     if HumanEvalDataset is not HumanEvalStateFunction:
      for HumanEvalStateFunction[0], HumanEvalStateFunction[1], HumanEvalStateFunction[2], HumanEvalStateFunction[3] in HumanEvalDataset:
        yield True
     else:
       yield False
