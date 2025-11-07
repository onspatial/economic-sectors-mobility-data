import utils.string.fips as fips_utils


def get_division_codes(which="us"):
    division_codes = ()
    length = 0
    if which == "d1":
        division_1_states = ["CT", "ME", "MA", "NH", "RI", "VT"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_1_states)
        length = 2
    elif which == "d2":
        division_2_states = ["NJ", "NY", "PA"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_2_states)
        length = 2
    elif which == "d3":
        division_3_states = ["IL", "IN", "MI", "OH", "WI"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_3_states)
        length = 2
    elif which == "d4":
        division_4_states = ["IA", "KS", "MN", "MO", "NE", "ND", "SD"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_4_states)
        length = 2
    elif which == "d5":
        division_5_states = ["DE", "DC", "FL", "GA", "MD", "NC", "SC", "VA", "WV"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_5_states)
        length = 2
    elif which == "d6":
        division_6_states = ["AL", "KY", "MS", "TN"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_6_states)
        length = 2
    elif which == "d7":
        division_7_states = ["AR", "LA", "OK", "TX"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_7_states)
        length = 2
    elif which == "d8":
        division_8_states = ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_8_states)
        length = 2
    elif which == "d9":
        division_9_states = ["AK", "CA", "HI", "OR", "WA"]
        division_codes = tuple(fips_utils.get_state_fips_code(state) for state in division_9_states)
        length = 2
    elif which.upper() in fips_utils.get_state_fips_dict().keys():
        division_codes = tuple(fips_utils.get_state_fips_code(which))
        length = 2
    return division_codes, length


def get_filtered_df(input_df, division):
    print(f"Filtering len={len(input_df)} input_df for state codes: {division}")
    division_codes, length = get_division_codes(which=division)
    mask = input_df["poi_cbg"].astype("string").str[:length].isin(division_codes)
    # TODO: Check this
    # mask = input_df["poi_cbg"].astype("string").str.startswith(division_codes)
    input_df = input_df.loc[mask]
    return input_df
