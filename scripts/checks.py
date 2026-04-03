import datetime

# Orders dataset checks

def check_missing_orders(df):
    return df[['order_id', 'customer_id', 'order_purchase_timestamp']].isnull().sum().to_dict()

def check_duplicate_orders(df):
    return df.duplicated(subset=['order_id']).sum()

def invalid_status(df):
    valid_status = ['delivered', 'canceled', 'shipped', 'processing', 'invoiced']
    return(~df['order_status'].isin(valid_status)).sum()

def check_future_orders(df):
    now = datetime.datetime.now()
    return(df['order_purchase_timestamp']>now).sum()

def check_invalid_timestamp(df):
    errors = {}

    errors['approved_before_purchase']=(
        df['order_approved_at'] < df['order_purchase_timestamp']
    ).sum();

    errors['delivered_before_shipped']=(
        df['order_delivered_customer_date'] < df['order_delivered_customer_date']
    ).sum()

    return errors

def late_deliveries(df):
    return(
        df['order_delivered_customer_date'] > df['order_estimated_delivery_date']
    ).sum()


# Customers dataset checks

def check_missing_customers(df):
    return(df[['customer_id', 'customer_unique_id']]).isnull().sum().to_dict()

def check_duplicate_customers(df):
    return(
        df.duplicated(subset = ['customer_id'])
    ).sum()

def repeat_customers(df):
    return df['customer_unique_id'].value_counts().gt(1).sum()

def invalid_zip_code(df):
    return(
        df['customer_zip_code_prefix'].astype(str).str.len().ne(5).sum()
    )


# Cross table data relation checks

def invalid_customer_ref(orders, customers):
    return(
        ~orders['customer_id'].isin(customers['customer_id'])
    ).sum()

