def type_conversion():
    # implicit type conversion
    # automatically converts to int
    a = 7
    print("Automatic type converion")
    print(type(a))

    # automatically converts to float
    b = 10.0
    print(type(b))

    print("int and float addition and result is converted to float")
    # automatically converts to float
    c = a + b
    print(type(c))

    print("int and float multiplication and result is converted to float")
    # automatically converts to float
    d = a * b
    print(type(d))


    # explicit conversion
    # int to float conversion
    print("int type explicitly converted to float")
    a=float(a)
    print(type(a))

    # float to int conversion
    x = 5.6
    #print(type(x))
    print("float type explicitly converted to int")
    y=int(x)
    print(type(y))

    # float to string conversion
    print("flaot type conveteed to string type explicitly")
    a=str(a)
    print(type(a))

    # string to float conversion
    z_string="10.10"
    print("string type conveteed to float type explicitly")
    m_float=float(z_string)
    print(type(m_float))

if __name__ == "__main__":
    type_conversion()