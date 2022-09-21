from Auth import Auth

import os
os.chdir(f"{os.path.dirname(os.path.abspath(__file__))}/..")

if __name__ == '__main__':
    auth = Auth()
    auth.log_in()
