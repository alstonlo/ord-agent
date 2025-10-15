from __future__ import annotations

__all__ = (
    "Amount",
    "Compound",
    "CompoundIdentifier",
    "CompoundIdentifierType",
    "CompoundPreparation",
    "CompoundPreparationType",
    "CompoundSource",
    "CrudeComponent",
    "IlluminationConditions",
    "IlluminationType",
    "Length",
    "LengthUnit",
    "Mass",
    "MassMassUnit",
    "Moles",
    "MolesUnit",
    "Percentage",
    "Pressure",
    "PressureConditions",
    "PressureConditionsAtmosphere",
    "AtmosphereType",
    "PressureConditionsPressureControl",
    "PressureControlType",
    "PressureConditionsPressureMeasurement",
    "PressureMeasurementType",
    "PressureUnit",
    "ProductCompound",
    "Reaction",
    "ReactionConditions",
    "ReactionInput",
    "ReactionInputAdditionDevice",
    "AdditionDeviceType",
    "ReactionInputAdditionSpeed",
    "AdditionSpeedType",
    "ReactionNotes",
    "ReactionOutcome",
    "ReactionRoleType",
    "ReactionSetup",
    "ReactionSetupReactionEnvironment",
    "ReactionEnvironmentType",
    "ReactionWorkup",
    "ReactionWorkupType",
    "StirringConditions",
    "StirringMethodType",
    "StirringConditionsStirringRate",
    "StirringRateType",
    "Temperature",
    "TemperatureConditions",
    "TemperatureConditionsTemperatureControl",
    "TemperatureControlType",
    "TemperatureConditionsTemperatureMeasurement",
    "TemperatureMeasurementType",
    "TemperatureUnit",
    "Texture",
    "TextureType",
    "Time",
    "TimeUnit",
    "UnmeasuredAmount",
    "UnmeasuredAmountType",
    "Vessel",
    "VesselAttachment",
    "VesselAttachmentType",
    "VesselMaterial",
    "VesselMaterialType",
    "VesselPreparation",
    "VesselPreparationType",
    "VesselType",
    "Volume",
    "VolumeUnit",
    "Wavelength",
    "WavelengthUnit",
)

import enum
from dataclasses import dataclass


class CompoundIdentifierType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    SMILES = 2
    """
    Simplified molecular-input line-entry system.
    """

    INCHI = 3
    """
    IUPAC International Chemical Identifier.
    """

    MOLBLOCK = 4
    """
    Molblock from a MDL Molfile V3000.
    """

    IUPAC_NAME = 5
    """
    Chemical name following IUPAC nomenclature recommendations.
    """

    NAME = 6
    """
    Any accepted common name, trade name, etc.
    """

    CAS_NUMBER = 7
    """
    Chemical Abstracts Service Registry Number (with hyphens).
    """

    PUBCHEM_CID = 8
    """
    PubChem Compound ID number.
    """

    CHEMSPIDER_ID = 9
    """
    ChemSpider ID number.
    """

    CXSMILES = 10
    """
    ChemAxon extended SMILES
    """

    INCHI_KEY = 11
    """
    IUPAC International Chemical Identifier key
    """

    XYZ = 12
    """
    XYZ molecule file
    """

    UNIPROT_ID = 13
    """
    UniProt ID (for enzymes)
    """

    PDB_ID = 14
    """
    Protein data bank ID (for enzymes)
    """

    AMINO_ACID_SEQUENCE = 15
    """
    Amino acid sequence (for enzymes).
    """

    HELM = 16
    """
    HELM; https://www.pistoiaalliance.org/helm-notation/.
    """

    MDL = 17
    """
    MDL number e.g., MFCD00005972 for morpholine,
    often included on commercial supplier listings.
    """


class CompoundPreparationType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    NONE = 2
    """
    Compound used as received.
    """

    REPURIFIED = 3
    """
    Compound repurified (e.g., recrystallized).
    """

    SPARGED = 4
    """
    Compound sparged, most likely to be the case with solvents.
    """

    DRIED = 5
    """
    Moisture removed, e.g., using molecular sieves.
    """

    SYNTHESIZED = 6
    """
    Compound synthesized in-house.
    """


