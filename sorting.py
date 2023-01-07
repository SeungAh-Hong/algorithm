## 1. Selection
def selection(arr): ## 앞에서부터 값 하나씩 뒤의 모든 값 확인 (O(n^2))
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i] ## 자리 스왑

## 2. Bubble
def bubble(arr): ## 앞에서부터 인접한 두 수 확인 (O(n^2))
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion(arr):
    n = len(arr)
    for i in range(1, n): ## 두번째 수부터 앞의 배열들과 비교하여 추가
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

## 3. Merge
def merge(arr): ## 분할 정복 & 재귀
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2 ## 반 쪼개서 정렬 -> 합쳐서 정렬
    low_arr = merge(arr[:mid])
    high_arr = merge(arr[mid:])

    merge_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[h])
            h += 1
    ## 마지막 남은 수 배열에 추가
    merge_arr += low_arr[l:]
    merge_arr += high_arr[h:]


## 4. Quick (기본 구현)
def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    l_arr, e_arr, r_arr = [], [], [] ## pivot 기준으로 왼쪽 / 오른쪽 배열 나누어서 재귀
    for num in arr:
        if num < pivot:
            l_arr.append(num)
        elif num > pivot:
            r_arr.append(num)
        else: ## pivot 자신
            e_arr.append(num)
    return quick(l_arr) + e_arr + quick(r_arr) ## 두 배열에 대해 재귀 후 return
# 재귀 호출의 결과를 다시 크기 순으로 합치면 정렬된 리스트를 얻을 수 있음  


## 4. Quick (최적화 구현)
def quick(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high) ## swap
        sort(low, mid - 1) ## mid 기준 왼쪽 정렬 (재귀)
        sort(mid, high) ## mid 기준 오른쪽 정렬 (재귀)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot: ## 왼쪽정렬인데 피봇보다 크면 stop
                low += 1
            while arr[high] > pivot: ## 오른쪽정렬인데 피봇보다 작으면 stop
                high -= 1
            if low <= high: ## stop된 경우
                arr[low], arr[high] = arr[high], arr[low] ## swap
                low, high = low + 1, high - 1 ## idx 고침 (이미 low, high까지 확인됐으니까)
        return low

    sort(0, len(arr) - 1)
    return

## 6. Heap
def heap(arr):
    def heapify(arr, index, heap_size):  ## 부모 노드 <-> 자식 노드 비교해서 최대 힙 구성
        largest = index ## 부모 노드 index
        left_index = 2 * index + 1 # 왼쪽 자식 노드
        right_index = 2 * index + 2 # 오른쪽 자식 노드
        if left_index < heap_size and arr[left_index] > arr[largest]:
            ## 왼쪽 자식 노드가 부모 노드보다 더 클 경우 swap (왼쪽 우선 적용)
            largest = left_index
        if right_index < heap_size and arr[right_index] > arr[largest]:
            ## 오른쪽 자식 노드가 부모 노드보다 더 클 경우 swap
            largest = right_index
        if largest != index: ## swap해야하는 경우
            arr[largest], arr[index] = arr[index], arr[largest]
            heapify(arr, largest, heap_size) ## 재귀

    n = len(arr)
    # BUILD-MAX-HEAP (A) : 위의 1단계
    # 인덱스 : (n을 2로 나눈 몫-1)~0
    # 최초 힙 구성시 배열의 중간부터 시작하면 
    # 이진트리 성질에 의해 모든 요소값을 
    # 서로 한번씩 비교할 수 있게 됨 : O(n)
    ## 최대 힙을 구성하게 되면 arr의 첫번째 요소(16)가 전체 요소 가운데 최댓값이 됨(root node)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n) ## build heap : 위에서 아래로 heapify
    # Recurrent (B) : 2~4단계
    # 한번 힙이 구성되면 개별 노드는
    # 최악의 경우에도 트리의 높이(logn)
    # 만큼의 자리 이동을 하게 됨
    # 이런 노드들이 n개 있으므로 : O(nlogn)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i) ## 위에서 아래로 heapify
    return arr

## 7. Radix
def radix(arr):
    def countingSort(arr, digit):
        n = len(arr)
    
        # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성
        output = [0] * (n)
        count = [0] * (10)
        
        # digit, 자릿수에 맞는 count에 +=1 해줌
        for i in range(0, n):
            index = arr[i]//digit
            count[(index)%10] += 1
    
        # 누적 count를 세기
        for i in range(1,10):
            count[i] += count[i-1]  
     
        # 결과 배열, output을 설정
        i = n-1 ## len(arr)-1만큼 반복
        while i >= 0: ## 배열 맨 끝에서부터 반복함
            index = arr[i]//digit
            output[count[(index)%10]-1] = arr[i] 
            ## count는 1부터 시작했으니까 idx에서는 -1 한 후 arr 원소 넣어줌
            count[(index)%10] -= 1 # 넣었으면 -1 해주기
            i -= 1

        #arr를 결과물에 다시 재할당
        for i in range(0,len(arr)): 
            arr[i] = output[i]
    

    # arr 배열중에서 maxValue를 잡아서 어느 자릿수까지 반복하면 될지를 정함
    maxValue = max(arr)  
    #자릿수마다 countingSorting을 시작
    digit = 1
    while maxValue//digit > 0:
        countingSort(arr,digit)
        digit *= 10
    
    return