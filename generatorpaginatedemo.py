def get_pages(data, page_size):
    for i in range(0, len(data),page_size):
        yield data[i:i+page_size]

items = list(range(1,11)) # [1,2,3,..10]

for page in get_pages(items,3):
    print(page)