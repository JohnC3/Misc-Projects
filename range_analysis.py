from collections import deque
import math
import logging
from AssetTracking.utils.general_utils import extract_records
from AssetTracking.main import Setup

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

AVE_SIZE = 15

# TODO Move this data into the database
calibration_constants = {
    'DD5F8286EDD': -53.425, '646194C876E': -53.554, '05C3EC38CFD': -54.635,
    'A543A814AEC': -52.052, 'CDA03DC10EF': -57.105}


class TagData:
    """
    Contain data from a specific tag

    Attributes:
    tag_id:     The id of a tag
    ave_rssi:   The average rssi of the tag in receiver: rssi pairs
    rssi_val:   Deque objects for the last AVE_SIZE signals received per receiver
    """
    def __init__(self, tag_id):
        """Constructor for """
        self.tag_id = tag_id
        self.rssi_val = {}
        self.ave_rssi = {}
        self.cal_constant = calibration_constants[tag_id]
        self.dist_estimate = {}

    def add(self, rssi, receiver):
        logger.info('Adding {} of {} dbm from {}'.format(self.tag_id, rssi, receiver))

        if receiver not in self.rssi_val:
            self.rssi_val[receiver] = deque([], maxlen=AVE_SIZE)
        self.rssi_val[receiver].append(rssi)
        self.update_moving_ave(receiver)
        self.calculate_dist_estimate(receiver)

    def update_moving_ave(self, receiver):
        """
        Calculate the average rssi using the standard mean of the finite_queue

        Returns:
        the float value or None if we have 0 entries
        """

        if len(self.rssi_val[receiver]) < 1:
            self.ave_rssi[receiver] = None
        else:
            self.ave_rssi[receiver] = math.mean(self.rssi_val[receiver])

    def calculate_dist_estimate(self, receiver):
        """
        See jypyter notebook for fitting of the rssi data to this formula
        distance = a * (rssi/rssi_calibration_constant)^b + class
        a=2.59548556  b=3.28426389 c=-0.09661684
        """
        r = self.ave_rssi[receiver]/self.cal_constant
        self.dist_estimate[receiver] = 2.596 * math.pow(r, 3.284) - 0.0966

    def save_state(self):
        pass

    def load_state(self):
        pass


class TagMonitor:
    """
    Monitor the latest signals from the location tags and update the estimate
    location
    """

    def __init__(self):
        """Recover the the list of active tags or create a new one"""
        self.tags = self.recover_state()
    # Receive the Pull updates from each radio,
    # update the moving averages with the new values
    # Convert the moving average into a distance

    # Use the location of each radio plus the current distance of each tag to find
    # the region the tag is currently inside relative to radios.

    def recover_state(self):
        """Load the last set of devices from backup"""
        return {}

    def add_records(self, raw_records):
        """
        Extract the scan data from a raspberry pi and push new values into the
        correct tags.
        """
        records = extract_records(raw_records)
        logger.info(f'parsed recrods {records}')


if __name__ == "__main__":
    setup = Setup()

    logger.info('starting scan')
    raw_records = setup.data_uplink_command("python3 data_uplink.py --scan")
    logger.info('attempting to pull records from raspi')
    logger.info(type(raw_records))
    raw_records = str(raw_records)
    tm = TagMonitor()
    tm.add_records(raw_records)
