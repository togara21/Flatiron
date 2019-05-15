class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        #these are defaults below
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
   
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price":price})
            self.total += price
        return self.total
        
    def mean_item_price(self):
        return (self.total)/(len(self.items)) 

    def median_item_price(self):
        prices = [item["price"] for item in self.items]
        length = len(prices)
        if (length % 2 ==0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        mid = int(length/2)
        return prices[mid]

    def apply_discount(self):
        if self.employee_discount:
            return self.total * ((100-self.employee_discount)/100)
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if len(self.items) > 1:
            del self.items[-1]
            self.total -= self.items[-1]["price"]
        else:
            return "There are no items in your cart!"
    
    #how the solution did it
    #def void_last_item(self):
        #if self.items:
            #removed_item = self.items.pop()
        #else:
            #return "There are no items in your cart!"
        #self.total -= removed_item['price']