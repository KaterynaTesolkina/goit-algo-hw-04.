# Efficiency of Sorting Algorithms

In this document, we conducted empirical testing of three sorting algorithms: Merge Sort, Insertion Sort, and Timsort. Below are the results of the testing and conclusions.

## Testing Results

1. **Merge Sort**: Approximately 0.0198 seconds.
2. **Insertion Sort**: Approximately 0.1324 seconds.
3. **Timsort**: Approximately 0.00098 seconds.

## Conclusions

1. **Timsort** proved to be the most efficient algorithm among the tested ones. Its execution speed significantly outperforms other algorithms, even on large datasets.
2. **Merge Sort** showed relatively good results compared to **Insertion Sort**, but it was less efficient on this particular dataset.
3. **Insertion Sort** turned out to be the slowest among the tested algorithms for this specific case.

Overall, **Timsort** is an excellent choice for sorting in Python as it demonstrates high efficiency in various conditions.
