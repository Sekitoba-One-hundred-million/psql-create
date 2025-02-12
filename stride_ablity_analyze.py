import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "stride_ablity_analyze"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    stride_ablity_analyze = dm.pickle_load( "stride_ablity_analyze_data.pickle" )

    for race_id in tqdm( stride_ablity_analyze.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( stride_ablity_analyze[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
