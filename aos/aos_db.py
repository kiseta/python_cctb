import psycopg2
from config import config


def get_account(user_email):
    """ query data from the account table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT email FROM account WHERE email = '{user_email}'")
        print("The number of records: ", cur.rowcount)
        if cur.rowcount == 1:
            print(f'User record {user_email} is confirmed in the database')
        row = cur.fetchone()

        while row is not None:
            print(row)
            for i in row:
                print(i)
                if i == user_email:
                    print(f'User is confirmed')
                    break
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_inventory():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM product WHERE productstatus = 'Active'")
        instock_list = [i[0] for i in cur.fetchall()]
        cur.close()
        return instock_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#get_account('jonathanphel@yahoo.com')

# instock_inventory = get_inventory()
# print(instock_inventory)