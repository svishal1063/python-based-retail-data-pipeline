import pandas as pd
import uuid

def transform_data(df):

    ## Removing the NULL rows
	df = df.dropna()


    # Rename col_names to match DB schema
	df = df.rename(columns={
		"total_bill":"bill_amount",
		"tip":"tip_amount",
		"sex":"customer_gender",
		"smoker":"smoker_status",
		"size":"party_size"
	})

	# Generate unique order id
	df["order_id"] = [uuid.uuid4() for x in range(len(df))]

	# Create new revenue column
	df["revenue"] = df["bill_amount"] + df["tip_amount"]

	# Create new order_date column
	df["order_date"] = pd.Timestamp.now()

	print("Transformation successful")

	return df 
