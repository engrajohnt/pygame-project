import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Store Management")

        # Product Frame
        prod_fram = ttk.LabelFrame(root, text="Product Management")
        prod_fram.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        # Product List Frame
        prod_li_frame = ttk.LabelFrame(root, text="Product List")
        prod_li_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

        # Sales Frame
        sales_frame = ttk.LabelFrame(root, text="Sales")
        sales_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="nswe")

        # Product Management Widgets
        self.product_name = tk.StringVar()
        self.product_price = tk.DoubleVar()

        ttk.Label(prod_fram, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(prod_fram, textvariable=self.product_name).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(prod_fram, text="Product Price:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(prod_fram, textvariable=self.product_price).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(prod_fram, text="Add Product", command=self.add_product).grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        # Product List Widgets
        self.prod_li = ttk.Treeview(prod_li_frame, columns=("Product Name", "Product Price"), show="headings")
        self.prod_li.heading("Product Name", text="Product Name")
        self.prod_li.heading("Product Price", text="Product Price")
        self.prod_li.grid(row=0, column=0, padx=5, pady=5)

        # Sales Widgets
        self.sale_product = tk.StringVar()
        self.sale_quantity = tk.IntVar()

        ttk.Label(sales_frame, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(sales_frame, textvariable=self.sale_product).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(sales_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(sales_frame, textvariable=self.sale_quantity).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(sales_frame, text="Make Sale", command=self.make_sale).grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        self.sales_list = ttk.Treeview(sales_frame, columns=("Product Name", "Quantity"), show="headings")
        self.sales_list.heading("Product Name", text="Product Name")
        self.sales_list.heading("Quantity", text="Quantity")
        self.sales_list.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

        self.product_data = []  # List of products in the store
        self.sales_data = []  # List of sales made

    def add_product(self):
        product_name = self.product_name.get()
        product_price = self.product_price.get()

        if not product_name or product_price <= 0:
            messagebox.showerror("Error", "Please enter valid product information.")
            return

        # Add product to the list
        self.product_data.append({"name": product_name, "price": product_price})

        # Update the product list
        self.prod_li.insert("", "end", values=(product_name, product_price))

        # Clear input fields
        self.product_name.set("")
        self.product_price.set(0)

    def make_sale(self):
        product_name = self.sale_product.get()
        quantity = self.sale_quantity.get()

        if not product_name or quantity <= 0:
            messagebox.showerror("Error", "Please enter valid sale information.")
            return

        # Check if the product exists
        product_exists = any(
            product for product in self.product_data if product["name"] == product_name
        )

        if not product_exists:
            messagebox.showerror("Error", "Product not found in the store.")
            return

        # Add sale to the list
        self.sales_data.append({"product_name": product_name, "quantity": quantity})

        # Update the sales list
        self.sales_list.insert("", "end", values=(product_name, quantity))

        # Clear input fields
        self.sale_product.set("")
        self.sale_quantity.set(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()
