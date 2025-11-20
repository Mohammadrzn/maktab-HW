# Question 1

# import datetime
# import pprint
# import json
#
# print("Welcome to simple notepad")
# def show_main_menu() -> str:
#     print("\n1. Add new note\n2. See all notes\n3. Search in notes\n4. Delete a note\n5. Exit")
#     choice = input("Choice an option: ")
#     return choice
#
# while True:
#     user_choice = show_main_menu()
#     match user_choice:
#         case "1":
#             note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             note_title = input("Enter note title: ")
#             note_content = input("Enter note content: ")
#             with open("notes.jsonl", "a+", encoding="utf-8") as note_file:
#                 json.dump({"title": note_title, "content": note_content, "date": note_date}, note_file)
#                 note_file.write("\n")
#                 print("Note added")
#         case "2":
#             with open("notes.jsonl", "r", encoding="utf-8") as note_file:
#                 pprint.pprint([json.loads(line) for line in note_file], sort_dicts=False)
#         case "3":
#             note_title = input("Enter note title you want to search: ")
#             results = []
#             with open("notes.jsonl", "r", encoding="utf-8") as note_file:
#                 for line in note_file:
#                     note = json.loads(line)
#                     results.append(note) if note_title in note["title"] else ...
#
#             print(json.dumps(results, indent=2)) if len(results) else print("No match found")
#         case "4":
#             note_title = input("Enter note title you want to delete: ")
#             found = False
#             with open("notes.jsonl", "r", encoding="utf-8") as note_file:
#                 notes = []
#                 for line in note_file:
#                     note = json.loads(line)
#                     if note["title"] != note_title:
#                         notes.append(note)
#                     else:
#                         found = True
#             if not found:
#                 print("No match found")
#             else:
#                 with open("notes.jsonl", "w", encoding="utf-8") as note_file:
#                     for note in notes:
#                         json.dump(note, note_file)
#                         note_file.write("\n")
#                 print(f'Note titled "{note_title}" has been deleted.')
#         case "5":
#             print("Leaving, Goodbye!")
#             break
#         case _:
#             print("Invalid choice. Try again.")


# Question 2

print("Welcome to simple shop manager")
def show_main_menu() -> str:
    print("\n1. Export sell report\n2. Add new sell report\n3. Exit")
    return input("Choice an option: ")

def read_sales_file(filename="sales.txt"):
    sales = []
    try:
        with open(filename, "r") as sales_file:
            for line in sales_file:
                try:
                    product, price, quantity = line.strip().split(",")
                    sales.append({
                        "product": product.strip(),
                        "price": float(price.strip()),
                        "quantity": int(quantity.strip())
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        open(filename, "w").close()
    return sales

def export_report():
    sales = read_sales_file()
    if not sales:
        print("No sales data available.")
        return

    total_sales_amount = 0.0
    total_transactions = len(sales)

    product_occurrences = {}
    product_quantities = {}
    product_revenues = {}

    for sale in sales:
        sale_total = sale["price"] * sale["quantity"]
        total_sales_amount += sale_total

        name = sale["product"]
        product_occurrences[name] = product_occurrences.get(name, 0) + 1
        product_quantities[name] = product_quantities.get(name, 0) + sale["quantity"]
        product_revenues[name] = product_revenues.get(name, 0) + sale_total

    max_occ = max(product_occurrences.values())
    most_frequent_products = [product for product, cnt in product_occurrences.items() if cnt == max_occ]

    average_purchase = total_sales_amount / total_transactions

    print("\n--- گزارش فروش روز ---")
    print(f"تعداد تراکنش‌ها: {total_transactions}")
    print(f"فروش کل: {total_sales_amount:.2f} دلار")
    if len(most_frequent_products) == 1:
        product = most_frequent_products[0]
        print(f"پرفروش‌ترین کالا: {product} ({max_occ} بار)")
    else:
        print("پرفروش‌ترین کالاها:")
        for product in most_frequent_products:
            print(f" - {product} (تکرار {max_occ} بار)")
    print(f"میانگین مبلغ خرید هر تراکنش: {average_purchase:.2f} دلار")

def add_new_sale(filename="sales.txt"):
    try:
        product = input("Enter product name: ").strip()
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        with open(filename, "a") as file:
            file.write(f"\n{product}, {price}, {quantity}\n")
        print("New sale added successfully!")
    except ValueError:
        print("Invalid input, sale not added.")

while True:
    user_choice = show_main_menu()
    match user_choice:
        case "1":
            export_report()
        case "2":
            add_new_sale()
        case "3":
            print("Leaving, Goodbye!")
            break
        case _:
            print("Invalid choice, please try again.")
