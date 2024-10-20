def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
inner_function()  # Здесь функция inner_function() определена внутри test_function().
# Для вызова inner_function() нужно сперва вызвать test_function().
# После этого test_function() начнет выполняться, что приведет к вызову inner_function().
# Внутренняя функция не будет выполняться, если не вызвать внешнюю.
# NameError: name 'inner_function' is not defined.
