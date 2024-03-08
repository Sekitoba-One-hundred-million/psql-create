import sekitoba_data_manage as dm
import sekitoba_library as lib
import sekitoba_psql as ps

def main():
    race_data = ps.RaceData()
    race_horce_data = ps.RaceHorceData()
    horce_data = ps.HorceData()
    jockey_data = ps.JockeyData()
    trainer_data = ps.TrainerData()
    
    race_data.create_table()
    race_horce_data.create_table()
    horce_data.create_table()
    jockey_data.create_table()
    trainer_data.create_table()

    race_data_data = dm.pickle_load( "race_data.pickle" )
    horce_data_storage = dm.pickle_load( "horce_data_storage.pickle")
    trainer_id_data = dm.pickle_load( "trainer_id_data.pickle" )
    jockey_id_data = dm.pickle_load( "jockey_id_data.pickle" )
    
    race_data.insert_data( race_data_data )
    race_horce_data.insert_data( race_data_data )
    jockey_data.insert_data( list( jockey_id_data.keys() ) )
    trainer_data.insert_data( list( trainer_id_data.keys() ) )
    horce_data.insert_data( horce_data_storage )

if __name__ == "__main__":
    main()
