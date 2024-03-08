import json
from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "standard_time"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    standard_time = dm.pickle_load( "standard_time.pickle" )

    for race_id in tqdm( standard_time.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( standard_time[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
