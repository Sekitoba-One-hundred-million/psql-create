import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "win_rate"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    win_rate = dm.pickle_load( "rate_data.pickle" )

    for race_id in tqdm( win_rate.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( win_rate[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
