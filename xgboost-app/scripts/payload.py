def get_first():
    file_name = "abalone.single.test"
    with open(file_name, "r") as f:
        prediction_payload = f.read().strip()
        
    return prediction_payload
