# this is the file that we used to process the raw data and create the intermediate files
# The intermediate files are used to create the final datasets
import utils.files.check as check_utils
import utils.files.log as log_utils
import utils.dewey as dewey_utils
import utils.data_structure.list as list_utils
import utils.data_structure.dict as dict_utils
import utils.data_structure.dataframe as dataframe_utils
import pandas
import os
import sys

pandas.set_option("future.no_silent_downcasting", True)
import time


def get_naics_grouped_input_df(input_df, lenghts=[2, 4, 6], verbose=True):
    naics_grouped_list = []
    for length in lenghts:
        niacs_df = get_trim_niacs_code(input_df, length=length, verbose=verbose)
        print(f"length:{length} len(niacs_df[naics_code].unique()): {len(niacs_df['naics_code'].unique())}")
        naics_grouped_list.append(niacs_df)
    naics_grouped_df = pandas.concat(naics_grouped_list)
    return naics_grouped_df


def get_trim_niacs_code(input_df, length=2, verbose=True):
    df = input_df.copy()
    df["naics_code"] = df["naics_code"].astype(str)
    df["naics_code"] = df["naics_code"].apply(lambda x: x[:length] if len(x) >= length else None)
    if length == 2:
        # 31,32,33 -> 31
        # 44,45 -> 44
        # 48,49 -> 48
        df["naics_code"] = df["naics_code"].apply(lambda x: x if x not in ["31", "32", "33"] else "31")
        df["naics_code"] = df["naics_code"].apply(lambda x: x if x not in ["44", "45"] else "44")
        df["naics_code"] = df["naics_code"].apply(lambda x: x if x not in ["48", "49"] else "48")
    if verbose:
        print(f"Trimming naics_code to {length} length")
        print(df.head())
    return df


def get_aggregated_df(input_df, column="raw_visit_counts", group_by_column="naics_code", verbose=True):
    if verbose:
        print(f"Aggregating {column} by {group_by_column}")
        print(input_df.head())
    aggregated_df = (
        input_df.groupby(group_by_column)
        .agg(
            # weighted_mean=(column, lambda x: (x * input_df[column]).sum() / input_df[column].sum()),
            count=(column, "count"),
            mean=(column, "mean"),
            std=(column, "std"),
            min=(column, "min"),
            q1=(column, lambda x: x.quantile(0.25)),
            q2=(column, lambda x: x.quantile(0.5)),
            q3=(column, lambda x: x.quantile(0.75)),
            max=(column, "max"),
            sum=(column, "sum"),
        )
        .reset_index()
    )
    return aggregated_df


