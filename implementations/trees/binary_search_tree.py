class Node():
    def __init__(self, data):
        '''
        summary :
            노드의 데이터를 초기화하고, 좌/우 자식 노드를 None으로 설정합니다.

        args :
            data : 노드에 저장할 데이터 값
        '''
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        '''
        summary :
            이진 탐색 트리를 초기화합니다. 루트 노드는 None으로 설정됩니다.
        '''
        self.root = None
    
    def insert(self, data):
        '''
        summary :
            새로운 데이터를 트리에 삽입합니다.

        args :
            data : 트리에 삽입할 데이터 값
        '''
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right
        
    def delete(self, data):
        '''
        summary :
            트리에서 특정 데이터를 삭제합니다.

        args :
            data : 트리에서 삭제할 데이터 값
        '''
        self.root = self._delete_node(self.root, data)
    
    def _delete_node(self, node, data):
        '''
        summary :
            특정 데이터를 가진 노드를 삭제하고 트리를 재구성합니다.

        args :
            node : 현재 노드
            data : 삭제할 데이터 값

        return :
            수정된 서브트리의 루트 노드
        '''
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor = node.right
            while successor.left:
                successor = successor.left
            
            node.data = successor.data

            node.right = self._delete_node(node.right, successor.data)
            
        return node            

    def find_min(self):
        '''
        summary :
            트리에서 가장 작은 값을 찾습니다.

        args :
            인자값이 없습니다.

        return :
            트리에서 가장 작은 값
        '''
        current = self.root
        
        while current and current.left:
            current = current.left
        
        return current.data

    def find_max(self):
        '''
        summary :
            트리에서 가장 큰 값을 찾습니다.

        args :
            인자값이 없습니다.

        return :
            트리에서 가장 큰 값
        '''
        current = self.root

        while current and current.right:
            current = current.right
        
        return current.data

    def preorder(self, node):
        '''
        summary :
            전위 순회 방식으로 트리를 탐색하며 노드의 데이터를 출력합니다.

        args :
            node : 순회를 시작할 노드
        '''
        if node is not None:
            print(node.data, "", end="")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        '''
        summary :
            중위 순회 방식으로 트리를 탐색하며 노드의 데이터를 출력합니다.

        args :
            node : 순회를 시작할 노드
        '''
        if node is not None:
            self.inorder(node.left)
            print(node.data, "", end="")
            self.inorder(node.right)

    def postorder(self, node):
        '''
        summary :
            후위 순회 방식으로 트리를 탐색하며 노드의 데이터를 출력합니다.

        args :
            node : 순회를 시작할 노드
        '''
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, "", end="")


# 사용 예시
if __name__ == "__main__":
    bst = BinarySearchTree()

    # 노드 삽입
    bst.insert(50)
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # 트리 순회
    print("Preorder:")
    bst.preorder(bst.root)
    print("\nInorder:")
    bst.inorder(bst.root)
    print("\nPostorder:")
    bst.postorder(bst.root)
    print("\n")

    # 최소값, 최대값
    print(f"최소값 출력 : {bst.find_min()}")
    print(f"최대값 출력 : {bst.find_max()}")

    # 값 삭제
    bst.delete(50)
    print("\nPreorder traversal after delete root node:")
    bst.preorder(bst.root)




