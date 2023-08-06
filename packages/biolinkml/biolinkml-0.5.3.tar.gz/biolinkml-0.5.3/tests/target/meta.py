# Auto generated from meta.yaml by pythongen.py version: 0.2.0
# Generation date: 2019-02-05 16:34
# Schema: metamodel
#
# id: http://w3id.org/biolink/biolinkml/meta
# description: A metamodel for defining biolink related schemas
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, NCName, URIorCURIE, XSDDate
from includes.types import Boolean, Datetime, Integer, Ncname, String, Uri

metamodel_version = "1.0.1"

inherited_slots: List[str] = ["domain", "range", "multivalued", "inherited", "readonly", "ifabsent", "required",
                              "inlined", "key", "identifier"]


# Types

# Class references
class ElementName(str):
    pass


class SchemaDefinitionName(ElementName):
    pass


class TypeDefinitionName(ElementName):
    pass


class SubsetDefinitionName(ElementName):
    pass


class DefinitionName(ElementName):
    pass


class SlotDefinitionName(DefinitionName):
    pass


class ClassDefinitionName(DefinitionName):
    pass


class PrefixLocalName(NCName):
    pass


@dataclass
class Element(YAMLRoot):
    """
    a named element in the model
    """

    # === element ===
    name: Union[str, ElementName]
    description: Optional[str] = None
    aliases: List[str] = empty_list()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated: Optional[str] = None
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, SchemaDefinitionName]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.name, ElementName):
            self.name = ElementName(self.name)
        self.mappings = [v if isinstance(v, URIorCURIE)
                         else URIorCURIE(v) for v in self.mappings]
        self.examples = [v if isinstance(v, Example)
                         else Example(**v) for v in self.examples]
        self.in_subset = [v if isinstance(v, SubsetDefinitionName)
                          else SubsetDefinitionName(v) for v in self.in_subset]
        if self.from_schema and not isinstance(self.from_schema, SchemaDefinitionName):
            self.from_schema = SchemaDefinitionName(self.from_schema)
        self.see_also = [v if isinstance(v, URIorCURIE)
                         else URIorCURIE(v) for v in self.see_also]
        self.id_prefixes = [v if isinstance(v, NCName)
                            else NCName(v) for v in self.id_prefixes]


@dataclass
class SchemaDefinition(Element):
    """
    a collection of subset, type, slot and class definitions
    """

    # === element ===
    name: Union[str, SchemaDefinitionName]
    aliases: List[str] = empty_list()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated: Optional[str] = None
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, SchemaDefinitionName]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()

    # === schema definition ===
    id: Union[str, URIorCURIE] = None
    description: Optional[str] = None
    title: Optional[str] = None
    version: Optional[str] = None
    imports: List[Union[str, URIorCURIE]] = empty_list()
    license: Optional[str] = None
    prefixes: Union[dict, "Prefix"] = empty_dict()
    default_curi_maps: List[str] = empty_list()
    default_prefix: Optional[str] = None
    default_range: Optional[Union[str, DefinitionName]] = None
    subsets: Dict[Union[str, SubsetDefinitionName], Union[dict, "SubsetDefinition"]] = empty_dict()
    types: Dict[Union[str, TypeDefinitionName], Union[dict, "TypeDefinition"]] = empty_dict()
    slots: Dict[Union[str, SlotDefinitionName], Union[dict, "SlotDefinition"]] = empty_dict()
    classes: Dict[Union[str, ClassDefinitionName], Union[dict, "ClassDefinition"]] = empty_dict()
    metamodel_version: Optional[str] = None
    source_file: Optional[str] = None
    source_file_date: Optional[Union[str, XSDDate]] = None
    source_file_size: Optional[int] = None
    generation_date: Optional[Union[str, XSDDate]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name and not isinstance(self.name, SchemaDefinitionName):
            self.name = SchemaDefinitionName(self.name)
        if self.id and not isinstance(self.id, URIorCURIE):
            self.id = URIorCURIE(self.id)
        self.imports = [v if isinstance(v, URIorCURIE)
                        else URIorCURIE(v) for v in self.imports]
        for k, v in self.prefixes.items():
            if not isinstance(v, Prefix):
                self.prefixes[k] = Prefix(k, v)
        if self.default_range and not isinstance(self.default_range, DefinitionName):
            self.default_range = DefinitionName(self.default_range)
        for k, v in self.subsets.items():
            if not isinstance(v, SubsetDefinition):
                self.subsets[k] = SubsetDefinition(name=k, **({} if v is None else v))
        for k, v in self.types.items():
            if not isinstance(v, TypeDefinition):
                self.types[k] = TypeDefinition(name=k, **({} if v is None else v))
        for k, v in self.slots.items():
            if not isinstance(v, SlotDefinition):
                self.slots[k] = SlotDefinition(name=k, **({} if v is None else v))
        for k, v in self.classes.items():
            if not isinstance(v, ClassDefinition):
                self.classes[k] = ClassDefinition(name=k, **({} if v is None else v))
        if self.source_file_date and not isinstance(self.source_file_date, XSDDate):
            self.source_file_date = XSDDate(self.source_file_date)
        if self.generation_date and not isinstance(self.generation_date, XSDDate):
            self.generation_date = XSDDate(self.generation_date)


@dataclass
class TypeDefinition(Element):
    """
    A data type definition.
    """

    # === element ===
    name: Union[str, TypeDefinitionName]
    description: Optional[str] = None
    aliases: List[str] = empty_list()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated: Optional[str] = None
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, SchemaDefinitionName]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()

    # === type definition ===
    typeof: Optional[Union[str, TypeDefinitionName]] = None
    base: Optional[str] = None
    uri: Optional[Union[str, URIorCURIE]] = None
    repr: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name and not isinstance(self.name, TypeDefinitionName):
            self.name = TypeDefinitionName(self.name)
        if self.typeof and not isinstance(self.typeof, TypeDefinitionName):
            self.typeof = TypeDefinitionName(self.typeof)
        if self.uri and not isinstance(self.uri, URIorCURIE):
            self.uri = URIorCURIE(self.uri)


