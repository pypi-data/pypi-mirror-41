from metagenomi.models.modelbase import MgModel
from metagenomi.tasks.assemblystats import Assembly_stats
from metagenomi.tasks.prodigal import Prodigal
from metagenomi.tasks.mapping import Mapping
from metagenomi.tasks.jgimetadata import Jgi_metadata

from metagenomi.logger import logger


class Assembly(MgModel):
    # Possible tasks:
    # Mapping, Megahit, TODO:Prodigal
    def __init__(self, mgid, validate=True, **data):
        MgModel.__init__(self, mgid, **data)

        self.mgtype = 'assembly'
        if 'mgtype' in self.d:
            self.mgtype = self.d['mgtype']

        self.mappings = None
        if 'Mappings' in self.d:
            self.mappings = []
            for m in self.d['Mappings']:
                self.mappings.append(Mapping(self.mgid, **m))

        self.assembly_stats = None
        if 'Assembly_stats' in self.d:
            self.assembly_stats = Assembly_stats(self.mgid,
                                                 **self.d['Assembly_stats'])

        self.prodigal = None
        if 'Prodigal' in self.d:
            self.prodigal = Prodigal(self.mgid, **self.d['Prodigal'])

        self.jgi_metadata = None
        if 'JgiMetadata' in self.d:
            self.jgi_metadata = Jgi_metadata(self.mgid, **self.d['Jgi_metadata'])

        # No MgTasks are required. TODO: Except perhaps mapping?
        self.schema = {**self.schema, **{
            'Prodigal': {'type': 'dict'},
            'Assembly_stats': {'type': 'dict'},
            'Mappings': {'type': 'list'},
            'Jgi_metadata': {'type': 'dict'},
            'mgtype': {'type': 'string',
                       'allowed': ['assembly'],
                       'required': True}
            },
            'associated': {'type': 'dict',
                           'required': True,
                           'schema': {'sequencing': {
                                'type': 'list',
                                'schema': {'type': ['mgid',
                                                    'nonestring']},
                                'required': True
                                },
                            }
                        }
            }

        if validate:
            self.validate()
