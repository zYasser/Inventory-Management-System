class Transaction:
    def __init__(
        self,
        transaction_id,
        product_id,
        transaction_type,
        transaction_date,
        quantity,
        total_amount,
        customer,
    ):
        self.TransactionID = transaction_id
        self.customer = customer
        self.ProductID = product_id
        self.TransactionType = transaction_type
        self.TransactionDate = transaction_date
        self.Quantity = quantity
        self.TotalAmount = total_amount
