import json
from collections import Counter
import matplotlib.pyplot as plt

def GetMethodData(data):
    methods = []
    for sublist in data:
        for entry in sublist:
            if entry["allowed_methods"]:
                methods.extend(method.strip().upper() for method in entry["allowed_methods"].split(","))
    
    method_counts = Counter(methods)
    sorted_methods = dict(sorted(method_counts.items(), key=lambda item: item[1], reverse=True))

    # Plotting
    plt.figure(figsize=(14, 8))
    plt.bar(sorted_methods.keys(), sorted_methods.values(), color='skyblue')
    plt.xlabel("Allowed Methods")
    plt.ylabel("Frequency")
    plt.title("Frequency of Allowed Methods")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def GetHeaderData(data):
    headers = []
    for sublist in data:
        for entry in sublist:
            if entry["allowed_headers"]:
                headers.extend(header.strip().upper() for header in entry["allowed_headers"].split(","))
    
    header_counts = Counter(headers)
    top_headers = dict(header_counts.most_common(10))

    plt.figure(figsize=(14, 8))
    plt.bar(top_headers.keys(), top_headers.values(), color='skyblue')
    plt.xlabel("Allowed Headers")
    plt.ylabel("Frequency")
    plt.title("Frequency of Allowed Headers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    with open('Cors_Data.json', 'r') as f:
        data = json.load(f)
    GetMethodData(data)
    GetHeaderData(data)
