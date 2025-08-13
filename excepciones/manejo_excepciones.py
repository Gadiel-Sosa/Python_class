# 10/0 error no se puede divir entre 0
try:
    10/0
except Exception as e:
    print(f'Ocurrió un error: {e}')