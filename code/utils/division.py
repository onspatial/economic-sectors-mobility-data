import re
import utils.string.fips as fips_utils


def get_division_codes(which="us"):
    division_codes = ()
    if which == "d1":
        division_1_states = ["CT", "ME", "MA", "NH", "RI", "VT"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_1_states)
    elif which == "d2":
        division_2_states = ["NJ", "NY", "PA"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_2_states)
    elif which == "d3":
        division_3_states = ["IL", "IN", "MI", "OH", "WI"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_3_states)
    elif which == "d4":
        division_4_states = ["IA", "KS", "MN", "MO", "NE", "ND", "SD"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_4_states)
    elif which == "d5":
        division_5_states = ["DE", "DC", "FL", "GA", "MD", "NC", "SC", "VA", "WV"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_5_states)
    elif which == "d6":
        division_6_states = ["AL", "KY", "MS", "TN"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_6_states)
    elif which == "d7":
        division_7_states = ["AR", "LA", "OK", "TX"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_7_states)
    elif which == "d8":
        division_8_states = ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_8_states)
    elif which == "d9":
        division_9_states = ["AK", "CA", "HI", "OR", "WA"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_9_states)
    elif which.upper() in fips_utils.get_state_fips_dict().keys():
        division_codes = tuple(fips_utils.get_state_fips_code(which))
    elif which == "GA_FULTON":
        division_codes = tuple("13121")  # Example custom codes
    elif which == "GA_DEKALB":
        division_codes = tuple("13089")  # Example custom codes
    # elif which.upper() in fips_utils.get_county_fips_dict().keys():
    #     division_codes = tuple(fips_utils.get_county_fips_code(which))
    return division_codes


def get_filtered_df(input_df, division, poi_names=None, exact_match=False):
    """Filters input_df for rows matching division codes or POI names.
    Args:
        input_df (pd.DataFrame): Input dataframe with 'poi_cbg' and 'location_name' columns.
        division (str): Division code or state code to filter by.
        poi_names (list, optional): List of POI names to filter by. Defaults to None.
        exact_match (bool, optional): Whether to use exact match for POI names. Defaults to False.
    Returns:
        pd.DataFrame: Filtered dataframe.
    """
    if poi_names is not None:
        print(f"Filtering len={len(input_df)} input_df for POI names: {poi_names}")
        if not exact_match:
            pattern = "|".join(map(re.escape, poi_names))
            mask = input_df["location_name"].str.contains(pattern, case=False, na=False)
        else:
            mask = input_df["location_name"].isin(poi_names)
        input_df = input_df.loc[mask]
        return input_df
    print(f"Filtering len={len(input_df)} input_df for state codes: {division}")
    division_codes = get_division_codes(which=division)
    mask = input_df["poi_cbg"].astype("string").str.startswith(division_codes)
    input_df = input_df.loc[mask]
    return input_df
