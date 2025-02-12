import json
from tqdm import tqdm

import SekitobaDataManage as dm
import SekitobaPsql as ps

COLUM_NAME = "jockey_year_rank"

def main():
    jockey_data = ps.JockeyData()
    jockey_data.add_colum( COLUM_NAME, "{}" )
    jockey_year_rank_data = dm.pickle_load( "jockey_year_rank_data.pickle" )

    for jockey_id in tqdm( jockey_year_rank_data.keys() ):
        jockey_data.update_data( COLUM_NAME, \
                                 json.dumps( jockey_year_rank_data[jockey_id], ensure_ascii = False ), \
                                 jockey_id )

if __name__ == "__main__":
    main()
