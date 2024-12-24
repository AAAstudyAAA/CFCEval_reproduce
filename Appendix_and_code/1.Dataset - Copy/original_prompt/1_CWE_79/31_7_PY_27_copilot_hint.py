from .utils import (sanitize_html)
@property
def zones(self):
    """
    Get drop zone data, defined by the author.
    """
    # Convert zone data from old to new format if necessary
    migrator = StateMigration(self)
    migrated_zones = migrator.migrate_zones()