dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for m, n in inventory.items():
        print(str(n)+' '+m)
        item_total+=n
    print("Total number of items: "+str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 1)
        inventory[i] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
