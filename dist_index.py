import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "dist_index"

def main():
    dist_index_data = dm.pickle_load( "dist_index.pickle" )
    race_data = ps.RaceData()
    prod_data = ps.ProdData()
    race_id_list = race_data.get_all_race_id()
    race_data.add_colum( COLUM_NAME, "{}" )
    prod_data.add_colum( COLUM_NAME, "{}" )

    prod_data.update_data( COLUM_NAME, json.dumps( dist_index_data, ensure_ascii = False ) )

    for race_id in tqdm( race_id_list ):
        race_data.update_data( COLUM_NAME, json.dumps( dist_index_data, ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
