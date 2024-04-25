class BlockWorldAgent: 
    def __init__(self, initial_state, goal_state): 
        self.initial_state = initial_state 
        self.goal_state = goal_state 
    def plan(self): 
        plan = self.generate_plan() 
        return plan 
 
    def generate_plan(self): 
        plan = [] 
        for block, goal_location in self.goal_state.items(): 
            current_location = self.initial_state[block] 
            if current_location != goal_location: 
                if goal_location == "on table": 
                    plan.append(f"Move block {block} to the table") 
                else: 
                    plan.append(f"Stack block {block} on top of block {goal_location}") 
        return plan 

initial_state = {"A": "on table", "B": "on table", "C": "on table", "D": "on E", "E": "on table"} 
goal_state = {"A": "on table", "B": "on C", "C": "on D", "D": "on table", "E": "on table"} 
agent = BlockWorldAgent(initial_state, goal_state) 
print("Initial State:") 
for block, location in initial_state.items(): 
 print(f"Block {block} is {location}") 
print("\nGoal State:") 
for block, location in goal_state.items(): 
 print(f"Block {block} should be {location}") 
plan = agent.plan() 
print("\nPlan to Achieve Goal State:") 
for action in plan: 
 print(action)