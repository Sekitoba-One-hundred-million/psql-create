import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "up_pace_regressin"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, -1 )
    up_pace_regressin = dm.pickle_load( "up_pace_regressin_data.pickle" )

    for race_id in tqdm( up_pace_regressin.keys() ):
        race_data.update_data( COLUM_NAME, json.dumps( up_pace_regressin[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
