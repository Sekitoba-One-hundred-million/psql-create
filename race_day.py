from tqdm import tqdm

import sekitoba_data_manage as dm
import sekitoba_psql as ps

def main():
    race_data = ps.RaceData()
    race_data.add_colum( "year", -1 )
    race_data.add_colum( "month", -1 )
    race_data.add_colum( "day", -1 )
    race_day_data = dm.pickle_load( "race_day.pickle" )

    for race_id in tqdm( race_day_data.keys() ):
        for kind in race_day_data[race_id].keys():
            race_data.update_race_data( kind, race_day_data[race_id][kind], race_id )

if __name__ == "__main__":
    main()
