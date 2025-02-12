import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "trainer_analyze"

def main():
    trainer_data = ps.TrainerData()
    trainer_data.add_colum( COLUM_NAME, "{}" )
    trainer_analyze_data = dm.pickle_load( "trainer_analyze_data.pickle" )

    for trainer_id in tqdm( trainer_analyze_data.keys() ):
        trainer_data.update_data( COLUM_NAME, \
                                 json.dumps( trainer_analyze_data[trainer_id], ensure_ascii = False ), \
                                 trainer_id )

if __name__ == "__main__":
    main()