class IlluminationType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    AMBIENT = 2

    DARK = 3

    LED = 4

    HALOGEN_LAMP = 5

    DEUTERIUM_LAMP = 6

    SOLAR_SIMULATOR = 7

    BROAD_SPECTRUM = 8


class LengthUnit(enum.Enum):
    UNSPECIFIED = 0

    CENTIMETER = 1

    MILLIMETER = 2

    METER = 3

    INCH = 4

    FOOT = 5


class MassMassUnit(enum.Enum):
    UNSPECIFIED = 0

    KILOGRAM = 1

    GRAM = 2

    MILLIGRAM = 3

    MICROGRAM = 4


class MolesUnit(enum.Enum):
    UNSPECIFIED = 0

    MOLE = 1

    MILLIMOLE = 2

    MICROMOLE = 3

    NANOMOLE = 4


class PressureUnit(enum.Enum):
    UNSPECIFIED = 0

    BAR = 1

    ATMOSPHERE = 2

    PSI = 3

    KPSI = 4

    PASCAL = 5

    KILOPASCAL = 6

    TORR = 7

    MM_HG = 8


class AtmosphereType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    AIR = 2

    NITROGEN = 3

    ARGON = 4

    OXYGEN = 5

    HYDROGEN = 6

    CARBON_MONOXIDE = 7

    CARBON_DIOXIDE = 8

    METHANE = 9

    AMMONIA = 10

    OZONE = 11

    ETHYLENE = 12

    ACETYLENE = 13


class PressureControlType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    AMBIENT = 2

    SLIGHT_POSITIVE = 3
    """
    E.g., 1-5 psi with a gas line inlet.
    """

    SEALED = 4
    """
    Fully sealed vessel (e.g., microwave vial, sealed tube).
    """

    PRESSURIZED = 5
    """
    High-pressure applied, e.g., in a bomb reactor.
    """


class PressureMeasurementType(enum.Enum):
    """
    TODO(ccoley) get input on how to expand this enum, among others
    """

    UNSPECIFIED = 0

    CUSTOM = 1

    PRESSURE_TRANSDUCER = 2


class AdditionDeviceType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    NONE = 2

    SYRINGE = 3

    CANNULA = 4

    ADDITION_FUNNEL = 5

    PIPETTE = 6

    POSITIVE_DISPLACEMENT_PIPETTE = 7

    PISTON_PUMP = 8

    SYRINGE_PUMP = 9

    PERISTALTIC_PUMP = 10


class AdditionSpeedType(enum.Enum):
    UNSPECIFIED = 0
    """
    Unspecified.
    """

    ALL_AT_ONCE = 1

    FAST = 2

    SLOW = 3

    DROPWISE = 4

    CONTINUOUS = 5

    PORTIONWISE = 6


class ReactionRoleType(enum.Enum):
    UNSPECIFIED = 0

    REACTANT = 1
    """
    A reactant is any compound that contributes atoms to a desired or
    observed product.
    """

    REAGENT = 2

    SOLVENT = 3

    CATALYST = 4

    WORKUP = 5
    """
    The workup role is used when defining quenches, buffer additives for
    liquid-liquid separations, etc.
    """

    INTERNAL_STANDARD = 6
    """
    Internal standards can be included as part of a reaction input (when
    added prior to the start of the reaction) or as part of a workup
    step of addition.
    """

    AUTHENTIC_STANDARD = 7

    PRODUCT = 8
    """
    A product can be any species produced by the reaction, whether desired
    or undesired.
    """

    BYPRODUCT = 9
    """
    When there is one intended chemical equation:
    - Set `is_desired_product=True` to indicate a desired product.
    - Use BYPRODUCT to indicate a chemical species that is an expected result
    of the reaction but is not the product of interest.
    - Use SIDE_PRODUCT to indicate the product of a side reaction.
    - See https://doi.org/10.1021/op300317g for a discussion of these terms.
    """

    SIDE_PRODUCT = 10


class ReactionEnvironmentType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    FUME_HOOD = 2

    BENCH_TOP = 3

    GLOVE_BOX = 4

    GLOVE_BAG = 5


