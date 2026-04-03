import checks
from utils import format_result
from loader import load_orders, load_customers
from db import insert_checks, insert_pipeline_run

def run_pipeline():

    orders = load_orders('DataSets/Raw/orders_dataset.csv')
    customers = load_customers('DataSets/Raw/customers_dataset.csv')

    results = []

    results.append(format_result('orders', 'missing_orders', checks.check_missing_orders(orders)))
    results.append(format_result('orders', 'duplicate_orders', checks.check_duplicate_orders(orders)))
    results.append(format_result('orders', 'invalid_status', checks.invalid_status(orders)))
    results.append(format_result('orders', 'check_future_orders', checks.check_future_orders(orders)))
    results.append(format_result('orders', 'invalid_timestamp', checks.check_invalid_timestamp(orders)))
    results.append(format_result('orders', 'late_deliveries', checks.late_deliveries(orders)))
    

    results.append(format_result('customers', 'missing_customers', checks.check_missing_customers(customers)))
    results.append(format_result('customers', 'duplicate_customers', checks.check_duplicate_customers(customers)))
    results.append(format_result('customers', 'repeat_customers', checks.repeat_customers(customers)))
    results.append(format_result('customers', 'invalid_zip_code', checks.invalid_zip_code(customers)))


    results.append(format_result('cross', 'invalid_customer_ref', checks.invalid_customer_ref(orders, customers)))

    return results, orders

if __name__ == "__main__":
    # Run pipeline
    results, orders = run_pipeline()

    # --- INSERT INTO DATA QUALITY TABLE ---
    insert_checks(results)

    # --- PIPELINE SUMMARY ---
    # Count total errors (only numeric results)
    total_errors = sum(
        int(r['check_result']) if str(r['check_result']).isdigit() else 0
        for r in results
    )

    # Insert pipeline run
    insert_pipeline_run(
        status="success",
        records=len(orders),
        errors=total_errors
    )

    print("Pipeline run completed successfully!")