@dataclass
class SubsetDefinition(Element):
    """
    the name and description of a subset
    """

    # === element ===
    name: Union[str, SubsetDefinitionName]
    description: Optional[str] = None
    aliases: List[str] = empty_list()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated: Optional[str] = None
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, SchemaDefinitionName]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()

    # === subset definition ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.name and not isinstance(self.name, SubsetDefinitionName):
            self.name = SubsetDefinitionName(self.name)


@dataclass
class Definition(Element):
    """
    base class for definitions
    """

    # === element ===
    name: Union[str, DefinitionName]
    description: Optional[str] = None
    aliases: List[str] = empty_list()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated: Optional[str] = None
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, SchemaDefinitionName]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()

    # === definition ===
    is_a: Optional[Union[str, DefinitionName]] = None
    abstract: Optional[Bool] = None
    local_names: List[str] = empty_list()
    mixin: Optional[Bool] = None
    mixins: List[Union[str, DefinitionName]] = empty_list()
    apply_to: List[Union[str, DefinitionName]] = empty_list()
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.is_a and not isinstance(self.is_a, DefinitionName):
            self.is_a = DefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, DefinitionName)
                       else DefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, DefinitionName)
                         else DefinitionName(v) for v in self.apply_to]
        self.values_from = [v if isinstance(v, URIorCURIE)
                            else URIorCURIE(v) for v in self.values_from]


@dataclass
class SlotDefinition(Definition):
    """
    the definition of a property or a slot
    """

    # === element ===
    name: Union[str, SlotDefinitionName]
    description: Optional[str] = None
    aliases: List[str] = empty_list()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated: Optional[str] = None
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, SchemaDefinitionName]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()

    # === definition ===
    abstract: Optional[Bool] = None
    local_names: List[str] = empty_list()
    mixin: Optional[Bool] = None
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    # === slot definition ===
    domain: Union[str, ClassDefinitionName] = None
    is_a: Optional[Union[str, SlotDefinitionName]] = None
    mixins: List[Union[str, SlotDefinitionName]] = empty_list()
    apply_to: List[Union[str, SlotDefinitionName]] = empty_list()
    range: Optional[Union[str, ElementName]] = None
    slot_uri: Optional[Union[str, URIorCURIE]] = None
    multivalued: Optional[Bool] = None
    inherited: Optional[Bool] = None
    readonly: Optional[str] = None
    ifabsent: Optional[str] = None
    required: Optional[Bool] = None
    inlined: Optional[Bool] = None
    key: Optional[Bool] = None
    identifier: Optional[Bool] = None
    alias: Optional[str] = None
    subclass_of: Optional[Union[str, URIorCURIE]] = None
    inverse: Optional[Union[str, SlotDefinitionName]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name and not isinstance(self.name, SlotDefinitionName):
            self.name = SlotDefinitionName(self.name)
        if self.is_a and not isinstance(self.is_a, SlotDefinitionName):
            self.is_a = SlotDefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, SlotDefinitionName)
                       else SlotDefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, SlotDefinitionName)
                         else SlotDefinitionName(v) for v in self.apply_to]
        if self.domain and not isinstance(self.domain, ClassDefinitionName):
            self.domain = ClassDefinitionName(self.domain)
        if self.range and not isinstance(self.range, ElementName):
            self.range = ElementName(self.range)
        if self.slot_uri and not isinstance(self.slot_uri, URIorCURIE):
            self.slot_uri = URIorCURIE(self.slot_uri)
        if self.subclass_of and not isinstance(self.subclass_of, URIorCURIE):
            self.subclass_of = URIorCURIE(self.subclass_of)
        if self.inverse and not isinstance(self.inverse, SlotDefinitionName):
            self.inverse = SlotDefinitionName(self.inverse)


