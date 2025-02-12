import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "parent_id"

def main():
    horce_data = ps.HorceData()
    horce_data.add_colum( COLUM_NAME, -1000 )
    parent_id_data = dm.pickle_load( "parent_id_data.pickle" )

    for horce_id in tqdm( parent_id_data.keys() ):
        if not "father" in parent_id_data[horce_id]:
            print( horce_id, parent_id_data[horce_id] )
            
        horce_data.update_data( COLUM_NAME, json.dumps( parent_id_data[horce_id] ), horce_id )

if __name__ == "__main__":
    main()
