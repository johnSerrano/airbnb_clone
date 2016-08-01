#This program is for testing things. you should create any tests you want, and
#add them to the 'tests' array in test_all.
#
#Tests will either return True or a message explaining what went wrong.

def test_imports():
    try:
        import app.models.base
        database = app.models.base.test_import()
    except Exception as e:
        return str(e)
    return True

def test_user():
    try:
        import app.models.user
        user = app.models.user.User()
        data = user.to_dict()
    except Exception as e:
        return str(e)
    return True

def test_state():
    try:
        import app.models.state
        state = app.models.state.State()
        data = state.to_dict()
    except Exception as e:
        return str(e)
    return True

def test_city():
    try:
        import app.models.city
        city = app.models.city.City()
        data = city.to_dict()
    except Exception as e:
        return str(e)
    return True

def test_place():
    try:
        import app.models.place
        place = app.models.place.Place()
        data = place.to_dict()
    except Exception as e:
        return str(e)
    return True

def test_place_book():
    try:
        import app.models.place_book
        place_book = app.models.place_book.PlaceBook()
        data = place_book.to_dict()
    except Exception as e:
        return str(e)
    return True

def test_amenity():
    try:
        import app.models.amenity
        amenity = app.models.amenity.Amenity()
        data = amenity.to_dict()
    except Exception as e:
        return str(e)
    return True

def test_place_amenities():
    try:
        import app.models.place_amenity
        place_amenity = app.models.place_amenity.PlaceAmenities()
    except Exception as e:
        return str(e)
    return True

def test_basemodel():
    try:
        from app.models.base import BaseModel
        basemodel = BaseModel()
        data = basemodel.to_dict()
    except Exception as e:
        return str(e)
    return True

def test_password_update():
    #TODO
    pass

def test_fail():
    return "This test is supposed to fail. It is a meta-test."

def test_all():
    tests = [
        test_user,
        test_city,
        test_state,
        test_imports,
        test_basemodel,
        test_place,
        test_place_book,
        test_amenity,
        test_place_amenities,
#        test_fail,
    ]

    total_num_tests = len(tests)
    tests_run = 0
    tests_passed = 0
    tests_failed = 0

    for test in tests:
        tests_run += 1

        response = test()

        if response == True:
            tests_passed += 1
        else:
            tests_failed += 1
            print "FAILED: " + str(response) + " (" + test.__name__ + ")"

    print "Complete."
    print str(tests_run) + " of " + str(total_num_tests) + " tests ran."
    print str(tests_failed) + " failed, " + str(tests_passed) + " passed."

if __name__ == "__main__":
    test_all()
