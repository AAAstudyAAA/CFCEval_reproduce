from .utils import (sanitize_html)
@property
def zones(self):
    """
    Get drop zone data, defined by the author.
    """
    # Convert zone data from old to new format if necessary
    migrator = StateMigration(self)
    migrated_zones = []
    # ---fixed---
    for zone in self.data.get('zones', []):
        result = migrator.apply_zone_migrations(zone)
        result['title'] = sanitize_html(result.get('title', ''))
        migrated_zones.append(result)
    # ---fixed---
    return migrated_zones