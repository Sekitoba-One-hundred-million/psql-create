import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "baba_index"

def main():
    horce_data = ps.HorceData()
    horce_data.add_colum( COLUM_NAME, "{}" )
    baba_index_data = dm.pickle_load( "baba_index_data.pickle" )

    for horce_id in tqdm( baba_index_data.keys() ):
        horce_data.update_data( COLUM_NAME, json.dumps( baba_index_data[horce_id], ensure_ascii = False ), horce_id )

if __name__ == "__main__":
    main()
