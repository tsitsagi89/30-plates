import plates

def main():
    test_plates()

def test_plates():
    assert plates.is_valid('CS50') == True
    assert plates.is_valid('AAAA11') == True
    assert plates.is_valid('BV26VB') == False



if __name__ == "__main__":
    main()