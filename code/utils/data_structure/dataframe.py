import pandas
import utils.data_structure.list as list_utils
import utils.files.path as path_utils
import utils.files.check as check_utils


def get_intersection(source_row, destination_df, column_name_node="poi_cbg", list_of_values_column_name="list_of_values"):
    intersection_counts = destination_df[list_of_values_column_name].apply(lambda list_destination: list_utils.get_intersection(source_row[list_of_values_column_name], list_destination, count=True))

    intersection_df = pandas.DataFrame({f"{column_name_node}_source": source_row[column_name_node], f"{column_name_node}_destination": destination_df[column_name_node], "intersection_count": intersection_counts})

    intersection_df = intersection_df[intersection_df[f"{column_name_node}_source"] != intersection_df[f"{column_name_node}_destination"]]
    return intersection_df


def concat(dfs, flush_path=None, flush_threshold=1000000, verbose=False):
    if flush_path is None:
        return pandas.concat(dfs)
    else:
        df = pandas.concat(dfs)

        if len(df) > flush_threshold:
            if verbose:
                print(f"Flushing {flush_path}")
            if not check_utils.exists(flush_path):
                df.to_csv(flush_path, index=False)
                return pandas.DataFrame()
            else:
                previous_df = pandas.read_csv(flush_path)
                df = pandas.concat([previous_df, df])
                df.to_csv(flush_path, index=False)
                return pandas.DataFrame()
        return df
