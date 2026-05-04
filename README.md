To execute Debug ( Open Execute Anonymous Window and paste this 
List<Integer> numbers = new List<Integer>{64, 25, 12, 22, 11};
System.debug('Original List: ' + numbers);
List<Integer> sortedList = SelectionSortExample.selectionSort(numbers);
System.debug('Sorted List: ' + sortedList);
