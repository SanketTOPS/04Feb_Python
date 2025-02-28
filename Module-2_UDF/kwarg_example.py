def fun(**kwarg):
    for i, j in kwarg.items():
        print(f"Key:{i} and Value={j}")


fun(id=1, name="Sanket", city="Rajkot")
