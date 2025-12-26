## Index Optimization

- Used `keyword` fields for category and tags to enable fast filtering
- Limited shards to 1 for local single-node setup
- Disabled replicas to reduce indexing overhead
- Used explicit mappings to avoid dynamic field conflicts
