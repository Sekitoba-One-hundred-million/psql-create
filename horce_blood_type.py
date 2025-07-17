import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "blood_type"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "" )
    horce_blood_type_data = dm.pickle_load( "horce_blood_type_data.pickle" )

    for race_id in tqdm( horce_blood_type_data.keys() ):
        print( race_id, horce_blood_type_data[race_id] )
        race_data.update_data( COLUM_NAME,
                               json.dumps( horce_blood_type_data[race_id], ensure_ascii = False ),
                               race_id )

if __name__ == "__main__":
    main()
