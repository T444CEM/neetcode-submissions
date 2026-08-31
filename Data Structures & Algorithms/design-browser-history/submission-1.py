class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory:


    def __init__(self, homepage: str):
        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.hp = ListNode(homepage)

        self.head.next = self.hp
        self.hp.prev = self.head

        self.hp.next = self.tail
        self.tail.prev = self.hp

        self.currpage = ListNode(0)
        self.currpage.next = self.hp

    def visit(self, url: str) -> None:
            new_page = ListNode(url)

            new_page.next = self.tail
            self.tail.prev = new_page

            self.currpage.next.next = new_page
            new_page.prev = self.currpage.next 

            self.currpage.next = new_page 

    def back(self, steps: int) -> str:
            curr = self.currpage.next
            for i in range(steps):
                if curr.prev != self.head:
                    curr = curr.prev
                    self.currpage.next = curr
                else:
                    self.currpage.next = curr
                    return curr.val

            return curr.val

    def forward(self, steps: int) -> str:
        curr = self.currpage.next
        for i in range(steps):
            if curr.next != self.tail:
                curr = curr.next
                self.currpage.next = curr
            else:
                self.currpage.next = curr
                return curr.val
        
        return curr.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)