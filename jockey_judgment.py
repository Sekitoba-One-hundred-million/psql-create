import json
from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "jockey_judgment"

def main():
    race_horce_data = ps.RaceHorceData()
    jockey_data = ps.JockeyData()

    race_horce_data.add_colum( COLUM_NAME, "{}" )
    jockey_data.add_colum( COLUM_NAME, "{}" )

    jockey_judgment_data = dm.pickle_load( "jockey_judgment_data.pickle" )
    jockey_judgment_prod_data = dm.pickle_load( "jockey_judgment_prod_data.pickle" )

    for race_id in tqdm( jockey_judgment_data.keys() ):
        for horce_id in jockey_judgment_data[race_id].keys():
            race_horce_data.update_data( COLUM_NAME, \
                                        json.dumps( jockey_judgment_data[race_id][horce_id], ensure_ascii = False ), \
                                        race_id, horce_id, "horce_id" )

    for jockey_id in tqdm( jockey_judgment_prod_data.keys() ):
        jockey_data.update_data( COLUM_NAME, \
                                json.dumps( jockey_judgment_prod_data[jockey_id], ensure_ascii = False ), \
                                jockey_id )

if __name__ == "__main__":
    main()
