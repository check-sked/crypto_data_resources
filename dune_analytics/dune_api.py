import requests
import time
import csv


# Function to delay execution
def delay(seconds):
    time.sleep(seconds)


# Function to fetch query data and loop until completed
def fetch_query_data(queryID):
    try:
        # Add the API key to the headers
        headers = {"x-dune-api-key": "[INSERT_YOUR_API_KEY]"}

        # Execute the query and get the execution_id
        executionResponse = requests.post(
            f"https://api.dune.com/api/v1/query/{queryID}/execute", headers=headers
        )

        # Check if the execution response is not successful and raise an error
        if not executionResponse.ok:
            raise Exception(f"Error executing query: {executionResponse.status_code}")

        executionData = executionResponse.json()
        executionID = executionData["execution_id"]

        isCompleted = False
        attempts = 0
        timeout = time.time() + 5 * 60  # 5 minutes timeout

        # Loop until the query is completed or the maximum number of attempts is reached
        while not isCompleted and time.time() < timeout:
            # Check the query execution status using the execution_id
            statusResponse = requests.get(
                f"https://api.dune.com/api/v1/execution/{executionID}/status",
                headers=headers,
            )

            # Check if the status response is not successful and raise an error
            if not statusResponse.ok:
                raise Exception(f"Error fetching status: {statusResponse.status_code}")

            statusData = statusResponse.json()

            print(statusData)

            # Check if the query state is completed
            if statusData["state"] == "QUERY_STATE_COMPLETED":
                isCompleted = True
            else:
                attempts += 1
                delay(5)  # Wait for 5 seconds before trying again

        # Raise an error if the query is not completed within the timeout
        if not isCompleted:
            raise Exception("Unable to fetch query results after multiple attempts")

        # Fetch the query results in CSV format
        resultsResponse = requests.get(
            f"https://api.dune.com/api/v1/execution/{executionID}/results/csv",
            headers=headers,
        )

        # Check if the results response is not successful and raise an error
        if not resultsResponse.ok:
            raise Exception(f"Error fetching results: {resultsResponse.status_code}")

        resultsData = resultsResponse.text

        # Save the CSV data to a file
        fileName = f"results_{queryID}.csv"
        with open(fileName, "w", newline="") as file:
            file.write(resultsData)

        print(f"CSV file has been saved as {fileName}")
    except Exception as error:
        # Log the error message if an error occurs
        print("Error:", str(error))


if __name__ == "__main__":
    # Get the query ID from user input
    queryID = input("Enter the Query ID: ")
    print("Retrieving data for query " + queryID + "...")

    # Call the function to fetch query data
    fetch_query_data(queryID)
