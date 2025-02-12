import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "money_class_true_skill"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "{}" )
    money_class_true_skill_data = dm.pickle_load( "money_class_true_skill_data.pickle" )

    for race_id in tqdm( money_class_true_skill_data.keys() ):
        race_data.update_race_data( COLUM_NAME, json.dumps( money_class_true_skill_data[race_id], ensure_ascii = False ), race_id )

if __name__ == "__main__":
    main()
