from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "money"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, -1 )
    race_money_data = dm.pickle_load( "race_money_data.pickle" )

    for race_id in tqdm( race_money_data.keys() ):
        race_data.update_race_data( COLUM_NAME, race_money_data[race_id], race_id )

if __name__ == "__main__":
    main()
