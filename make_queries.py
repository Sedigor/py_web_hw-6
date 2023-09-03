queries = [
]

for i, query in enumerate(queries, start=1):
    filename = f"query_{i}.sql"
    with open(filename, "w") as f:
        f.write(query)

    print(f"Query {i} saved to {filename}")