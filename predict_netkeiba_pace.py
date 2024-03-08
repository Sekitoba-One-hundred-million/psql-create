from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "predict_netkeiba_pace"

def main():
    race_data = ps.RaceData()
    race_data.add_colum( COLUM_NAME, "None" )
    predict_netkeiba_pace_data = dm.pickle_load( "predict_netkeiba_pace_data.pickle" )

    for race_id in tqdm( predict_netkeiba_pace_data.keys() ):
        race_data.update_race_data( COLUM_NAME, predict_netkeiba_pace_data[race_id], race_id )

if __name__ == "__main__":
    main()