class ReactionWorkupType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    ADDITION = 2
    """
    Addition (quench, dilution, extraction solvent, internal standard, etc.)
    Specify composition/amount in "input".
    Often preceded by TEMPERATURE.
    """

    ALIQUOT = 3
    """
    Sampling (by mass of volume) a portion of the mixture, often for
    dilution in a subsequent ADDITION step prior to analysis. The vessel to
    which the aliquot is transferred can be specified in "details".
    """

    TEMPERATURE = 4
    """
    Change of temperature.
    Specify conditions in "temperature".
    """

    CONCENTRATION = 5
    """
    Concentration step, often using a rotovap.
    Specify degree in "details" if appropriate, e.g., "to half volume".
    """

    EXTRACTION = 6
    """
    Liquid extractions are often preceded by Additions. If there
    are multiple distinct additions prior to an extraction, it is
    assumed that the kept phases are pooled.
    Specify which phase to keep in "keep_phase".
    """

    FILTRATION = 7
    """
    Filtration (can keep solid or filtrate).
    Specify which phase to keep in "keep phase".
    """

    WASH = 8
    """
    Washing a solid or liquid, keeping the original phase.
    Specify "input" of rinse. Rinses performed in
    multiple stages should be given multiple workup steps
    """

    DRY_IN_VACUUM = 9
    """
    Dried under vacuum.
    Specify temperature in "temperature".
    """

    DRY_WITH_MATERIAL = 10
    """
    Dried with chemical additive.
    Specify chemical additive in "input".
    """

    FLASH_CHROMATOGRAPHY = 11
    """
    Purification by flash chromatography.
    Specify stationary and mobile phases (and gradients) in "details".
    Specify automation in "is_automated".
    """

    OTHER_CHROMATOGRAPHY = 12
    """
    Purification by other prep chromatography (e.g. prep TLC, prep HPLC).
    Specify method, stationary and mobile phases in "details".
    Specify automation in "is_automated".
    """

    SCAVENGING = 13
    """
    Scavenging step (e.g., pass through silica/alumina pad)
    Specify any material additives in "input".
    """

    WAIT = 14
    """
    Waiting step. Specify "duration".
    """

    STIRRING = 15
    """
    Mixing step. Specify "stirring"
    """

    PH_ADJUST = 16
    """
    pH adjustments should specify "input" to define
    species used as well as "ph" for target ph
    """

    DISSOLUTION = 17
    """
    Redissolution considered to be a special form of addition.
    Specify "input"
    """

    DISTILLATION = 18
    """
    Specify temperature in "temperature".
    Specify pressure and apparatus notes in "details".
    """


class StirringMethodType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    NONE = 2

    STIR_BAR = 3

    OVERHEAD_MIXER = 4

    AGITATION = 5

    BALL_MILLING = 6

    SONICATION = 7


class StirringRateType(enum.Enum):
    UNSPECIFIED = 0

    HIGH = 1

    MEDIUM = 2

    LOW = 3


class TemperatureUnit(enum.Enum):
    UNSPECIFIED = 0

    CELSIUS = 1

    FAHRENHEIT = 2

    KELVIN = 3


class TemperatureControlType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    AMBIENT = 2

    OIL_BATH = 3

    WATER_BATH = 4

    SAND_BATH = 5

    ICE_BATH = 6

    DRY_ALUMINUM_PLATE = 7

    MICROWAVE = 8

    DRY_ICE_BATH = 9

    AIR_FAN = 10

    LIQUID_NITROGEN = 11


class TemperatureMeasurementType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    THERMOCOUPLE_INTERNAL = 2
    """
    Physically in reaction solution.
    """

    THERMOCOUPLE_EXTERNAL = 3
    """
    On outside of vessel or, e.g., in oil bath.
    """

    INFRARED = 4
    """
    Contactless infrared probe.
    """


class TextureType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    POWDER = 2

    CRYSTAL = 3

    OIL = 4

    AMORPHOUS_SOLID = 5

    FOAM = 6

    WAX = 7

    SEMI_SOLID = 8

    SOLID = 9

    LIQUID = 10

    GAS = 11


class TimeUnit(enum.Enum):
    UNSPECIFIED = 0

    DAY = 4

    HOUR = 1

    MINUTE = 2

    SECOND = 3


