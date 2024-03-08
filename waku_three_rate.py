import json
from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "waku_three_rate"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    waku_three_rate = dm.pickle_load( "waku_three_rate_data.pickle" )

    for race_id in tqdm( waku_three_rate.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( waku_three_rate[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
