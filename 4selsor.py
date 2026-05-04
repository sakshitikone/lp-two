def prac_selec(arr):
    
    if not isinstance(arr, list):
        return "Invalid Input"
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        x = arr.copy()
        return x
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            
            if not isinstance(arr[j], (int, float)):
                return "user please enter only numbers"
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    user_input = input("Enter numbers only: ")
    
    try:
        arr = list(map(float, user_input.strip().split()))
        result = prac_selec(arr)
        print("Sorted Array:", result)
    except ValueError:
        print("Invalid input")
    
if __name__ == "__main__":
    main() 
                
            

