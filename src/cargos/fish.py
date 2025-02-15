from cargo import Cargo

cargo = Cargo(
    id="fish",
    type_name="string(STR_CARGO_NAME_FISH)",
    unit_name="string(STR_CARGO_NAME_FISH)",
    type_abbreviation="string(STR_CID_FISH)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_EXPRESS, CC_REFRIGERATED)",
    cargo_label="FISH",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FISH)",
    penalty_lowerbound="0",
    single_penalty_length="18",
    price_factor=134,
    capacity_multiplier="1",
    icon_indices=(15, 0),
)
