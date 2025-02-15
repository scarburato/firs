from cargo import Cargo

cargo = Cargo(
    id="limestone",
    type_name="string(STR_CARGO_NAME_LIMESTONE)",
    unit_name="string(STR_CARGO_NAME_LIMESTONE)",
    type_abbreviation="string(STR_CID_LIMESTONE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK)",
    cargo_label="LIME",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_LIMESTONE)",
    penalty_lowerbound="38",
    single_penalty_length="255",
    price_factor=92,
    capacity_multiplier="1",
    icon_indices=(0, 4),
)
