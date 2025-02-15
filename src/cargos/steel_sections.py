from cargo import Cargo

cargo = Cargo(
    id="steel_sections",
    type_name="string(STR_CARGO_NAME_STEEL_SECTIONS)",
    unit_name="string(STR_CARGO_NAME_STEEL_SECTIONS)",
    type_abbreviation="string(STR_CID_STEEL_SECTIONS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="STSE",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_SECTIONS)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=142,
    icon_indices=(7, 5),
)
