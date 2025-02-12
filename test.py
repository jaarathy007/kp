def test_calculator():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert divide(8, 2) == 4
    assert divide(5, 0) == "Cannot divide by zero"
    print("All tests passed!")
 
if __name__ == "__main__":
    # Run tests first
    test_calculator()
 
    # Then run the calculator
    calculator()
