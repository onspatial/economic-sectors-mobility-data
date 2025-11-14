import utils.files.check as check_utils
import utils.files.log as log_utils
import utils.string.time as time_utils
import utils.data_structure.list as list_utils
import utils.data_structure.dict as dict_utils
import utils.data_structure.dataframe as dataframe_utils
import utils.dewey as dewey_utils
import pandas
import os
import sys

from .data import get_aggregated_df

pandas.set_option("future.no_silent_downcasting", True)
pandas.options.mode.copy_on_write = True
import time


def get_naics_code_filtered_df(input_df, naics_code="11"):
    start_time = time.time()
    print(f"Getting naics code filtered")
    input_df["naics_code"] = input_df["naics_code"].astype(str)
    filtered_df = input_df[input_df["naics_code"].str.match(f"^{naics_code}", na=False)]
    end_time = time.time()
    print(f"Time taken for naics code filtering is {end_time - start_time}")
    return filtered_df


def get_bbx_filtered_df(input_df, bbx_df, multiplier=1):
    print(f"Getting bbx filtered")
    for index, row in bbx_df.iterrows():
        # print(f"Getting bbx for {row['Name']} with {row['bbx']}")
        if row["bbx"] == "[]":
            continue
        bbx = eval(row["bbx"])
        bbx = list(map(float, bbx))
        area = (bbx[1] - bbx[0]) * (bbx[3] - bbx[2])
        print(f"Area is {area}")
        min_latitude = bbx[0] - (multiplier * area)
        max_latitude = bbx[1] + (multiplier * area)
        min_longitude = bbx[2] - (multiplier * area)
        max_longitude = bbx[3] + (multiplier * area)
        # print(f"Min latitude is {min_latitude}, min longitude is {min_longitude}, max latitude is {max_latitude}, max longitude is {max_longitude}")
        filtered_df = input_df[(input_df["longitude"] <= max_longitude) & (input_df["longitude"] >= min_longitude) & (input_df["latitude"] <= max_latitude) & (input_df["latitude"] >= min_latitude)]

    return filtered_df


def get_coordinate_filtered_df(input_df, coordinate_df, threshold=0.95):
    for index, row in coordinate_df.iterrows():
        min_latitude = row["latitude"] - threshold
        max_latitude = row["latitude"] + threshold
        min_longitude = row["longitude"] - threshold
        max_longitude = row["longitude"] + threshold
        filtered_df = input_df[(input_df["longitude"] <= max_longitude) & (input_df["longitude"] >= min_longitude) & (input_df["latitude"] <= max_latitude) & (input_df["latitude"] >= min_latitude)]

    return filtered_df


def get_filtered_df(input_df, info_df, type="coordinate"):
    start_time = time.time()
    filtered_df = pandas.DataFrame()
    if type == "coordinate":
        filtered_df = get_coordinate_filtered_df(input_df, info_df)
    elif type == "bbx":
        filtered_df = get_bbx_filtered_df(input_df, info_df)
    else:
        return input_df
    filtered_df.dropna(inplace=True)
    end_time = time.time()
    print(f"Time taken for filtering is {end_time - start_time}")
    return filtered_df


if __name__ == "__main__":
    section = 0
    weeks = 0
    if len(sys.argv) > 1:
        section = int(sys.argv[1])
        max_section = int(sys.argv[2])

    dataset_class = "weekly"
    data_path = "data/p2/analysis"
    output_data_dir = f"{data_path}/{dataset_class}"
    output_data_path = f"{output_data_dir}/intermediate_files/raw_data.csv"
    check_utils.is_safe(output_data_path)

    process_time_start = time.time()
    partition_keys = dewey_utils.get_partition_keys()
    if section != 0:
        partition_keys = list_utils.get_section(partition_keys, section, max_section)
    if weeks != 0:
        partition_keys = partition_keys[:weeks]
    useful_columns = ["poi_cbg", "longitude", "latitude", "naics_code", "distance_from_home", "median_dwell", "raw_visit_counts", "raw_visitor_counts"]
    output_df = pandas.DataFrame()
    output_list = []
    bbx_df = pandas.read_csv("data/park/code_fullnames_bbx_manual.csv")
    coordinated_df = pandas.read_csv("data/park/top24.csv")
    bbx_df.dropna(inplace=True)
    coordinated_df.dropna(inplace=True)

    info_df = coordinated_df
    info_type = "coordinate"
    log_utils.info(f"Length of info_df is {len(info_df)} and type is {info_type} at {time_utils.get_human(time.time())}")
    if not check_utils.exists(output_data_path) or True:
        for partition_key in partition_keys:
            print(f"Processing {partition_key}")
            loop_time_start = time.time()
            intermediate_df_file_path = output_data_path.replace("raw_data.csv", f"{partition_key}_raw_data.csv")
            filtered_df_path = output_data_path.replace("raw_data.csv", f"{partition_key}_filtered_data.csv")
            intermediate_df = pandas.DataFrame()
            try:
                if check_utils.exists(filtered_df_path):
                    print(f"Already exists {filtered_df_path}")
                    filtered_df = pandas.read_csv(filtered_df_path)
                    filtered_df = get_filtered_df(filtered_df, info_df, type=info_type)
                    filtered_df["partition_key"] = partition_key.split("-")[0] + "-" + partition_key.split("-")[1] + "-" + "01"
                    output_list.append(filtered_df)
                    continue

                if check_utils.exists(intermediate_df_file_path):
                    intermediate_df = pandas.read_csv(intermediate_df_file_path)
                else:
                    intermediate_df = dewey_utils.get_partition_key_df(partition_key, useful_columns, dataset_class, data_path, verbose=True)
                    # intermediate_df.to_csv(intermediate_df_file_path, index=False)

                intermediate_df = get_naics_code_filtered_df(intermediate_df, naics_code="712190")
                intermediate_df.to_csv(filtered_df_path, index=False)
                filtered_df = get_filtered_df(intermediate_df, info_df, type=info_type)
                filtered_df["partition_key"] = partition_key.split("-")[0] + "-" + partition_key.split("-")[1] + "-" + "01"
                output_list.append(filtered_df)

            except Exception as e:
                print(f"Error in data for {partition_key}")
                log_utils.error(e, file=f"logs/error_{partition_key}.log")

            loop_time_end = time.time()
            print(f"Time taken for {partition_key} is {loop_time_end - loop_time_start}")

        output_df = pandas.concat(output_list)
        output_df.to_csv(output_data_path, index=False)
    else:
        output_df = pandas.read_csv(output_data_path)
    log_utils.info(f"Length of output_df is {len(output_df)} at {time_utils.get_human(time.time())}")
    columns = ["raw_visitor_counts", "raw_visit_counts"]
    output_df.dropna(inplace=True)
    for column in columns:
        aggregated_df = get_aggregated_df(output_df, column=column, group_by_column="partition_key")
        aggregated_df.to_csv(f"{output_data_dir}/{column}.csv", index=False)

    process_time_end = time.time()
    print(f"Total time taken is {process_time_end - process_time_start}")
