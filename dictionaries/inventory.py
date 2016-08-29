bag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for m, n in inventory.items():
        print(str(n)+' '+m)
        item_total+=n
    print("Total number of items: "+str(item_total))
displayInventory(bag)
