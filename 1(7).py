from datetime import datetime
data = [("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143))]
def print_table(data):
    header = f"| {'Post code':^10} | {'Cost, thousands USD':^20} | {'Country':^10} | {'City':^10} | {'Street':^20} | {'Build.':^7} | {'App.':^5} | {'Date':^20} |"
    separator = '-' * len(header)
    print(separator)
    print(header)
    print(separator)
    for line in data[1:]:
        (post_code, cost, country, city, street, build, app, Date) = line
        row = (f"| {post_code:<10} | "
            f"{cost:>20} | "
            f"{country:<10} | "
            f"{city:<10} | "
            f"{street:<20} | "
            f"{build:>7} | "
            f"{app:>5} | "
            f"{Date.strftime('%Y-%m-%d %H:%M:%S'):<20} |")
        print(row)
    print(separator)
print_table(data)
