# Tradingtest
Test your trading strategies depend on probability, profit rate, number of trades, especially distribution strategy etc 

At first you have to set 5 strategies in main.py

s1, s2 ... ,s5 are strategies, each trade strategy has it's own gambling setting(profit rate, loss rate), probability(chance of getting profit), Nth(this number is about how you will put your money, if you put Nth as 2 than that strategy will divide money into half and each money will be gambled at a round, after the round each gambles output will be summed. This operation will be repeated.)

After that, 5 strategies will compete each other. Tester will run as many times as you set. Default value is 100 and give you a number of each strategies win rate. (You can set default values in setting.py )

Output shows you each strategies win rate, median, mean, var, std.

With this tester you can test which strategy is more profitable than the others. 

Thanks.
