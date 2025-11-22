from algoritma import (
    linear_search,
    binary_search,
    bubble_sort,
    insertion_sort,
    merge_sort,
    compare_search_algorithms,
    compare_sorting_algorithms
)

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("ANALISIS KOMPLEKSITAS ALGORITMA")
    print("=" * 70)
    
    # Demo dengan array kecil
    print("\n--- DEMO DENGAN ARRAY KECIL ---")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_arr}")
    
    # Search demos
    target = 22
    idx, comps = linear_search(test_arr, target)
    print(f"\nLinear Search untuk {target}: index {idx}, {comps} komparasi")
    
    sorted_test = sorted(test_arr)
    idx, comps = binary_search(sorted_test, target)
    print(f"Binary Search untuk {target}: index {idx}, {comps} komparasi")
    
    # Sorting demos
    print(f"\n--- SORTING DEMO ---")
    
    arr1 = test_arr.copy()
    sorted_arr, comps, swaps = bubble_sort(arr1)
    print(f"Bubble Sort: {sorted_arr}")
    print(f"  Comparisons: {comps}, Swaps: {swaps}")
    
    arr2 = test_arr.copy()
    sorted_arr, comps, shifts = insertion_sort(arr2)
    print(f"Insertion Sort: {sorted_arr}")
    print(f"  Comparisons: {comps}, Shifts: {shifts}")
    
    arr3 = test_arr.copy()
    sorted_arr, comps = merge_sort(arr3)
    print(f"Merge Sort: {sorted_arr}")
    print(f"  Comparisons: {comps}")
    
    # Full comparison dengan data besar
    print("\n")
    compare_search_algorithms(arr_size=5000, num_tests=5)
    compare_sorting_algorithms(arr_size=1000, num_tests=3)
    
    print("\n" + "=" * 70)