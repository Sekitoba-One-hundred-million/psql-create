import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "flame_evaluation"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    
    flame_evaluation_data = dm.pickle_load( "flame_evaluation_data.pickle" )
    
    for race_id in tqdm( flame_evaluation_data.keys() ):
        race_data.update_data( COLUM_NAME, \
                              json.dumps( flame_evaluation_data[race_id] ), \
                              race_id )

if __name__ == "__main__":
    main()
