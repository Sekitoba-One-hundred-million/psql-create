import json
from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "time_index"

def main():
    horce_data = ps.HorceData()
    horce_data.add_colum( COLUM_NAME, "{}" )
    time_index_data = dm.pickle_load( "time_index_data.pickle" )

    for horce_id in tqdm( time_index_data.keys() ):
        horce_data.update_data( COLUM_NAME, json.dumps( time_index_data[horce_id], ensure_ascii = False ), horce_id )
    
if __name__ == "__main__":
    main()
