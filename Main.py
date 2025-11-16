from BinarySearch import BinarySearch, gen_binarysearch_data
from LinearSearch import LinearSearch, gen_linearsearch_data
from InsertionSort import InsertionSort, gen_insertionsort_data
from BubbleSort import BubbleSort, gen_bubblesort_data
from MergeSort import MergeSort, gen_merge_data
from BigOcomplexity import BigOAnalyzer
import numpy as np
import pandas as pd

if __name__ == "__main__":
    # binary search
    analyzer = BigOAnalyzer(min_n=100, max_n=10000, multiplier=2, repeats=5)
    result = analyzer.analyze_all(BinarySearch, gen_binarysearch_data, use_args=True)
    analyzer.print_results(result, "BinarySearch(A, n, T)")

    # linear search
    analyzer = BigOAnalyzer(min_n=100, max_n=10000, multiplier=2, repeats=5)
    result = analyzer.analyze_all(LinearSearch, gen_linearsearch_data, use_args=True)
    analyzer.print_results(result, "LinearSearch(A, n, T)")

    # insertion sort
    analyzer = BigOAnalyzer(min_n=100, max_n=5000, multiplier=2, repeats=5)
    result = analyzer.analyze_all(InsertionSort, gen_insertionsort_data, use_args=True)
    analyzer.print_results(result, "InsertionSort(A, n)")

    # bubble sort
    analyzer = BigOAnalyzer(min_n=100, max_n=2000, multiplier=2, repeats=5)
    result = analyzer.analyze_all(BubbleSort, gen_bubblesort_data, use_args=True)
    analyzer.print_results(result, "BubbleSort(A, n)")

    # merge sort
    analyzer = BigOAnalyzer(min_n=100, max_n=10000, multiplier=2, repeats=5)
    result = analyzer.analyze_all(MergeSort, gen_merge_data, use_args=True)
    analyzer.print_results(result, "MergeSort(A, n)")



