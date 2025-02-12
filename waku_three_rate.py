import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "waku_three_rate"

def main():
    race_data = ps.RaceData()
    prod_data = ps.ProdData()
    race_data.add_colum( COLUM_NAME, "{}" )
    prod_data.add_colum( COLUM_NAME, "{}" )
    waku_three_rate = dm.pickle_load( "waku_three_rate_data.pickle" )
    waku_three_rate_prod = dm.pickle_load( "waku_three_rate_prod_data.pickle" )

    for race_id in tqdm( waku_three_rate.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( waku_three_rate[race_id], ensure_ascii = False ), race_id )

    prod_data.update_data( COLUM_NAME, json.dumps( waku_three_rate_prod, ensure_ascii = False ) )

if __name__ == "__main__":
    main()
