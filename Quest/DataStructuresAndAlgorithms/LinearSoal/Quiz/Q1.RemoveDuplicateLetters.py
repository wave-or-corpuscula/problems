# https://leetcode.com/quest/data-structures-and-algorithms-quest/quiz/remove-duplicate-letters/?envType=problem-list-v2&envId=dsa-linear-shoal-assignment-ii

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Подсчитываем количество каждого символа
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        # Множество для отслеживания символов, уже добавленных в результат
        in_stack = set()
        stack = []
        
        for char in s:
            # Уменьшаем счетчик текущего символа
            counter[char] -= 1
            
            # Если символ уже есть в стеке - пропускаем
            if char in in_stack:
                continue
            
            # Жадное удаление: пока стек не пуст И текущий символ меньше вершины стека
            # И вершина стека еще встретится в будущем (counter[last_char] > 0)
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            
            # Добавляем текущий символ
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)