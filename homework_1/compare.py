if __name__ == "__main__":
    with open("/Users/sinelnikovweb/itmo/python/homework-1/out1.txt", "r") as f1:
        with open("/Users/sinelnikovweb/itmo/python/homework-1/out2.txt", "r") as f2:
            ls1 = f1.readlines()
            ls2 = f2.readlines()
            for line_index in range(len(ls1)):
                l1 = ls1[line_index]
                l2 = ls2[line_index]
                if l1 != l2:
                    print(l1)
                    print(l2)
                    print("----------------------------")
                    print("len", len(l1), len(l2))
                    for i in range(min(len(l1), len(l2))):
                        print(ord(l1[i]), ord(l2[i]))
