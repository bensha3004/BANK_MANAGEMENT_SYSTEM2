class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.left = None
        self.right = None

class Bank:
    def __init__(self):
        self.root = None


    def insert(self, account_number, account_holder, balance):
        new_account = BankAccount(account_number, account_holder, balance)
        if not self.root:
            self.root = new_account
        else:
            current = self.root
            while True:
                if current.account_number < new_account.account_number:
                    if current.left is None:
                        current.left = new_account
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_account
                        break
                    else:
                        current = current.right

    def search(self, account_number):
        current = self.root
        while current:
            if current.account_number == account_number:
                return current
            elif current.account_number < account_number:
                current = current.right
            else:
                current = current.left
        return None

    def display_inorder(self, root):
        if root is None:
            return None
        self.display_inorder(root.left)
        print("Account Number:", root.account_number)
        print("Account Holder:", root.account_holder)
        print("Balance:", root.balance)
        self.display_inorder(root.right)

    def display_all_accounts(self):
        if self.root is None:
            print('No Accounts Found')
        else:
            print('Bank Accounts:')
            print("---------------")
            self.display_inorder(self.root)

bank = Bank()

bank.insert(1000, "Fathima Bensha", 5000)
bank.insert(1001, "Bajisha Zainab", 20000)
bank.insert(1002, 'Benzy Mariyam', 15000)
bank.insert(1003, 'Zainul Ameen', 14000)

bank.display_all_accounts()
account_number = 1002
account = bank.search(account_number)
if account:
    print('Account found:')
    print("Account_number:", account.account_number)
    print("Account_holder:", account.account_holder)
    print("Balance:", account.balance)




