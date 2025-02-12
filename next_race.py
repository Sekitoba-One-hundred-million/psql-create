import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "next_race"

def main():
    race_horce_data = ps.RaceHorceData()
    race_horce_data.add_colum( COLUM_NAME, "[]" )
    next_race_data = dm.pickle_load( "next_race_data.pickle" )

    for race_id in tqdm( next_race_data.keys() ):
        for horce_id in next_race_data[race_id].keys():
            print( race_id, horce_id, next_race_data[race_id][horce_id] )
            race_horce_data.update_data( COLUM_NAME, json.dumps( next_race_data[race_id][horce_id], ensure_ascii = False ), \
                                        race_id, horce_id, "horce_id" )

if __name__ == "__main__":
    main()
