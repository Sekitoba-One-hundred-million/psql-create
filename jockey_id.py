from tqdm import tqdm
import sekitoba_data_manage as dm
import sekitoba_psql as ps

def main():
    race_horce_data = ps.RaceHorceData()
    race_horce_data.add_colum( "jockey_id", "None" )    
    race_jockey_id_data = dm.pickle_load( "race_jockey_id_data.pickle" )

    for race_id in tqdm( race_jockey_id_data.keys() ):
        for horce_id in race_jockey_id_data[race_id].keys():
            race_horce_data.update_data( "jockey_id", race_jockey_id_data[race_id][horce_id], race_id, horce_id )

if __name__ == "__main__":
    main()
