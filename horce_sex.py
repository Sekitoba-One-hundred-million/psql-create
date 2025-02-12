import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "sex"

def main():
    horce_data = ps.HorceData()
    horce_data.add_colum( COLUM_NAME, -1000 )
    horce_sex_data = dm.pickle_load( "horce_sex_data.pickle" )

    for horce_id in tqdm( horce_sex_data.keys() ):
        horce_data.update_data( COLUM_NAME, horce_sex_data[horce_id], horce_id )

if __name__ == "__main__":
    main()
