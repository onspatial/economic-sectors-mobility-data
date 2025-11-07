import utils.string.fips as fips_utils


def get_division_code(which="us"):
    division = ()
    length = 0
    if which == "d1":
        d1_states = ["CT", "ME", "MA", "NH", "RI", "VT"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d1_states)
        length = 2
    elif which == "d2":
        d2_states = ["NJ", "NY", "PA"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d2_states)
        length = 2
    elif which == "d3":
        d3_states = ["IL", "IN", "MI", "OH", "WI"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d3_states)
        length = 2
    elif which == "d4":
        d4_states = ["IA", "KS", "MN", "MO", "NE", "ND", "SD"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d4_states)
        length = 2
    elif which == "d5":
        d5_states = ["DE", "DC", "FL", "GA", "MD", "NC", "SC", "VA", "WV"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d5_states)
        length = 2
    elif which == "d6":
        d6_states = ["AL", "KY", "MS", "TN"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d6_states)
        length = 2
    elif which == "d7":
        d7_states = ["AR", "LA", "OK", "TX"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d7_states)
        length = 2
    elif which == "d8":
        d8_states = ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d8_states)
        length = 2
    elif which == "d9":
        d9_states = ["AK", "CA", "HI", "OR", "WA"]
        division = tuple(fips_utils.get_state_fips_code(state) for state in d9_states)
        length = 2
    elif which.upper() in fips_utils.get_state_fips_dict().keys():
        division = tuple(fips_utils.get_state_fips_code(which))
        length = 2
    return division, length


def get_filtered_df(input_df, division):
    print(f"Filtering len={len(input_df)} input_df for state codes: {division}")
    division_code, length = get_division_code(which=division)
    mask = input_df["poi_cbg"].astype("string").str[:length].isin(division_code)
    input_df = input_df.loc[mask]
    return input_df