if __name__ == "__main__":
    section = 0
    if len(sys.argv) > 1:
        section = int(sys.argv[1])
        max_section = int(sys.argv[2])

    dataset_class = "weekly"
    data_path = "data/p2"
    metric_names = ["mean", "q2", "count", "sum"]
    for metric_name in metric_names:
        refresh_intermediate_file = False
        visit_csv_path = f"{data_path}/{dataset_class}/visits_{metric_name}.csv"
        visitor_csv_path = f"{data_path}/{dataset_class}/visitors_{metric_name}.csv"
        distance_csv_path = f"{data_path}/{dataset_class}/distance_{metric_name}.csv"
        dwell_csv_path = f"{data_path}/{dataset_class}/dwell_{metric_name}.csv"

        process_time_start = time.time()
        partition_keys = dewey_utils.get_partition_keys()

        useful_columns = ["placekey", "parent_placekey", "naics_code", "raw_visit_counts", "raw_visitor_counts", "distance_from_home", "median_dwell"]
        visits_df = pandas.DataFrame()
        visitors_df = pandas.DataFrame()
        distance_df = pandas.DataFrame()
        dwell_df = pandas.DataFrame()
        if section != 0:
            partition_keys = list_utils.get_section(partition_keys, section, max_section)
        for partition_key in partition_keys:
            print(f"Processing {partition_key}")
            loop_time_start = time.time()
            visitor_csv_intermediate_file_path = visitor_csv_path.replace(f"_{metric_name}.csv", f"_{partition_key}.csv")
            visitor_csv_path_statistics = visitor_csv_path.replace(f"_{metric_name}.csv", f"_{partition_key}_statistics.csv")
            distance_csv_intermediate_file_path = distance_csv_path.replace(f"_{metric_name}.csv", f"_{partition_key}.csv")
            distance_csv_path_statistics = distance_csv_path.replace(f"_{metric_name}.csv", f"_{partition_key}_statistics.csv")
            dwell_csv_intermediate_file_path = dwell_csv_path.replace(f"_{metric_name}.csv", f"_{partition_key}.csv")
            dwell_csv_path_statistics = dwell_csv_path.replace(f"_{metric_name}.csv", f"_{partition_key}_statistics.csv")
            input_df = pandas.DataFrame()
            grouped_input_df = pandas.DataFrame()

            try:
                if not check_utils.exists(visitor_csv_path_statistics):
                    print(f"File {visitor_csv_path_statistics} not available")
                    print(f"Getting visitor for {partition_key}")
                    if len(input_df) == 0:
                        input_df = dewey_utils.get_partition_key_df(partition_key, useful_columns, dataset_class, data_path, verbose=True)
                    if len(grouped_input_df) == 0:
                        grouped_input_df = get_naics_grouped_input_df(input_df, verbose=True)

                    partition_aggregated_visitors_df = get_aggregated_df(grouped_input_df, "raw_visitor_counts", "naics_code")
                    partition_aggregated_visitors_df.to_csv(visitor_csv_path_statistics, index=False)
                    partition_visitors_df = partition_aggregated_visitors_df[["naics_code", metric_name]]
                    partition_visitors_df.to_csv(visitor_csv_intermediate_file_path, index=False)
                    partition_visitors_df.columns = ["naics_code", f"{partition_key}"]
                    visitors_df = pandas.merge(visitors_df, partition_visitors_df, on="naics_code", how="outer") if not visitors_df.empty else partition_visitors_df
                else:
                    print(f"Already exists {visitor_csv_path_statistics}")
                    partition_aggregated_visitors_df = pandas.read_csv(visitor_csv_path_statistics)
                    partition_visitors_df = partition_aggregated_visitors_df[["naics_code", metric_name]]
                    partition_visitors_df.to_csv(visitor_csv_intermediate_file_path, index=False)
                    partition_visitors_df.columns = ["naics_code", f"{partition_key}"]
                    visitors_df = pandas.merge(visitors_df, partition_visitors_df, on="naics_code", how="outer") if not visitors_df.empty else partition_visitors_df

                visitors_df.to_csv(visitor_csv_path, index=False)

            except Exception as e:
                print(f"Error in visitor for {partition_key}")
                log_utils.error(e, file=f"logs/error_{partition_key}.log")

            try:
                if not check_utils.exists(distance_csv_path_statistics):
                    print(f"File {distance_csv_path_statistics} not available")
                    print(f"Getting distance for {partition_key}")
                    if len(input_df) == 0:
                        input_df = dewey_utils.get_partition_key_df(partition_key, useful_columns, dataset_class, data_path, verbose=True)
                    if len(grouped_input_df) == 0:
                        grouped_input_df = get_naics_grouped_input_df(input_df)

                    partition_aggregated_distance_df = get_aggregated_df(grouped_input_df, "distance_from_home", "naics_code")
                    partition_aggregated_distance_df.to_csv(distance_csv_path_statistics, index=False)
                    partition_distance_df = partition_aggregated_distance_df[["naics_code", metric_name]]
                    partition_distance_df.to_csv(distance_csv_intermediate_file_path, index=False)
                    partition_distance_df.columns = ["naics_code", f"{partition_key}"]
                    distance_df = pandas.merge(distance_df, partition_distance_df, on="naics_code", how="outer") if not distance_df.empty else partition_distance_df
                    distance_df.to_csv(distance_csv_path, index=False)
                else:
                    print(f"Already exists {distance_csv_path_statistics}")
                    partition_aggregated_distance_df = pandas.read_csv(distance_csv_path_statistics)
                    partition_distance_df = partition_aggregated_distance_df[["naics_code", metric_name]]
                    partition_distance_df.to_csv(distance_csv_intermediate_file_path, index=False)
                    partition_distance_df.columns = ["naics_code", f"{partition_key}"]
                    distance_df = pandas.merge(distance_df, partition_distance_df, on="naics_code", how="outer") if not distance_df.empty else partition_distance_df

                distance_df.to_csv(distance_csv_path, index=False)

            except Exception as e:
                print(f"Error in distance for {partition_key}")
                log_utils.error(e, file=f"logs/error_{partition_key}.log")

            try:

                if not check_utils.exists(dwell_csv_path_statistics):
                    print(f"File {dwell_csv_path_statistics} not available")
                    print(f"Getting dwell for {partition_key}")
                    if len(input_df) == 0:
                        input_df = dewey_utils.get_partition_key_df(partition_key, useful_columns, dataset_class, data_path, verbose=True)
                    if len(grouped_input_df) == 0:
                        grouped_input_df = get_naics_grouped_input_df(input_df)

                    partition_aggregated_dwell_df = get_aggregated_df(grouped_input_df, "median_dwell", "naics_code")
                    partition_aggregated_dwell_df.to_csv(dwell_csv_path_statistics, index=False)
                    partition_dwell_df = partition_aggregated_dwell_df[["naics_code", metric_name]]
                    partition_dwell_df.to_csv(dwell_csv_intermediate_file_path, index=False)
                    partition_dwell_df.columns = ["naics_code", f"{partition_key}"]
                    dwell_df = pandas.merge(dwell_df, partition_dwell_df, on="naics_code", how="outer") if not dwell_df.empty else partition_dwell_df
                    dwell_df.to_csv(dwell_csv_path, index=False)

                else:
                    print(f"Already exists {dwell_csv_path_statistics}")
                    partition_aggregated_dwell_df = pandas.read_csv(dwell_csv_path_statistics)
                    partition_dwell_df = partition_aggregated_dwell_df[["naics_code", metric_name]]
                    partition_dwell_df.to_csv(dwell_csv_intermediate_file_path, index=False)
                    partition_dwell_df.columns = ["naics_code", f"{partition_key}"]
                    dwell_df = pandas.merge(dwell_df, partition_dwell_df, on="naics_code", how="outer") if not dwell_df.empty else partition_dwell_df

                dwell_df.to_csv(dwell_csv_path, index=False)

            except Exception as e:
                print(f"Error in dwell for {partition_key}")
                log_utils.error(e, file=f"logs/error_{partition_key}.log")

            loop_time_end = time.time()
            print(f"Time taken for {partition_key} is {loop_time_end - loop_time_start}")

        process_time_end = time.time()
        print(f"Total time taken is {process_time_end - process_time_start}")
