from mesa import Agent, Model
from mesa.time import RandomActivation

class MoneyAgent(Agent):
	"""An Agent with fixed inital wealth."""

	def __init__(self, unique_id, model):
		super().__init__(unique_id, model)
		self.wealth = 1

	def step(self):
		# The agent's step will go here.
		if self.wealth == 0:
			return
		other_agent = self.random.choice(self.model.schedule.agents)
		other_agent.wealth += 1
		self.wealth -= 1
		

class MoneyModel(Model):
	"""A model with some number of agents."""

	def __init__(self,N):
		self.num_agents = N
		self.schedule = RandomActivation(self)
		#Create Agents
		for i in range(self.num_agents):
			a = MoneyAgent(i, self)
			self.schedule.add(a)

	def step(self):
		"""Advance the model by one step."""
		self.schedule.step()
        

"""Scripting"""
       
model = MoneyModel(10)
for i in range(10):
    model.step()

import matplotlib.pyplot as plt
agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth)

all_wealth = []
for j in range(100):
    # Run the model
    model = MoneyModel(10)
    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)

plt.hist(all_wealth, bins=range(max(all_wealth)+1))