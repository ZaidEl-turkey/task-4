import tkinter as tk

class SupermarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Market")
        self.fruit_prices = {
            "Mango": 7,
            " Apple ": 3,
            "Banana": 6,
            " Guava ": 5
        }
        self.fruit_counts = {fruit: 0 for fruit in self.fruit_prices}
        self.total_cost = 0

        self.create_widgets()

    def create_widgets(self):
        fruit_frame = tk.Frame(self.root)
        fruit_frame.pack()
        for i, fruit in enumerate(self.fruit_prices):
            button = tk.Button(fruit_frame, text=fruit, command=lambda fruit=fruit: self.increment_count(fruit))
            button.grid(row=i, column=0)

        self.total_cost_label = tk.Label(self.root, text="Total Cost: 0 EGP")
        self.total_cost_label.pack()

        checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout)
        checkout_button.pack()

    def increment_count(self, fruit):
        self.fruit_counts[fruit] += 1
        self.total_cost = self.fruit_prices[fruit]
        self.total_cost_label.config(text=f"Total Cost: {self.total_cost} EGP")

    def checkout(self):
        self.total_cost = 0
        self.fruit_counts = {fruit: 0 for fruit in self.fruit_prices}
        self.total_cost_label.config(text="Total Cost: 0 EGP")

root = tk.Tk()
app = SupermarketApp(root)
root.mainloop()