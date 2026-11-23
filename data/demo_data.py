import pandas as pd


def get_demo_suppliers():
    return pd.DataFrame([
        {
            "supplier_id": "SUP-001",
            "supplier_name": "Global Raw Materials",
            "country": "China",
            "reliability": 72,
            "lead_time_days": 18,
            "status": "At Risk",
            "category": "Raw Materials",
        },
        {
            "supplier_id": "SUP-002",
            "supplier_name": "Eastern Components",
            "country": "Malaysia",
            "reliability": 91,
            "lead_time_days": 10,
            "status": "Active",
            "category": "Electronic Components",
        },
        {
            "supplier_id": "SUP-003",
            "supplier_name": "Prime Industrial",
            "country": "Germany",
            "reliability": 96,
            "lead_time_days": 7,
            "status": "Active",
            "category": "Industrial Parts",
        },
        {
            "supplier_id": "SUP-004",
            "supplier_name": "Northern Supplies",
            "country": "Turkey",
            "reliability": 88,
            "lead_time_days": 12,
            "status": "Active",
            "category": "Packaging Materials",
        },
    ])


def get_demo_shipments():
    return pd.DataFrame([
        {
            "shipment_id": "SHP-1001",
            "supplier_id": "SUP-001",
            "product": "Industrial Resin",
            "quantity": 500,
            "origin": "Shanghai",
            "destination": "Karachi",
            "expected_days": 18,
            "delay_days": 12,
            "status": "Delayed",
        },
        {
            "shipment_id": "SHP-1002",
            "supplier_id": "SUP-002",
            "product": "Electronic Controllers",
            "quantity": 300,
            "origin": "Kuala Lumpur",
            "destination": "Karachi",
            "expected_days": 10,
            "delay_days": 3,
            "status": "At Risk",
        },
        {
            "shipment_id": "SHP-1003",
            "supplier_id": "SUP-003",
            "product": "Industrial Motors",
            "quantity": 150,
            "origin": "Hamburg",
            "destination": "Karachi",
            "expected_days": 7,
            "delay_days": 0,
            "status": "Delivered",
        },
        {
            "shipment_id": "SHP-1004",
            "supplier_id": "SUP-004",
            "product": "Packaging Rolls",
            "quantity": 800,
            "origin": "Istanbul",
            "destination": "Karachi",
            "expected_days": 12,
            "delay_days": 5,
            "status": "At Risk",
        },
    ])


def get_demo_inventory():
    return pd.DataFrame([
        {
            "product_id": "PRD-001",
            "product_name": "Industrial Resin",
            "available_stock": 120,
            "daily_demand": 40,
            "reorder_level": 200,
            "safety_stock": 100,
            "unit": "Units",
        },
        {
            "product_id": "PRD-002",
            "product_name": "Electronic Controllers",
            "available_stock": 450,
            "daily_demand": 35,
            "reorder_level": 150,
            "safety_stock": 100,
            "unit": "Units",
        },
        {
            "product_id": "PRD-003",
            "product_name": "Industrial Motors",
            "available_stock": 80,
            "daily_demand": 8,
            "reorder_level": 50,
            "safety_stock": 30,
            "unit": "Units",
        },
        {
            "product_id": "PRD-004",
            "product_name": "Packaging Rolls",
            "available_stock": 160,
            "daily_demand": 25,
            "reorder_level": 180,
            "safety_stock": 80,
            "unit": "Units",
        },
    ])


def get_all_demo_data():
    """
    Return all demonstration datasets in one dictionary.
    """

    return {
        "suppliers": get_demo_suppliers(),
        "shipments": get_demo_shipments(),
        "inventory": get_demo_inventory(),
    }


def get_combined_demo_context():
    """
    Convert all demo datasets into a dictionary of records
    that can be passed to the multi-agent crew.
    """

    data = get_all_demo_data()

    return {
        name: dataframe.to_dict(orient="records")
        for name, dataframe in data.items()
    }
