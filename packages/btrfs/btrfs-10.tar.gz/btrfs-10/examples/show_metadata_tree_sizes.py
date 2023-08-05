#!/usr/bin/python3

from collections import Counter
import btrfs
import sys

if len(sys.argv) < 2:
    print("Usage: {} <mountpoint>".format(sys.argv[0]))
    sys.exit(1)

trees = {
    btrfs.ctree.ROOT_TREE_OBJECTID: Counter(),
    btrfs.ctree.EXTENT_TREE_OBJECTID: Counter(),
    btrfs.ctree.CHUNK_TREE_OBJECTID: Counter(),
    btrfs.ctree.DEV_TREE_OBJECTID: Counter(),
    btrfs.ctree.FS_TREE_OBJECTID: Counter(),
    btrfs.ctree.CSUM_TREE_OBJECTID: Counter(),
    btrfs.ctree.QUOTA_TREE_OBJECTID: Counter(),
    btrfs.ctree.UUID_TREE_OBJECTID: Counter(),
    btrfs.ctree.FREE_SPACE_TREE_OBJECTID: Counter(),
    btrfs.ctree.DATA_RELOC_TREE_OBJECTID: Counter(),
}

tree_id_str = {
    btrfs.ctree.ROOT_TREE_OBJECTID: 'ROOT_TREE',
    btrfs.ctree.EXTENT_TREE_OBJECTID: 'EXTENT_TREE',
    btrfs.ctree.CHUNK_TREE_OBJECTID: 'CHUNK_TREE',
    btrfs.ctree.DEV_TREE_OBJECTID: 'DEV_TREE',
    btrfs.ctree.FS_TREE_OBJECTID: 'FS_TREE',
    btrfs.ctree.CSUM_TREE_OBJECTID: 'CSUM_TREE',
    btrfs.ctree.QUOTA_TREE_OBJECTID: 'QUOTA_TREE',
    btrfs.ctree.UUID_TREE_OBJECTID: 'UUID_TREE',
    btrfs.ctree.FREE_SPACE_TREE_OBJECTID: 'FREE_SPACE_TREE',
    btrfs.ctree.DATA_RELOC_TREE_OBJECTID: 'DATA_RELOC_TREE',
}


def _get_metadata_root(extent):
    if extent.refs > 1:
        return btrfs.ctree.FS_TREE_OBJECTID
    if len(extent.shared_block_refs) > 0:
        return btrfs.ctree.FS_TREE_OBJECTID
    root = extent.tree_block_refs[0].root
    if root >= btrfs.ctree.FIRST_FREE_OBJECTID and root <= btrfs.ctree.LAST_FREE_OBJECTID:
        return btrfs.ctree.FS_TREE_OBJECTID
    return root


with btrfs.FileSystem(sys.argv[1]) as fs:
    nodesize = fs.fs_info().nodesize

    for chunk in fs.chunks():
        if not chunk.type & (btrfs.BLOCK_GROUP_METADATA | btrfs.BLOCK_GROUP_SYSTEM):
            continue
        try:
            block_group = fs.block_group(chunk.vaddr, chunk.length)
        except IndexError:
            continue
        min_vaddr = block_group.vaddr
        max_vaddr = block_group.vaddr + block_group.length - 1
        for extent in fs.extents(min_vaddr, max_vaddr, load_metadata_refs=True):
            if isinstance(extent, btrfs.ctree.ExtentItem) \
                    and extent.flags & btrfs.ctree.EXTENT_FLAG_TREE_BLOCK:
                trees[_get_metadata_root(extent)][extent.tree_block_info.level] += 1
            elif isinstance(extent, btrfs.ctree.MetaDataItem):
                trees[_get_metadata_root(extent)][extent.skinny_level] += 1
            else:
                raise Exception("BUG: Expected metadata but got {}".format(extent))

    for root in sorted(trees.keys()):
        counter = trees[root]
        txt = [
            "{: <16}".format(tree_id_str[root]),
            "{: >10}".format(btrfs.utils.pretty_size(nodesize * sum(counter.values()))),
        ]
        for level in sorted(counter.keys()):
            txt.append("{}({: >6})".format(level, counter[level]))
        print(' '.join(txt))
