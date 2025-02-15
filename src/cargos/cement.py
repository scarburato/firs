from cargo import Cargo

cargo = Cargo(
    id="cement",
    type_name="string(STR_CARGO_NAME_CEMENT)",
    unit_name="string(STR_CARGO_NAME_CEMENT)",
    type_abbreviation="string(STR_CID_CEMENT)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_COVERED, CC_POWDERIZED)",
    cargo_label="CMNT",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CEMENT)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    price_factor=118,
    capacity_multiplier="1",
    icon_indices=(8, 3),
)
