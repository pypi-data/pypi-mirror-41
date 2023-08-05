from typing import List, Optional

import attr
from cortex_profiles.implicit.schema import implicity_generate_profile_schema_from_config
from cortex_profiles.types.schema import ProfileSchema, ProfileTagSchema, ProfileGroupSchema, ProfileAttributeSchema
from cortex_profiles.types.schema_config import SchemaConfig
from cortex_client.utils import current_cortex_cli_profile_config


class ProfileSchemaBuilder(object):

    def __init__(self, tenantId:str=None, environmentId:str="cortex/default", schemaId:Optional[str]=None):
        self.tenantId = tenantId if tenantId is not None else  current_cortex_cli_profile_config()["account"]
        self.environmentId = environmentId
        self._schema: ProfileSchema = ProfileSchema(tenantId=tenantId, environmentId=environmentId)
        if schemaId is not None:
            self._schema = attr.evolve(self._schema, id=schemaId)

    def append_schema_config(self, schema_confg:SchemaConfig) :
        self._schema:ProfileSchema = self._schema + implicity_generate_profile_schema_from_config(schema_confg, self.tenantId, self.environmentId)
        return self

    def append_tags(self, tags:List[ProfileTagSchema]):
        self._schema = attr.evolve(self._schema, tags=(self._schema.tags + tags))
        return self

    def append_groups(self, groups: List[ProfileGroupSchema]):
        # ... need to merge the tags in each group!
        self._schema = attr.evolve(self._schema, groups=(self._schema.groups + groups))
        return self

    def append_attributes(self, attributes: List[ProfileAttributeSchema]):
        self._schema = attr.evolve(self._schema, attributes=(self._schema.attributes + attributes))
        return self

    def get_schema(self) -> ProfileSchema:
        return self._schema
