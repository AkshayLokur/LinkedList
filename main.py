from linkedlist import LinkedList

ll = LinkedList()


def create_list():
    ll.append(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # print("------------- Linked List:")
    # ll.print()
    #
    # ll.prepend(0)
    # ll.prepend(-1)
    # print("LL After prepend:")
    # ll.print()


def test_pop():
    print("Popping items from LL:")
    for i in range(ll.length):
        popped_item = ll.pop()
        print(f"Popped item: {popped_item}")


def test_pop_first():
    for i in range(ll.length):
        popped_item = ll.pop_first()
        print(f"Popped item: {popped_item}")


if __name__ == "__main__":
    create_list()
    # test_pop()
    # create_list()
    # test_pop_first()
    # print(f"Item at index 3 is: {ll.get(3)}")
    # if ll.set(3, "BBBB"):
    #     ll.print()
    print("~~~~ Reversed LL: ~~~~~")
    ll.reverse()
    ll.print()
