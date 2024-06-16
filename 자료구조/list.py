# 트리는 가계도와 같은 계층적인 구조를 표현할 떄 사용할 수 있는 자료구조 

# 루트노드 (root node) : 부모가 없는 최상위 노드 
# 단말 노드 (leaf node) : 자식이 없는 노드 
# 크기 (size)  : 트리에 포함된 모든 노드의 갯수 
# 깊이 depth : 루트 노드부터의 거리
# 높이 (height) : 깊이 중 최댓값
# 차수(degree) : 각 노드의 간선 개수

# 기본적으로 트리의 크기가 N일때 전체 간선의 개수는 N-1이다


# 이진 탐색이 동작할 수 있도록 고안된 효율족인 탐색이 가능한 자료구조의 일종이다
# 이진 탐색 트리의 특징은 
# 왼쪽 자식 노드 < 부모 < 오른쪽 자식 노드로 이동한다 
# 부모 노드보다 왼쪽 자식 노드가 작습니다.
# 부모 노드보다 오른쪽 자식 노드가 큽니다 


#              30 
#     17                48
# 5     23          37      50

# 이진 탐색 트리가 이미 구성되어 있다고 가정하고 데이터를 조회하는 과정
# 찾고자 하는 원소 37 
# 루트노드가 30이고 37를 찾아야하니 오른쪽으로 이동 
# 48보다 37이 작으니 외쪽으로 이동 

# 트리 자료구조에 포함된 노드를 특정한 방법으로 한번씩 방문하는 방법을 의미합니다
# 트리의 정보를 시가적으로 확인 할 수 있다
# 대표적인 트리 순회 방법은 
# 전위 순회 : 루트를 먼저 방문합니다
# 중위 순회 : 왼쪽 자식을 방문한 뒤 루트를 방문
# 후위 순휘 : 오른쪽 자식을 방문하고 루트를 방문
import sys
import heapq
input = sys.stdin.readline

class Node:
    def __init__(self, data, left_node, right_node) :
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
        #전위순회
        def pre_order(node):
            print(node.data, end='')
            if node.left_node != None:
               pre_order(tree[node.left_node])
            if node.right_node != None:
               pre_order(tree[node.right_node])

        #중위순회
        def in_order(node):
            print(node.data, end='')
            if node.left_node != None:
               in_order(tree[node.left_node])
            if node.right_node != None:
               in_order(tree[node.right_node])
            
        #후위순회
        def post_order(node):
            print(node.data, end='')
            if node.left_node != None:
               post_order(tree[node.left_node])
            if node.right_node != None:
               post_order(tree[node.right_node])       
            print(node.data, end='')
            
            n = int(input())
            tree = {}
            
            for i in range(n):
                data, left_node, right_node = input().split()
                if left_node == 'None':
                    left_node = None
                if right_node == 'None':
                    right_node == None
                tree[data] = Node(data, left_node, right_node)
                
                pre_order(tree['A'])
                print()
                in_order(tree['A'])
                print()
                post_order(tree['A'])

#리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 떄는 슬라이싱 slicing을 이용
# 대괄호 안에 콜론을 넣어서 시작이덱스와 끝 인덱스를 설정

# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다


a = [1,2,3,4,5,6,7,8,9]

#네번쨰 원소만 출력하고 싶으면 

print(a[3])
# 두 번쨰 원소부터 네 번쨰 원소까지 
print(a[1:4])


# 리스트 컴프리헨션
# 리스트를 초기화하는 방법 중 하나
# 대괄호 안에 조건문과 반목문을 적용하여 리스트를 초기화 할 수 있다

array = [ i for i in range(10)]
# i는 리스트의 변수로 활용한다 
print(array)

# 0부터 19까지의 수 중에 홀수만 존재하는 리스트 
array2 = [i for i in range(20) if i % 2 ==1]

print(array2)

array2 = [i *i for i in range[1,10]]

print(array2)

# 코드 1 리스트 컴프리헨션
# 0 ~ 19까지의 수 중에서 홀수만 포함하는 리스트
array = [ i for i in range(20) if i %2 ==1]

# 일반적인 코드 (컴프리헨션 X)
array = []
for i in range(20) : 
        if i % 2 == 1 : 
            array.append(i)
            
            
# 리스트 컴프리헨션 2차원 리스트를 초기화 할 떄 효과적으로 사용
# 특히 N*M 크기의 2차원 리스트를 한번에 초기화 해야할 때 매우 유용
# 좋은 예시 array = [[o] * m for _ in range(n)]
# 만약 2차원 리스트를 초기화할 때 다음과 같이 작성하면 예기치 않은 결과가 나온다 
# bad : array = [[0]*m] * n
# 위 코드는 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식된다 
# 변경을 하게 되면 잘 내부가 같은 객체로 인식해서 잘 안될 수 있음 


n=4
m=3 
array = [[0] * m for _ in range(n)]
print(array)



# 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 _를 자주 사용한다 
# code1
summary = 0
for i in range(1,100):
    summary += i
    
    print(summary)
    
#code2
for _ in range(5):
    print("Hello~")    
    
    
    # append 
    # 변수명.append()  리스트에 원소를 하나 삽입할 떄 사용한다 O(1)
    
    #sort() 
    #변수명.sort() 기본 정렬 기능으로 오름차순이다 
    #변수명.sort(reverse = treu) 내림차순으로 정렬한다       O(NlogN)
    
    #reverse()
    #변수명.reverse() 리스트의 원소의 순서를 모두 뒤집어 놓는다 O(n)
    
    #insert() insert(어디에,값) 특정한 인덱스 위치에 원소를 삽입할 떄 사용 O(n)
    
    #count()  변수.count(특정값) 리스트에서 특정한 값을 가지는 데이터의 개수를 셀떄 사용한다  O(n)
    
    # remove 변수.remove(특정 값) 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거 O(n)
    
    a = [4,3,1]
    #원소 뒤집기
    a.reverse()
    print(a)
    # 특정 인덱스에 데이터 추가 
    a.insert(2,3)
    print(a)
    
    
    a.count(3)
    
    
    