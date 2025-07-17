import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "blood_type_score"

def main():
    race_data = ps.RaceData()
    prod_data = ps.ProdData()
    race_data.add_colum( COLUM_NAME, "{}" )
    prod_data.add_colum( COLUM_NAME, "{}" )
    blood_type_score_data = dm.pickle_load( "blood_type_score_data.pickle" )
    prod_blood_type_score_data = dm.pickle_load( "prod_blood_type_score_data.pickle" )

    for race_id in tqdm( blood_type_score_data.keys() ):
        race_data.update_data( COLUM_NAME, json.dumps( blood_type_score_data[race_id], ensure_ascii = False ), race_id )

    prod_data.update_data( COLUM_NAME, json.dumps( prod_blood_type_score_data, ensure_ascii = False ) )

if __name__ == "__main__":
    main()
