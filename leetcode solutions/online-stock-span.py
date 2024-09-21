class StockSpanner:

    def __init__(self):
        self.stack =[]
        self.prices =[]
        self.i = 0




    def next(self, price: int) -> int:
        self.prices.append(price)
        ans =-1




        while self.stack and self.prices[self.stack[-1]]<= price:
            self.stack.pop()

        if self.stack:
            ans = self.i -self.stack[-1]
        else:
            ans = self.i +1



        self.stack.append(self.i)
        self.i+=1




        return ans

















# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
