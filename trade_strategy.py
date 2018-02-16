from settings import defaults
import random

class Strategy():
	def __init__(self, **kwargs):
		trade_defaults = {
			"profit_rate" : defaults["profit_rate"],
			"loss_rate" : defaults["loss_rate"],
			"profit_probability" : defaults["profit_probability"],

			"budget" : defaults["budget"],
			"number_of_trades" : defaults["number_of_trades"],

			"Nth" : defaults["Nth"],
		}

		for (key, default) in trade_defaults.items():
			setattr(self, key, kwargs.get(key, default))
				
	def _trading(self, money):
		r = random.uniform(0,1)
		
		if r >= 1 - self.profit_probability :
			res = money*(1 + self.profit_rate)
		else:	
			res = money*(1 + self.loss_rate)
		
		return res

	def trade_Nth(self):
		ms = self.budget
		n = self.Nth
		m = 0
		
		a = 0

		while a < self.number_of_trades:
			x = 0
			while x < n:
				m = m + self._trading(ms/n)
				x += 1
			ms = m
			m = 0
			a += 1
			
		return ms

	def trade_twothird(self):
		m = self.budget
		a = 0
		while a < self.number_of_trades:
			m = self._trading(m/3) + self._trading(m/3) + m/3
			a += 1
		return m