
# mtlib - discover, query and control Malleable Things devices


## Install:

```
pip3 install mtlib
```



## Testing

Setup
```
cd mtlib
python3 -m venv /tmp/mtlib.venv
source /tmp/mtlib.venv/bin/activate
pip3 install -e .[test]
```


Run All Tests
```
python3 run_tests.py 
```

Run Single Test with debug logs
```
python3 run_tests.py test.test_integration.AsyncTest.test_state -d
```


