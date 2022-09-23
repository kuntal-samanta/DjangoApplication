from django.shortcuts import render

# Create your views here.

'''
# demo views.py {Query Example}

""" All our db query will be here """
def demo(request):

    """ One To One Insert
    u = User(username="user@123", email="user123@mail.com", first_name="Alex")
    u.save()
    ud = UserDetails(
        user=u,
        phone="9632584567"
    )
    ud.save()
    
    # fetching
    u = User.objects.get(email="user123@mail.com")
    print(u.first_name)
    ud = UserDetails.objects.get(user__email="user123@mail.com")
    print(u.first_name)
    ud = UserDetails.objects.get(user__id=u.id)
    print(ud.phone)
    """

    """
    # FK Insert
    b = Batch(
        batch_id=55,
        batch_name="new batchsw"
    )
    b.save()
    s = Student(
        name="John",
        email="jhon@mail.com",
        batch=b
    )
    s.save()

    # Fetch
    s = Student.objects.get(email="jhon@mail.com")
    print(s.name)
    print(s.batch.batch_name)
    """

    """ 
    Mant To Many
    # Insert
    c = Course(name="course 51", year=2018)
    c.save()
    c1 = Course(name="course 52", year=2018)
    c1.save()
    c2 = Course(name="course 53", year=2018)
    c2.save()

    p = Person(last_name="gfhjb", first_name="ghjk")
    p.save()
    p.courses.add(c)
    p.courses.add(c1)
    p.courses.add(c2)

    # Fetch
    p = Person.objects.get(last_name="gfhjb")
    o = p.courses.all()
    for i in p.courses.all():
        print(i.name)
    """

    return HttpResponse("hi")

'''
