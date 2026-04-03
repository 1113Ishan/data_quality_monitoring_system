from datetime import datetime
import json
import numpy as np

def format_result(table_name, check_type, check_result):
    """
    Formats a data quality check result into a consistent dictionary for SQL insertion.
    
    - Converts dicts, lists, or numpy types to JSON strings
    - Adds timestamp
    """

    # Helper to convert numpy types to Python native
    def convert(obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [convert(v) for v in obj]
        return obj

    # Convert everything recursively
    converted_result = convert(check_result)

    # Serialize to JSON string
    check_result_json = json.dumps(converted_result)

    return {
        "table_name": table_name,
        "check_type": check_type,
        "check_result": check_result_json,
        "check_time": datetime.now()
    }