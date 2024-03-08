from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

def main():
    race_data = ps.RaceData()
    race_data.add_colum( "kind", -1 )
    race_data.add_colum( "baba", -1 )
    race_data.add_colum( "dist", -1 )
    race_data.add_colum( "place", -1 )
    race_data.add_colum( "out_side", False )
    race_data.add_colum( "direction", -1 )
    race_info_data = dm.pickle_load( "race_info_data.pickle" )

    for race_id in tqdm( race_info_data.keys() ):
        for kind in race_info_data[race_id].keys():
            race_data.update_race_data( kind, race_info_data[race_id][kind], race_id )

if __name__ == "__main__":
    main()
