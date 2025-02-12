from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "race_ave_true_skill"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, 25 )
    race_ave_true_skill = dm.pickle_load( "race_ave_true_skill.pickle" )

    for race_id in tqdm( race_ave_true_skill.keys() ):
        race_data.update_race_data( COLUM_NAME, race_ave_true_skill[race_id], race_id )

if __name__ == "__main__":
    main()
