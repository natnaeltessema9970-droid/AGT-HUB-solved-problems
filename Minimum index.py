class Solution(object):
    def findRestaurant(self, list1, list2):
        
        res_map = {restaurant: i for i, restaurant in enumerate(list1)}
        
        min_sum = float('inf')
        result = []

        for j, restaurant in enumerate(list2):
            if restaurant in res_map:
                i = res_map[restaurant]
                current_sum = i + j
                
            
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [restaurant]
                elif current_sum == min_sum:
                    result.append(restaurant)
                    
        return result
    
        
