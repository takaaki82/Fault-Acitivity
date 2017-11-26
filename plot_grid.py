import numpy as np
import pandas as pd


def plot_grid():

    # xmin, ymin , xmax, ymax
    SHIKOKU_BOX = [31.0, 129.0, 34.0, 132.0]
    KYUSYU_BOX = [33.7, 130.7, 35.7, 135.0]

    # degree per 20km
    LON_DEGREE = 20 / 93.45286
    LAT_DEGREE = 20 / 111.263

    grid2SHIKOKU = pd.DataFrame(index=[], columns=["center-point", "bbox"])
    for lon in np.arange(start=SHIKOKU_BOX[0], stop=SHIKOKU_BOX[2], step=LON_DEGREE, dtype=float):

        for lat in np.arange(start=SHIKOKU_BOX[1], stop=SHIKOKU_BOX[3], step=LAT_DEGREE, dtype=float):

            center_point = [lon, lat]
            bbox = [lon - LON_DEGREE, lat - LAT_DEGREE, lon + LON_DEGREE, lat + LAT_DEGREE]
            grid_data = [center_point, bbox]
            grid_data = pd.Series(grid_data, index=grid2SHIKOKU.columns)
            grid2SHIKOKU = grid2SHIKOKU.append(grid_data, ignore_index=True)

    grid2KYUSYU = pd.DataFrame(index=[], columns=["center-point", "bbox"])
    for lon in np.arange(start=KYUSYU_BOX[0], stop=KYUSYU_BOX[2], step=LON_DEGREE, dtype=float):

        for lat in np.arange(start=KYUSYU_BOX[1], stop=KYUSYU_BOX[3], step=LAT_DEGREE, dtype=float):

            center_point = lon, lat
            bbox = (lon - LON_DEGREE, lat - LAT_DEGREE, lon + LON_DEGREE, lat + LAT_DEGREE)
            grid_data = [center_point, bbox]
            grid_data = pd.Series(grid_data, index=grid2SHIKOKU.columns)
            grid2KYUSYU = grid2KYUSYU.append(grid_data, ignore_index=True)

    grid2KYUSYU.to_csv("csv/grid-KYUSYU.csv")
    grid2SHIKOKU.to_csv("csv/grid-SHIKOKU.csv")

if __name__ == '__main__':
    plot_grid()