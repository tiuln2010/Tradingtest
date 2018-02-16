import numpy
import sys
import time
# import matplotlib.pyplot as plt

from settings import defaults
from trade_strategy import Strategy

'''
총 4개의 전략을 갖고, 4명이 같은 예산을 갖고 플레이 한다.
각 회차마다, 각 플레이어는 돈을 number_of_trades만큼 굴린다.
굴리고 난 뒤 수익이 가장 높은 전략에 1점을 준다.

모든 게임을 한 결과는 기록해 평균, 분산, 표준편차를 구한다.
각 전략의 점수를 합산해 구한다.
'''

'''
############################     Settings     ############################


profit_rate = 1.10 # 승리할 경우 얻는 수익
loss_rate = 0.95 # 실패할 경우 얻는 손해
profit_probability = 0.4 # 성공할 확률

Nth = 4 # N분의 1로 나눠서 하는 전략

budget = 100 # 플레이어가 시작할 때 갖고 있는 돈
number_of_trades = 100 # 플레이어가 실행할 거래의 횟수
number_of_tests = 1000 # 게임의 횟수


############################     Settings     ############################
'''

class Tester():

	

	def __init__(self, fuc1, fuc2, fuc3, fuc4, fuc5, **kwargs) :
		trade_defaults = {
			"budget" : defaults["budget"],
			"number_of_trades" : defaults["number_of_trades"],
			"number_of_tests" : defaults["number_of_tests"],
		}

		for (key, default) in trade_defaults.items():
			setattr(self, key, kwargs.get(key, default))
		
		self.fuc1 = fuc1
		self.fuc2 = fuc2
		self.fuc3 = fuc3
		self.fuc4 = fuc4
		self.fuc5 = fuc5

	def _sep(self, li):
		i = 1
		res = li[0].rjust(10)

		while i < len(li):
			res = res + str(li[i]).rjust(15)
			i += 1
		
		return res

	def _round_up(self, num):
		num = round(num, 2)
		return num

	def _print_results(self, test_res):
		
		msg = (('	{0} 	: {1}\n').format(test_res[0][0], self._sep(test_res[1])) +
			('	{0} 	: {1}\n').format(test_res[0][1], self._sep(test_res[2])) +
			('	{0} 	: {1}\n').format(test_res[0][2], self._sep(test_res[3])) +
			('	{0} 	: {1}\n').format(test_res[0][3], self._sep(test_res[4])) +
			('	{0} 	: {1}\n').format(test_res[0][4], self._sep(test_res[5])))
		
		
		print ('\r########################################     Results     ########################################\n' +
		'	Strategy_name	:    Win rate        Median           Mean            Var            Std\n' +
		'-------------------------------------------------------------------------------------------------')
		return msg

	def test(self):

		[output_list1, output_list2, output_list3, output_list4, output_list5] = [[],[],[],[],[]]
		s1win = s2win = s3win = s4win = s5win = 0


		def _win_rate(win):
			rate = '{}%'.format(self._round_up(100*win/self.number_of_tests))
			return rate
		
		def _loading(i, total):
			if 1000*(i/total) == int(1000*(i/total)):
				percentage = round(100*(i/total), 2)
				print('	{}% is done'.format(percentage), end='\r')
	
		i = 0
		s1win = s2win = s3win = s4win = s5win = 0
		while i < self.number_of_tests:
			outputs = [output1, output2, output3, output4, output5] = [self.fuc1(), self.fuc2(), self.fuc3(), self.fuc4(), self.fuc5()]
			
			maxnum = max(outputs)
			if maxnum == output1:
				s1win += 1
			if maxnum == output2:
				s2win += 1
			if maxnum == output3:
				s3win += 1
			if maxnum == output4:
				s4win += 1
			if maxnum == output5:
				s5win += 1
							
			output_list1.append(output1)
			output_list2.append(output2)
			output_list3.append(output3)
			output_list4.append(output4)
			output_list5.append(output5)
			
			_loading(i, self.number_of_tests)
			i += 1

		output_lists = [output_list1, output_list2, output_list3, output_list4, output_list5]
		stat_res = []

		for li in output_lists:
			stats = [numpy.median(li), numpy.mean(li), numpy.var(li), numpy.std(li)]
			stat_res.append(stats)

		win_rate = [_win_rate(s1win), _win_rate(s2win), _win_rate(s3win), _win_rate(s4win), _win_rate(s5win)]
		
		fuc_name = [self.fuc1.__name__, self.fuc2.__name__, self.fuc3.__name__, self.fuc4.__name__, self.fuc5.__name__]
		res_s1 = [win_rate[0], self._round_up(stat_res[0][0]), self._round_up(stat_res[0][1]), self._round_up(stat_res[0][2]), self._round_up(stat_res[0][3])]
		res_s2 = [win_rate[1], self._round_up(stat_res[1][0]), self._round_up(stat_res[1][1]), self._round_up(stat_res[1][2]), self._round_up(stat_res[1][3])]
		res_s3 = [win_rate[2], self._round_up(stat_res[2][0]), self._round_up(stat_res[2][1]), self._round_up(stat_res[2][2]), self._round_up(stat_res[2][3])]
		res_s4 = [win_rate[3], self._round_up(stat_res[3][0]), self._round_up(stat_res[3][1]), self._round_up(stat_res[3][2]), self._round_up(stat_res[3][3])]
		res_s5 = [win_rate[4], self._round_up(stat_res[4][0]), self._round_up(stat_res[4][1]), self._round_up(stat_res[4][2]), self._round_up(stat_res[4][3])]
		
		res = [fuc_name, res_s1, res_s2, res_s3, res_s4, res_s5]
		msg = self._print_results(res)
		
		return msg

		 

	# plt.hist(k, bins=50)
	# return plt.show()