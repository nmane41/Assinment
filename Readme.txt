
Binary Search :-

Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array.
If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty.

The time complexity of Binary Search can be written as

T(n) = T(n/2) + c


Sequential Search :-

Sequential Search is the most natural searching method.
In this method, the searching begins with searching every element of the list till the required record is found.
It makes no demands on the ordering of records. It takes considerably amount of time and is slower.

