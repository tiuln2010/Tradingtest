defaults = {

	"profit_rate" : 0.07, # 승리할 경우 얻는 수익
	"loss_rate" : -0.05, # 실패할 경우 얻는 손해
	"profit_probability" : 0.5, # 성공할 확률

	"Nth" : 1, # N분의 1로 나눠서 하는 전략

	"budget" : 100, # 플레이어가 시작할 때 갖고 있는 돈
	"number_of_trades" : 10000, # 플레이어가 실행할 거래의 횟수
	"number_of_tests" : 100 # 게임의 횟수

}


class Setting():
	def __init__(self, insts):
		self.insts = insts


	def _round_up(self, num):
		num = round(num, 2)
		return num

	def call_coefficients(self):

		coefficients = []

		def t(x): 
			res = self._round_up(x)
			return res

		for inst in self.insts:
			dic = {}
			dic['profit_rate'] = t(inst.profit_rate)
			dic['loss_rate'] = t(inst.loss_rate)
			dic['profit_probability'] = t(inst.profit_probability)
			dic['Nth'] = inst.Nth
			coefficients.append(dic)

		res = coefficients

		return res
	
	def bring_coefficients(self, key):
								
		res = []
		co = self.call_coefficients()

		def _sep(li):
			i = 1
			if li[i] < 1:
				res = (str(int(li[0]*100))+'%').rjust(10)
				while i < len(li):
					res = res + ((str(int(li[i]*100)))+'%').rjust(15)
					i += 1
			else:
				res = str(li[0]).rjust(10)
				while i < len(li):
					res = res + str(li[i]).rjust(15)
					i += 1

			return res
		
		i = 0
		while i < 5 :
			res.append(co[i][key])
			i +=1

		msg = _sep(res)

		return msg

	def print_settings(self):

		settingmsg = (
					'\n\n\n\n\n########################################    Settings    ########################################\n' 
					+
					('	Budget 		: {0}\n' +
					'	Number of trades: {1}\n' +
					'	Number of tests : {2}\n\n').format(defaults['budget'], defaults['number_of_trades'], defaults['number_of_tests'])
					 +
					'	Strategy_name	  :  Strategy1      Strategy2      Strategy3      Strategy4      Strategy5\n'
					 +
					'	Profit_rate 	  : {}\n'.format(self.bring_coefficients('profit_rate')) +
					'	Loss_rate 	  : {}\n'.format(self.bring_coefficients('loss_rate')) +
					'	Probability 	  : {}\n'.format(self.bring_coefficients('profit_probability')) +
					'	Distribution (m/n): {}\n'.format(self.bring_coefficients('Nth'))					
					)

		return settingmsg
