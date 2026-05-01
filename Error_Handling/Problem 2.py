def divide(x,y):
    try:


        z = x / y
        print(z)

    except:
        print("error dividing on zero try again")
    finally:
        print('All done')

divide(5,0)