from . import models
my_models = [models.Protein, models.Gene, models.Organism, models.StructureSegment]
class LegacyRouter:
    route_app_labels = {'existing_proteins'}

    def db_for_read(self, model, **hints):
        if model in my_models:
            return 'existing_proteins'
        return None

    def db_for_write(self, model, **hints):
        if model in my_models:
            return 'existing_proteins'
        return None
