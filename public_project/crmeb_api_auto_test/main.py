import pytest
import os
pytest.main(['-v','-s'])
os.system("allure generate -c -o ./report/html ./report/temps")
