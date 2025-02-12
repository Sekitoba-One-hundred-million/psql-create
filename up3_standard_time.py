import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "up3_standard_time"

def main():
    race_data = ps.RaceData()
    prod_data = ps.ProdData()
    race_data.add_colum( COLUM_NAME, "{}" )
    prod_data.add_colum( COLUM_NAME, "{}" )
    standard_time = dm.pickle_load( "up3_standard_time.pickle" )
    standard_prod_time = dm.pickle_load( "up3_standard_prod_time.pickle" )

    for race_id in tqdm( standard_time.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( standard_time[race_id], ensure_ascii = False ), race_id )

    prod_data.update_data( COLUM_NAME, json.dumps( standard_prod_time, ensure_ascii = False ) )

if __name__ == "__main__":
    main()
