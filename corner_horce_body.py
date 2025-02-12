import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "corner_horce_body"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    corner_horce_body_data = dm.pickle_load( "corner_horce_body.pickle" )
    
    for race_id in tqdm( corner_horce_body_data.keys() ):
        race_data.update_data( COLUM_NAME, \
                              json.dumps( corner_horce_body_data[race_id], ensure_ascii = False ), \
                              race_id )


if __name__ == "__main__":
    main()
