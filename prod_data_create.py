import SekitobaDataManage as dm
import SekitobaLibrary as lib
import SekitobaPsql as ps

def main():
    prod_data = ps.ProdData()
    prod_data.create_table()
    prod_data.insert_data()

if __name__ == "__main__":
    main()
