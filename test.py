from tqdm import tqdm
import sekitoba_psql as ps

def main():
    horce_data = ps.HorceData()
    race_data = ps.RaceData()
    all_race_id = race_data.get_all_race_id()
    horce_id_list = race_data.get_horce_id( all_race_id[-1] )

    for race_id in tqdm( all_race_id ):
        horce_id_list = race_data.get_horce_id( race_id )
        h_data = horce_data.get_multi_data( horce_id_list )
        #for horce_id in horce_id_list:
        #    h_data = horce_data.get_data( horce_id )

if __name__ == "__main__":
    main()
