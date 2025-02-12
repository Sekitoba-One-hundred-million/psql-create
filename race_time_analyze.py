import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "race_time_analyze"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( "race_time_analyze", "{}" )
    race_time_analyze = dm.pickle_load( "race_time_analyze_data.pickle" )

    for race_id in tqdm( race_time_analyze.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( race_time_analyze[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
