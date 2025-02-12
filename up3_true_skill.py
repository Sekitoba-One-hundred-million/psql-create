from tqdm import tqdm
import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "up3_true_skill"

def main():
    race_horce_data = ps.RaceHorceData()
    horce_data = ps.HorceData()
    jockey_data = ps.JockeyData()
    trainer_data = ps.TrainerData()
    race_horce_data.add_colum( "horce_" + COLUM_NAME, 25 )
    race_horce_data.add_colum( "jockey_" + COLUM_NAME, 25 )
    race_horce_data.add_colum( "trainer_" + COLUM_NAME, 25 )
    horce_data.add_colum( COLUM_NAME, 25 )
    jockey_data.add_colum( COLUM_NAME, 25 )
    trainer_data.add_colum( COLUM_NAME, 25 )
    
    up3_true_skill_data = dm.pickle_load( "up3_true_skill_data.pickle" )
    up3_true_skill_prod_data = dm.pickle_load( "up3_true_skill_prod_data.pickle" )

    for kind in up3_true_skill_prod_data.keys():
        for data_id in tqdm( up3_true_skill_prod_data[kind].keys() ):
            if kind == "horce":
                horce_data.update_data( COLUM_NAME, up3_true_skill_prod_data[kind][data_id], data_id )
            elif kind == "jockey":
                jockey_data.update_data( COLUM_NAME, up3_true_skill_prod_data[kind][data_id], data_id )
            elif kind == "trainer":
                trainer_data.update_data( COLUM_NAME, up3_true_skill_prod_data[kind][data_id], data_id )
    
    for kind in up3_true_skill_data.keys():
        for race_id in tqdm( up3_true_skill_data[kind].keys() ):
            for kind_id in up3_true_skill_data[kind][race_id].keys():
                race_horce_data.update_data( kind + "_up3_true_skill", \
                                            up3_true_skill_data[kind][race_id][kind_id], \
                                            race_id, kind_id, kind + "_id" )

if __name__ == "__main__":
    main()
