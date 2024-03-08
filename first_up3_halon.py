import json
from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "first_up3_halon"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    first_up3_halon = dm.pickle_load( "first_up3_halon.pickle" )

    for race_id in tqdm( first_up3_halon.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( first_up3_halon[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
