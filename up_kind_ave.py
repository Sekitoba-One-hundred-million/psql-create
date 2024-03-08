import json
from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "up_kind_ave"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    up_kind_ave_data = dm.pickle_load( "up_kind_ave_data.pickle" )

    for race_id in tqdm( up_kind_ave_data.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( up_kind_ave_data[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
