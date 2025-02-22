import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "run_circle_dist"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    run_circle_dist_data = dm.pickle_load( "run_circle_dist_data.pickle" )

    for race_id in tqdm( run_circle_dist_data.keys() ):
        race_data.update_data( COLUM_NAME, \
                              json.dumps( run_circle_dist_data[race_id], ensure_ascii = False ), \
                              race_id )

if __name__ == "__main__":
    main()
