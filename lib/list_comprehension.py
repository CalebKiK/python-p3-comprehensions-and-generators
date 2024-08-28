#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [n for n in num_list if n % 2 == 0]
    if len(even_nums) < 1:
        print([])
        return []
    
    else:
        print(even_nums)
        return even_nums

def make_exclamation(sentence_list):
    if len(sentence_list) <= 0:
        print([])
        return []
    
    else:
        string_exclamation = [word + "!" for word in sentence_list]
        print(string_exclamation)
        return string_exclamation