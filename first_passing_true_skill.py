from tqdm import tqdm
import sekitoba_data_manage as dm
import sekitoba_psql as ps

COLUM_NAME = "first_passing_true_skill"

def main():
    race_horce_data = ps.RaceHorceData()
    horce_data = ps.HorceData()
    jockey_data = ps.JockeyData()
    trainer_data = ps.TrainerData()
    race_horce_data.add_colum( "horce_" + COLUM_NAME, -1000 )
    race_horce_data.add_colum( "jockey_" + COLUM_NAME, -1000 )
    race_horce_data.add_colum( "trainer_" + COLUM_NAME, -1000 )
    horce_data.add_colum( COLUM_NAME, -1000 )
    jockey_data.add_colum( COLUM_NAME, -1000 )
    trainer_data.add_colum( COLUM_NAME, -1000 )
    
    first_passing_true_skill_data = dm.pickle_load( "first_passing_true_skill_data.pickle" )
    first_passing_true_skill_prod_data = dm.pickle_load( "first_passing_true_skill_prod_data.pickle" )

    for kind in first_passing_true_skill_prod_data.keys():
        for data_id in tqdm( first_passing_true_skill_prod_data[kind].keys() ):
            if kind == "horce":
                horce_data.update_data( COLUM_NAME, first_passing_true_skill_prod_data[kind][data_id], data_id )
            elif kind == "jockey":
                jockey_data.update_data( COLUM_NAME, first_passing_true_skill_prod_data[kind][data_id], data_id )
            elif kind == "trainer":
                trainer_data.update_data( COLUM_NAME, first_passing_true_skill_prod_data[kind][data_id], data_id )
    
    for kind in first_passing_true_skill_data.keys():
        for race_id in tqdm( first_passing_true_skill_data[kind].keys() ):
            for horce_id in first_passing_true_skill_data[kind][race_id].keys():
                race_horce_data.update_data( kind + "_" + COLUM_NAME, \
                                      first_passing_true_skill_data[kind][race_id][horce_id], \
                                      race_id, horce_id, kind + "_id" )

if __name__ == "__main__":
    main()