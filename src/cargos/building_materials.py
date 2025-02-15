from cargo import Cargo

cargo = Cargo(
    id="building_materials",
    type_name="string(STR_CARGO_NAME_BUILDING_MATERIALS)",
    unit_name="string(STR_CARGO_NAME_BUILDING_MATERIALS)",
    type_abbreviation="string(STR_CID_BUILDING_MATERIALS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS, CC_BULK)",
    cargo_label="BDMT",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_BUILDING_MATERIALS)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    price_factor=133,
    capacity_multiplier="1",
    icon_indices=(1, 1),
)
