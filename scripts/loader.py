import pandas as pd

def load_orders(path):
    df = pd.read_csv(path)

    date_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors = "coerce")
    return df



def load_customers(path):
    df = pd.read_csv(path)
    return df

