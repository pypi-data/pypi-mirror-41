#!/usr/bin/python3

import argparse
import btrfs
import sys


class WastedSpaceError(Exception):
    pass


class FakeDevItem(object):
    def __init__(self, devid, total_bytes):
        self.devid = devid
        self.total_bytes = total_bytes
        self.bytes_used = 1


class FakeSpace(object):
    def __init__(self, flags):
        self.flags = flags
        self.total_bytes = 1
        self.used_bytes = 1


class FakeStripe(object):
    def __init__(self):
        self.devid = 1
        self.offset = 0


class FakeChunk(object):
    def __init__(self, flags):
        self.type = flags
        self.length = 1
        self.stripes = [FakeStripe()]
        self.num_stripes = 1


class FakeFileSystem(object):
    def __init__(self, device_sizes, mixed_groups, metadata_profile, data_profile):
        self._mixed_groups = mixed_groups
        self._devices = [FakeDevItem(devid+1, size)
                         for devid, size in enumerate(device_sizes)]
        self._chunks = [FakeChunk(btrfs.BLOCK_GROUP_SYSTEM | metadata_profile)]
        self._spaces = [FakeSpace(btrfs.BLOCK_GROUP_SYSTEM | metadata_profile)]
        if mixed_groups:
            mixed_type = btrfs.BLOCK_GROUP_DATA | btrfs.BLOCK_GROUP_METADATA
            self._chunks.append(FakeChunk(mixed_type | metadata_profile))
            self._spaces.append(FakeSpace(mixed_type | metadata_profile))
        else:
            self._chunks.append(FakeChunk(btrfs.BLOCK_GROUP_DATA | data_profile))
            self._chunks.append(FakeChunk(btrfs.BLOCK_GROUP_METADATA | metadata_profile))
            self._spaces.append(FakeSpace(btrfs.BLOCK_GROUP_DATA | data_profile))
            self._spaces.append(FakeSpace(btrfs.BLOCK_GROUP_METADATA | metadata_profile))

    def mixed_groups(self):
        return self._mixed_groups

    def space_info(self):
        return self._spaces

    def devices(self):
        return self._devices

    def chunks(self):
        return self._chunks


def arg_parser():
    parser = argparse.ArgumentParser(description="Calculate usable and unallocatable disk space")
    parser.add_argument(
        '-m', '--metadata',
        required=True,
        action='store',
        help="metadata profile, values like for data profile",
    )
    parser.add_argument(
        '-d', '--data',
        required=True,
        action='store',
        help="data profile, raid0, raid1, raid5, raid6, raid10, dup or single",
    )
    parser.add_argument(
        '-M', '--mixed',
        action='store_true',
        help="use mixed block groups (data and metadata profile must match)",
    )
    parser.add_argument(
        '-r', '--ratio',
        action='store',
        type=int,
        default=200,
        help="data to metadata ratio, e.g. 200, which means allocate 0.5%% for metadata",
    )
    parser.add_argument(
        'sizes',
        nargs='*',
        help="disk sizes, e.g. 2TB 500G 1TiB",
    )
    return parser


_str_to_profile_map = {
    'raid0': btrfs.BLOCK_GROUP_RAID0,
    'raid1': btrfs.BLOCK_GROUP_RAID1,
    'raid5': btrfs.BLOCK_GROUP_RAID5,
    'raid6': btrfs.BLOCK_GROUP_RAID6,
    'raid10': btrfs.BLOCK_GROUP_RAID10,
    'single': 0,
    'dup': btrfs.BLOCK_GROUP_DUP,
}


def main():
    parser = arg_parser()
    args = parser.parse_args()

    device_sizes = []
    for size in args.sizes:
        try:
            device_sizes.append(btrfs.utils.parse_pretty_size(size))
        except ValueError as e:
            raise WastedSpaceError("Invalid device size {}".format(size))
    mixed_groups = args.mixed
    try:
        metadata_profile = _str_to_profile_map[args.metadata]
    except KeyError as e:
        raise WastedSpaceError("Unknown profile {}".format(args.metadata))
    try:
        data_profile = _str_to_profile_map[args.data]
    except KeyError as e:
        raise WastedSpaceError("Unknown profile {}".format(args.data))
    if mixed_groups and metadata_profile != data_profile:
        raise WastedSpaceError(
            "When using mixed groups, metadata and data profile need to be identical.")
    fs = FakeFileSystem(device_sizes, mixed_groups, metadata_profile, data_profile)
    usage = btrfs.fs_usage.FsUsage(fs)
    print("Target metadata profile: {}".format(
        btrfs.utils.space_profile_description(metadata_profile)))
    print("Target data profile: {}".format(
        btrfs.utils.space_profile_description(data_profile)))
    print("Mixed block groups: {}".format(mixed_groups))
    print("Total raw filesystem size: {}".format(btrfs.utils.pretty_size(usage.total)))
    print("Device sizes:")
    for devid, size in enumerate(device_sizes):
        print("  Device {}: {}".format(devid+1, btrfs.utils.pretty_size(size)))
    if args.ratio is not None:
        usage.default_data_metadata_ratio = args.ratio
    print("Metadata to data ratio: 1:{}".format(usage.default_data_metadata_ratio))
    if not mixed_groups:
        print("Estimated virtual space to use for metadata: {}".format(
            btrfs.utils.pretty_size(usage.estimated_full_allocatable_virtual_metadata)))
        print("Estimated virtual space to use for data: {}".format(
            btrfs.utils.pretty_size(usage.estimated_full_allocatable_virtual_data)))
    else:
        print("Estimated virtual space to use for metadata and data: {}".format(
            btrfs.utils.pretty_size(usage.estimated_full_allocatable_virtual_mixed)))
    print("Total unallocatable raw amount: {}".format(
        btrfs.utils.pretty_size(usage.unallocatable_hard)))
    print("Unallocatable raw bytes per device:")
    for key in sorted(usage.dev_usage.keys()):
        print("  Device {}: {}".format(
            key, btrfs.utils.pretty_size(usage.dev_usage[key].unallocatable_hard)))


if __name__ == '__main__':
    try:
        main()
    except WastedSpaceError as e:
        print("Error: {0}".format(e), file=sys.stderr)
        sys.exit(1)
