from tester import Tester
from settings import Setting, defaults
from trade_strategy import Strategy

s1 = Strategy(
	profit_rate = 0.07,
	loss_rate = -0.0388,
	profit_probability = 0.4,
	Nth = 50
	)

s2 = Strategy(
	profit_rate = 0.07,
	loss_rate = -0.0388,
	profit_probability = 0.4,
	Nth = 5,
	)

s3 = Strategy(
	profit_rate = 0.3,
	loss_rate = -0.0687,
	profit_probability = 0.2,
	Nth = 1,
	)

s4 = Strategy(
	profit_rate = 0.3,
	loss_rate = -0.0687,
	profit_probability = 0.2,
	Nth = 5,
	)


s5 = Strategy(
	profit_rate = 0.15,
	loss_rate = -0.0571,
	profit_probability = 0.3,
	Nth = 10,
	)

t = Tester(
	s1.trade_Nth, s2.trade_Nth, s3.trade_Nth, s4.trade_Nth, s5.trade_Nth,
	)

if __name__ == "__main__":

	strategy_list = [s1, s2, s3, s4, s5]
	setting = Setting(strategy_list)
	msg = setting.print_settings()
	print(msg)

	output = t.test()

	print(output)

