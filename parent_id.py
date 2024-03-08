import json
from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "parent_id"

def main():
    horce_data = ps.HorceData()
    horce_data.add_colum( COLUM_NAME, -1000 )
    parent_id_data = dm.pickle_load( "parent_id_data.pickle" )

    for horce_id in tqdm( parent_id_data.keys() ):
        horce_data.update_data( COLUM_NAME, json.dumps( parent_id_data[horce_id] ), horce_id )

if __name__ == "__main__":
    main()
