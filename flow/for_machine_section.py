# Copyright (c) 2021 ralabo.jp
# This software is released under the MIT License.
# see https://opensource.org/licenses/mit-license.php
# ====================================================
from common import com, TargetDomain
from flow.flow_item import FlowItem

class FlowDependMachineSection(object):
    """
    machine_type, section_index, domain に依存する制御を行うクラス
    
    flow =  FlowDependMachineSection()
    """
    machine_types = ['ToyCar','ToyTrain','fan', 'gearbox','pump','slider','valve']
    section_indices = ['00','01','02','03','04','05']
    targets = ['source', 'target']


    def __init__(self, f_target):
        self.f_target = f_target
        pass

    class _Item(FlowItem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def items(self):
        """
        generate a tuple of (machine_type, section_index, domain)
        """
        target = '*' # ignore target
        usable_machine_types = com.param['limit']['usable_machine_types']
        for machine_type in self.machine_types:
            if usable_machine_types and machine_type not in usable_machine_types:
                continue # skip
            for section_index in self.section_indices:
                if com.mode: # dev_mode
                    if section_index not in ['00','01','02']:
                        continue # skip
                yield self._Item(machine_type, section_index, target)

    def domain(self, machine_type, section_index, target):
        target = '*' # ignore target
        return TargetDomain(machine_type, section_index, target)
