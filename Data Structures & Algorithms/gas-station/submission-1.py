class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        gas = [1,2,3,4], cost = [2,2,4,1]
        [(1), (0), (1), (0)]
        [-1, 0, -1, 3]
        """
        precomp = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(precomp) < 0:
            return -1
        
        start_node = 0
        current_gas = 0
        for i in range(len(precomp)):
            current_gas += precomp[i]
            if current_gas < 0:
                current_gas = 0
                start_node = i + 1
        return start_node