class UnmeasuredAmountType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    SATURATED = 2
    """
    Solute species present at saturation limit. Should only be used for
    compounds when a solvent compound is also present in he same input.
    """

    CATALYTIC = 3
    """
    An unmeasured drop or scoop of compound intended to introduce it only
    at a catalytic (very low) concentration.
    """

    TITRATED = 4
    """
    Compound was titrated in, but the actual amount added was not recorded.
    Details of how the amount of compound added was decided, e.g., a change
    in color, should be included in the details field.
    """


class VesselType(enum.Enum):
    """
    Vessel type (flask, vial, well-plate, etc.).
    """

    UNSPECIFIED = 0

    CUSTOM = 1

    ROUND_BOTTOM_FLASK = 2

    VIAL = 3

    WELL_PLATE = 4

    MICROWAVE_VIAL = 5

    TUBE = 6

    CONTINUOUS_STIRRED_TANK_REACTOR = 7

    PACKED_BED_REACTOR = 8

    NMR_TUBE = 9

    PRESSURE_FLASK = 10
    """
    E.g., sealed tube
    """

    PRESSURE_REACTOR = 11
    """
    High-pressure (e.g., Parr bomb reactor)
    """

    ELECTROCHEMICAL_CELL = 12


class VesselAttachmentType(enum.Enum):
    UNSPECIFIED = 0

    NONE = 1

    CUSTOM = 2

    SEPTUM = 3

    CAP = 4

    MAT = 5
    """
    e.g. a covering for a well plate.
    """

    REFLUX_CONDENSER = 6

    VENT_NEEDLE = 7

    DEAN_STARK = 8

    VACUUM_TUBE = 9

    ADDITION_FUNNEL = 10

    DRYING_TUBE = 11

    ALUMINUM_FOIL = 12

    THERMOCOUPLE = 13

    BALLOON = 14

    GAS_ADAPTER = 15
    """
    E.g. a ground-glass adapter with a gas line.
    """

    PRESSURE_REGULATOR = 16

    RELEASE_VALVE = 17


class VesselMaterialType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    GLASS = 2

    POLYPROPYLENE = 3

    PLASTIC = 4

    METAL = 5

    QUARTZ = 6


class VesselPreparationType(enum.Enum):
    UNSPECIFIED = 0

    CUSTOM = 1

    NONE = 2

    OVEN_DRIED = 3

    FLAME_DRIED = 4

    EVACUATED_BACKFILLED = 5

    PURGED = 6


class VolumeUnit(enum.Enum):
    UNSPECIFIED = 0

    LITER = 1

    MILLILITER = 2

    MICROLITER = 3

    NANOLITER = 4


class WavelengthUnit(enum.Enum):
    UNSPECIFIED = 0

    NANOMETER = 1

    WAVENUMBER = 2
    """
    cm^{-1}
    """


@dataclass
class Amount:
    """
    *
    The quantitative amount of a Compound used in a particular reaction.
    Compounds added in their pure form should have their value defined by
    mass, moles, or volume. Compounds prepared as solutions should be defined
    in terms of their volume. Compounds prepared on solid supports should
    define the total mass/volume including the support.

    Oneofs:
        - kind:
    """

    mass: Mass | None

    moles: Moles | None

    volume: Volume | None

    unmeasured: UnmeasuredAmount | None

    volume_includes_solutes: bool | None
    """
    Whether the volume measurement refers to the pure substance or to the
    total volume of the reaction input. An example of when this field should
    be TRUE is when stock solutions are prepared by adding solvent to a
    volumetric flask already containing solute(s).
    """


@dataclass
class Compound:
    """
    *
    A Compound defines both the identity of a pure species and a quantitative
    amount (mass, moles, volume). For compounds used in inputs, details can
    be provided about how it was prepared and from where it was purchased.
    """

    identifiers: list[CompoundIdentifier]
    """
    Set of identifiers used to uniquely define this compound.
    Solutions or mixed compounds should use the NAME identifier
    and list all constituent compounds in the "components" field.
    """

    amount: Amount | None

    reaction_role: ReactionRoleType

    is_limiting: bool | None
    """
    Whether this species is intended to be a limiting reactant.
    """

    preparations: list[CompoundPreparation]

    source: CompoundSource | None

    texture: Texture | None