@dataclass
class ClassDefinition(Definition):
    """
    the definition of a class or interface
    """

    # === element ===
    name: Union[str, ClassDefinitionName]
    description: Optional[str] = None
    aliases: List[str] = empty_list()
    mappings: List[Union[str, URIorCURIE]] = empty_list()
    deprecated: Optional[str] = None
    notes: List[str] = empty_list()
    comments: List[str] = empty_list()
    examples: List[Union[dict, "Example"]] = empty_list()
    in_subset: List[Union[str, SubsetDefinitionName]] = empty_list()
    from_schema: Optional[Union[str, SchemaDefinitionName]] = None
    imported_from: Optional[str] = None
    see_also: List[Union[str, URIorCURIE]] = empty_list()
    id_prefixes: List[Union[str, NCName]] = empty_list()

    # === definition ===
    abstract: Optional[Bool] = None
    local_names: List[str] = empty_list()
    mixin: Optional[Bool] = None
    values_from: List[Union[str, URIorCURIE]] = empty_list()

    # === class definition ===
    is_a: Optional[Union[str, ClassDefinitionName]] = None
    mixins: List[Union[str, ClassDefinitionName]] = empty_list()
    apply_to: List[Union[str, ClassDefinitionName]] = empty_list()
    slots: List[Union[str, SlotDefinitionName]] = empty_list()
    slot_usage: Dict[Union[str, SlotDefinitionName], Union[dict, SlotDefinition]] = empty_dict()
    class_uri: Optional[Union[str, URIorCURIE]] = None
    defining_slots: List[Union[str, SlotDefinitionName]] = empty_list()
    subclass_of: Optional[Union[str, URIorCURIE]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.name and not isinstance(self.name, ClassDefinitionName):
            self.name = ClassDefinitionName(self.name)
        if self.is_a and not isinstance(self.is_a, ClassDefinitionName):
            self.is_a = ClassDefinitionName(self.is_a)
        self.mixins = [v if isinstance(v, ClassDefinitionName)
                       else ClassDefinitionName(v) for v in self.mixins]
        self.apply_to = [v if isinstance(v, ClassDefinitionName)
                         else ClassDefinitionName(v) for v in self.apply_to]
        self.slots = [v if isinstance(v, SlotDefinitionName)
                      else SlotDefinitionName(v) for v in self.slots]
        for k, v in self.slot_usage.items():
            if not isinstance(v, SlotDefinition):
                self.slot_usage[k] = SlotDefinition(name=k, **({} if v is None else v))
        if self.class_uri and not isinstance(self.class_uri, URIorCURIE):
            self.class_uri = URIorCURIE(self.class_uri)
        self.defining_slots = [v if isinstance(v, SlotDefinitionName)
                               else SlotDefinitionName(v) for v in self.defining_slots]
        if self.subclass_of and not isinstance(self.subclass_of, URIorCURIE):
            self.subclass_of = URIorCURIE(self.subclass_of)


@dataclass
class Prefix(YAMLRoot):
    """
    prefix URI tuple
    """

    # === prefix ===
    local_name: Union[str, PrefixLocalName]
    prefix_uri: Union[str, URIorCURIE]

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.local_name, PrefixLocalName):
            self.local_name = PrefixLocalName(self.local_name)
        if not isinstance(self.prefix_uri, URIorCURIE):
            self.prefix_uri = URIorCURIE(self.prefix_uri)


@dataclass
class Example(YAMLRoot):
    """
    usage example and description
    """

    # === example ===
    value: Optional[str] = None
    description: Optional[str] = None
