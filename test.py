import mlflow
print("printing tracking URI scheme below")
print(mlflow.get_tracking_uri())
print()
mlflow.set_tracking_uri("https://127.0.0.1:5000")
print("printing new tracking URI scheme below")
print(mlflow.get_tracking_uri())
print()