@dataclass
class CompoundSource:
    vendor: str
    """
    Name of the vendor or supplier the compound was purchased from.
    """

    catalog_id: str
    """
    Compound ID in the vendor database or catalog.
    """

    lot: str
    """
    Batch/lot identification.
    """


@dataclass
class CompoundIdentifier:
    """
    *
    Compound identifiers uniquely define a single (pure) chemical species.
    While we encourage the use of SMILES strings, these do not work well in
    all cases (e.g., handling tautomerism, axial chirality). Multiple
    identifiers may be specified for a single compound to avoid ambiguity.
    We discourage chemicals from being defined only by a name. For compounds
    that are prepared or isolated as salts, the identifier should include
    specification of which salt.
    """

    type: CompoundIdentifierType

    details: str

    value: str
    """
    Value of the compound identifier; certain types (e.g., PUBCHEM_CID) may
    cast the string as an integer for downstream processing and validation.
    """


@dataclass
class CompoundPreparation:
    """
    *
    Compounds may undergo additional preparation before being used in a
    reaction after being received from a supplier or vendor. We encourage
    the use of the 'preparation' enum when possible, even if the description
    is an oversimplification of the full procedure, which can be described
    in the 'details' field.
    """

    type: CompoundPreparationType

    details: str
    """
    Full description of how the received compound was prepared.
    """

    reaction_id: str
    """
    The ID of the reaction that produced this species. Note that this ID must
    be defined within the same Dataset; cross-references cannot exist between
    multiple datasets. Only to be used with the SYNTHESIZED preparation type.
    The referenced reaction should not merely be the procedure that was
    followed/reproduced, but the *exact* physical experiment.
    """


@dataclass
class CrudeComponent:
    """
    *
    Crude components are used in multi-step or multi-stage reactions (no strong
    distinction is made here) where one synthetic process must be described by
    multiple "Reaction" messages. In these cases, we often carry the crude
    product from one step/stage into the next. This message is only to be used
    when there is not complete isolation of an intermediate molecule; if there
    is complete isolation, then a regular Compound should be used with the
    SYNTHESIED preparation type.
    """

    reaction_id: str
    """
    The ID of the reaction that produced the crude. Note that this ID must be
    defined within the same Dataset; cross-references cannot exist between
    multiple datasets.
    """

    includes_workup: bool | None
    """
    Whether that reaction's workup and purification steps were performed
    prior to addition.
    """

    has_derived_amount: bool | None
    """
    Whether the amount added in this reaction should be inferred from the
    previous step, i.e, if everything was added.
    """

    amount: Amount | None
    """
    If the entire crude mixture was not used, need to specify an amount.
    """

    texture: Texture | None


@dataclass
class Data:
    """
    Data is a container for arbitrary data.

    Oneofs:
        - kind:
    """

    float_value: float | None

    integer_value: int | None

    bytes_value: bytes | None

    string_value: str | None

    url: str | None
    """
    URL for data stored elsewhere.
    """

    description: str
    """
    Description of these data (but avoid redundancy with map keys).
    """

    format: str
    """
    Description of the file format (if applicable); usually the file extension.
    For example, 'png' or 'tiff' for images. If empty, we assume string data.
    """


@dataclass
class IlluminationConditions:
    type: IlluminationType

    details: str
    """
    E.g. manufacturer, setup specifications, etc.
    """

    peak_wavelength: Wavelength | None

    color: str

    distance_to_vessel: Length | None


@dataclass
class Length:
    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: LengthUnit


@dataclass
class Mass:
    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: MassMassUnit


@dataclass
class Moles:
    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: MolesUnit


