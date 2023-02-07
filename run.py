import os
import time
import pytest
if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("/Users/kong/Desktop/software/allure-2.18.1/bin/allure generate ./temps -o ./reports --clean")
