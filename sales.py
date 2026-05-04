public class SelectionSortExample {
    public static List<Integer> selectionsort(List<Integer> arr) {
        
        Integer n = arr.size();
        
        for (Integer i = 0; i < n - 1; i++) {
            Integer minIndex = i;
            
            for (Integer j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            Integer temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
        
        return arr;
    }
}