@dataclass
class Percentage:
    """
    Used for things like conversion and yield.
    """

    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """


@dataclass
class Pressure:
    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: PressureUnit


@dataclass
class PressureConditions:

    control: PressureConditionsPressureControl | None

    setpoint: Pressure | None

    atmosphere: PressureConditionsAtmosphere | None

    measurements: list[PressureConditionsPressureMeasurement]


@dataclass
class PressureConditionsAtmosphere:
    type: AtmosphereType

    details: str


@dataclass
class PressureConditionsPressureControl:
    type: PressureControlType

    details: str
    """
    Include means of pressure control in "Attachment" when appropriate.
    """


@dataclass
class PressureConditionsPressureMeasurement:
    type: PressureMeasurementType

    details: str

    time: Time | None

    pressure: Pressure | None


@dataclass
class ProductCompound:
    identifiers: list[CompoundIdentifier]
    """
    The identity of the product compound.
    """

    is_desired_product: bool | None

    isolated_color: str

    texture: Texture | None

    reaction_role: ReactionRoleType
    """
    Specify the role the ProductCompound played in the reaction. This
    aids in constructing proper reaction SMILES and product lists.
    Species produced by the reaction should be identified as PRODUCT,
    whether desired or undesired. Recovered starting materials can be
    specified as REACTANT, REAGENT, CATALYST, etc. as appropriate.
    """


@dataclass
class Reaction:
    """
    *
    Throughout this schema, we introduce enums to encourage consistency in
    nomenclature and to avoid unnecessary downstream data processing that would
    otherwise be required to consolidate equivalent entries. However, we do
    not wish to restrict what users are able to specify if their synthesis
    does not fit cleanly into a pre-existing enum field. For that reason, many
    enums contain a CUSTOM field, which must be accompanied by setting the
    'details' field, where appropriate).

    NOTE(kearnes): In many places, we deliberately violate the style guide for
    enums by nesting instead of prefixing; this is not done lightly. The primary
    consideration is API consistency and the ability to use unqualified strings
    as enum values. For instance, we want 'CUSTOM' to be a valid value for all
    enums that support custom types.
    """

    inputs: dict[str, ReactionInput]
    """
    List of pure substances or mixtures that were added to the reaction vessel.
    This is a map instead of a repeated field to simplify reaction templating
    through the use of keys. String keys are simple descriptions and are
    present only for convenience.
    """

    setup: ReactionSetup | None
    """
    The reaction setup specifies how the reaction was prepared, e.g., whether
    it was automated, whether it was run in a glove box.
    """

    conditions: ReactionConditions | None
    """
    Reaction conditions predominantly include temperature, stirring, and
    pressure conditions, but also allow specification of flow, photochemistry,
    and electrochemistry conditions.
    """

    notes: ReactionNotes | None
    """
    Reaction notes largely pertain to safety considerations.
    """

    workups: list[ReactionWorkup]
    """
    Workup steps are listed in the order they are performed.
    """

    outcomes: list[ReactionOutcome]
    """
    Each reaction outcome contains all analyses and confirmed/expected product
    structures at a particular reaction time.
    """

    reaction_id: str
    """
    Official ID for this reaction in the Open Reaction Database.
    """


@dataclass
class ReactionConditions:

    temperature: TemperatureConditions | None

    pressure: PressureConditions | None

    stirring: StirringConditions | None

    illumination: IlluminationConditions | None

    reflux: bool | None

    ph: float | None

    conditions_are_dynamic: bool | None
    """
    Boolean to describe whether the conditions cannot be
    represented by the static, single-step schema.
    """

    details: str
    """
    A catch-all string field for providing more information about
    the conditions (e.g., multiple stages)
    """


@dataclass
class ReactionInput:
    """
    *
    A reaction input is any pure substance, mixture, or solution that is
    added to the reaction vessel.

    For example, suppose we are adding 3 mL of a 4 M solution of NaOH in water.
    We would define one component for the solvent and one component for the
    solute with the correct respective amounts.

    input {
      components: {
        identifiers: {type: IDENTIFIER_SMILES, value: O}
        identifiers: {type: IDENTIFIER_NAME, value: water}
        volume: {value: 3, units: MILLILITER}
        volume_includes_solutes: true
      }
      components: {
        identifiers: {type: IDENTIFIER_SMILES, value: [Na+].[OH-]}
        identifiers: {type: IDENTIFIER_NAME, value: sodium hydroxide}
        moles: {value: 12, units: MILLIMOLES}
      }
    }
    """

    components: list[Compound]
    """
    A component is any pure species that is added to the reaction, whether as
    a pure substance or in a mixture/solution.
    """

    crude_components: list[CrudeComponent]
    """
    A crude component refers to a non-purified, non-isolated compound or
    mixture that is produced by a preceding reaction step.
    """

    addition_order: int
    """
    The addition order is 1-indexed. Inputs with the same addition_order are
    assumed to be added simultaneously. One input with a lower addition_order
    than another was added earlier in the procedure.
    """

    addition_time: Time | None
    """
    When the addition event took place in terms of the reaction time (or,
    in the case of flow chemistry, the residence time).
    """

    addition_speed: ReactionInputAdditionSpeed | None
    """
    The qualitative rate of addition.
    """

    addition_duration: Time | None
    """
    Quantitatively, how long addition took
    """

    addition_device: ReactionInputAdditionDevice | None
    """
    The device used for addition.
    """

    addition_temperature: Temperature | None
    """
    Specify the temperature of the material being added.
    E.g., a cooled flask of a stock solution to be added at low temperature.
    """

    texture: Texture | None
    """
    The texture immediately before addition.
    """


@dataclass
class ReactionInputAdditionDevice:
    type: AdditionDeviceType

    details: str
    """
    Specify, e.g., "gas-tight" for SYRINGE or cannula material.
    """


@dataclass
class ReactionInputAdditionSpeed:
    type: AdditionSpeedType

    details: str
    """
    Specify, e.g., portion sizes and intervals for PORTIONWISE.
    """


@dataclass
class ReactionNotes:
    is_heterogeneous: bool | None
    """
    Equivalent to "not single phase".
    """

    forms_precipitate: bool | None
    """
    Qualitative precipitation. Could be desired or by-product.
    """

    is_exothermic: bool | None
    """
    Qualitative exothermicity (primarily for safety).
    """

    offgasses: bool | None
    """
    Qualitative offgassing (primarily for safety).
    """

    is_sensitive_to_moisture: bool | None

    is_sensitive_to_oxygen: bool | None

    is_sensitive_to_light: bool | None

    safety_notes: str
    """
    Include additional sensitivity issues, e.g., shock or heat.
    Include toxicity and other safety warnings.
    """

    procedure_details: str
    """
    Overflow field for full procedure details
    """


@dataclass
class ReactionOutcome:
    """
    *
    The outcomes of a reaction describe the conversion, yield, and/or other
    analyses of the resulting product mixture after workup step(s). Each
    outcome is associated with a reaction/residence time. To allow for
    one Reaction message to contain the results of a full kinetic profiling
    experiment, this is a repeated field of the Reaction message.

    It is the parent message for product characterization and any analytical
    data.
    """

    reaction_time: Time | None
    """
    Reaction time (for flow, equivalent to residence time or spacetime).
    """

    conversion: Percentage | None
    """
    Conversion with respect to the sole limiting reactant. If there is
    ambiguity in which species the conversion is defined with respect to, the
    quantification of leftover starting materials should be defined as the
    quantification of multiple products, where the compound identity of those
    products matches the starting materials.
    """

    products: list[ProductCompound]
    """
    The products observed in this reaction, including product-specific data
    defined in submessages. If the quantities of leftover starting materials
    are measured, these starting materials may also be defined as product
    species.
    """


@dataclass
class ReactionSetup:
    vessel: Vessel | None

    is_automated: bool | None
    """
    Specification of automated protocols.
    """

    automation_platform: str
    """
    Automated platform name, brand, or model number.
    """

    automation_code: dict[str, Data]
    """
    Raw automation code or synthetic recipe definition.
    """

    environment: ReactionSetupReactionEnvironment | None
    """
    Specify reaction environment.
    """


@dataclass
class ReactionSetupReactionEnvironment:
    type: ReactionEnvironmentType

    details: str
    """
    Specify environment details, e.g., "nitrogen-filled" for GLOVE_BOX.
    """


@dataclass
class ReactionWorkup:
    type: ReactionWorkupType

    details: str
    """
    Include step-specific details such as purpose of an addition, e.g.,
    "crystallization". Include method details, e.g., "layer diffusion".
    """

    duration: Time | None

    input: ReactionInput | None

    amount: Amount | None
    """
    When aliquotting a portion of the reaction mixture, the amount is
    specified by mass or volume. Note that the amounts for additions should
    be described in the "input" field instead; these are only for aliquots.
    """

    temperature: TemperatureConditions | None

    keep_phase: str

    stirring: StirringConditions | None

    target_ph: float | None

    is_automated: bool | None
    """
    Indicate automated workup/purification. Include specifications in
    "details", e.g., instrument manufacturer, solvent gradient
    (if applicable), column material and size, etc.
    """


@dataclass
class StirringConditions:
    type: StirringMethodType

    details: str
    """
    Specify, e.g., "egg-shape" for STIR_BAR.
    """

    rate: StirringConditionsStirringRate | None


@dataclass
class StirringConditionsStirringRate:
    type: StirringRateType

    details: str
    """
    Specify, e.g., "vigorous" for HIGH, or specify exact rpm in "rpm".
    """

    rpm: int


@dataclass
class Temperature:
    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: TemperatureUnit


@dataclass
class TemperatureConditions:
    control: TemperatureConditionsTemperatureControl | None

    setpoint: Temperature | None

    measurements: list[TemperatureConditionsTemperatureMeasurement]


@dataclass
class TemperatureConditionsTemperatureControl:
    type: TemperatureControlType

    details: str
    """
    Specify, e.g., ICE_BATH components (e.g., "ice water, salt"),
    MICROWAVE power, AIR_FAN speed, etc.
    """


@dataclass
class TemperatureConditionsTemperatureMeasurement:
    type: TemperatureMeasurementType

    details: str

    time: Time | None

    temperature: Temperature | None


@dataclass
class Texture:
    """
    *
    This qualitatively describes the apparent size and morphology of a Compound,
    a ProductCompound, or a ReactionInput.
    """

    type: TextureType

    details: str
    """
    Specify texture forms such as "fine needles" for CRYSTAL,
    "viscous" for OIL, etc.
    """


@dataclass
class Time:
    """
    *
    To allow users to describe synthetic processes in whatever units they find
    most natural, we define a fixed list of allowable units for each measurement
    type. Upon submission to a centralized database, or using a validation and
    canonicalization script, we will convert all values to the default units
    (the first nonzero item in each enum).

    Each message also contains a `precision` field, which specifies the precision
    of the measurement in the same units as the measurement itself. Often the
    precision will be the standard deviation from an instrument calibration.
    """

    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: TimeUnit


@dataclass
class UnmeasuredAmount:
    """
    *
    Compounds may be defined with qualitative amounts in situations where a
    precise quantity is not measured or reported.
    """

    type: UnmeasuredAmountType

    details: str
    """
    Full description of the unmeasured amount if more details are known.
    """


@dataclass
class Vessel:
    """
    *
    The Vessel defines the primary container within which the reaction was
    performed, including the type of vessel, its primary material, any
    preparation steps or vessel attachments, and its volume.
    """

    type: VesselType

    details: str
    """
    Include details such as "multi-neck" for ROUND_BOTTOM_FLASK,
    "J. Young" for NMR_TUBE, etc.
    """

    material: VesselMaterial | None
    """
    Vessel material (glass, plastic, etc.).
    """

    preparations: list[VesselPreparation]
    """
    How the vessel was prepared for the reaction.
    """

    attachments: list[VesselAttachment]
    """
    Vessel attachments (septum, cap, gas adapter, etc.).
    """

    volume: Volume | None
    """
    Size (volume) of the vessel.
    """

    vessel_id: str
    """
    Identifier number for a microtiter plate or parallel reactor run.
    """

    position: str
    """
    If a well-plate was used, the position of the well for this experiment,
    e.g., "A4".
    """

    row: str

    col: str


@dataclass
class VesselAttachment:
    type: VesselAttachmentType

    details: str
    """
    Include attachment specifications, e.g., "rubber" for SEPTUM,
    "Teflon" for CAP, "water jacket" for REFLUX_CONDENSER, etc.
    Also include sealing details, e.g., "electrical tape", "parafilm", etc.
    """


@dataclass
class VesselMaterial:
    type: VesselMaterialType

    details: str


@dataclass
class VesselPreparation:
    type: VesselPreparationType

    details: str


@dataclass
class Volume:

    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: VolumeUnit


@dataclass
class Wavelength:

    value: float | None

    precision: float | None
    """
    Precision of the measurement (with the same units as `value`).
    """

    units: WavelengthUnit
