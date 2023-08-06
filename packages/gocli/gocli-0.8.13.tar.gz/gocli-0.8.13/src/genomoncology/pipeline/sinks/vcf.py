from cytoolz.curried import curry
from gosdk.logger import get_logger
from .base import FileSink


@curry
class VcfFileSink(FileSink):
    def __init__(self, filename):
        super().__init__(filename, insert_newlines=False)
        self.records_seen = set()
        self.count = 0

    def convert(self, unit):
        self.count += 1
        record = unit.get("__record__")

        # if record is None, return None after warning
        if record is None:
            get_logger().warn(f"Missing __record__: {unit}")
            return

        # return header as string
        if self.count == 1:
            return str(record)

        # check and add unique records
        record_id = f"{record.chrom}:{record.pos}"
        if record_id not in self.records_seen:
            self.records_seen.add(record_id)
            return str(record)
