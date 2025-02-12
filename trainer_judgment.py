import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "trainer_judgment"

def main():
    race_horce_data = ps.RaceHorceData()
    trainer_data = ps.TrainerData()

    race_horce_data.add_colum( COLUM_NAME, "{}" )
    trainer_data.add_colum( COLUM_NAME, "{}" )

    trainer_judgment_data = dm.pickle_load( "trainer_judgment_data.pickle" )
    trainer_judgment_prod_data = dm.pickle_load( "trainer_judgment_prod_data.pickle" )

    for race_id in tqdm( trainer_judgment_data.keys() ):
        for horce_id in trainer_judgment_data[race_id].keys():
            race_horce_data.update_data( COLUM_NAME, \
                                        json.dumps( trainer_judgment_data[race_id][horce_id], ensure_ascii = False ), \
                                        race_id, horce_id, "horce_id" )

    for trainer_id in tqdm( trainer_judgment_prod_data.keys() ):
        trainer_data.update_data( COLUM_NAME, \
                                 json.dumps( trainer_judgment_prod_data[trainer_id], ensure_ascii = False ), \
                                 trainer_id )

if __name__ == "__main__":
    main()
