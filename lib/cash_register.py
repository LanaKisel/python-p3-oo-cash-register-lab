#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total= 0):
        self._discount = discount
        self._total = total
        self._items = []

    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, total):
        self._total = total
    @property
    def items(self):
        return self._items
    @property
    def discount(self):
        return self._discount                  

    def add_item(self, title, price, quantity=1):       
        self._total = self._total + price * quantity 
        for x in range(quantity):
            self._items.append(title)
        self.transaction = {
            'title': title,
            'price':price,
            'quantity': quantity
        }
 
             
    def apply_discount(self):
        if self._discount >0:
            self._total = ((100 - self._discount) / 100) * self._total
            print(f"After the discount, the total comes to ${int(self._total)}.")
        else:
            print("There is no discount to apply.")    
        return self._total

    def void_last_transaction(self):
        for i in range(self.transaction['quantity']):
            self.total -= self.transaction['price']
            self.items.pop()




