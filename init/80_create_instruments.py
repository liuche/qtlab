##example1 = qt.instruments.create('example1', 'example', address='GPIB::1', reset=True)
##dsgen = qt.instruments.create('dsgen', 'dummy_signal_generator')
##pos = qt.instruments.create('pos', 'dummy_positioner')
##combined = qt.instruments.create('combined', 'virtual_composite')
##combined.add_variable_scaled('magnet', example1, 'chA_output', 0.02, -0.13, units='mT')
import NI_DAQ
import Standa_USMC
Standa_USMC.detect_instruments() # Creates Standa0 and Standa1
NI_DAQ.detect_instruments() # creates NI DAQ instruments for all NI DAQs in the system
ddg = qt.instruments.create('ddg','SR_DG645',address='GPIB0::15::INSTR')
tl = qt.instruments.create('tl','ThorLabs_ITC4001',address='USB0::0x1313::0x804A::M00277475::INSTR')
verdi = qt.instruments.create('verdi','Coherent_VerdiG_USB')
xps = qt.instruments.create('xps','Newport_XPS',address='192.168.0.254')
li = qt.instruments.create('lockin','Lockin_726x',address='GPIB0::17::INSTR')
ls332 = qt.instruments.create('ls332','Lakeshore_332',address='GPIB0::18::INSTR')
fsm = qt.instruments.create('fsm','Newport_FSM')
snspd = qt.instruments.create('snspd','SSPDController',ni_ins=qt.instruments['NIDAQ6216'],resistance=200)
fm = qt.instruments.create('fm','Coherent_FieldMasterGS',address='ASRL7::INSTR')
sr400 = qt.instruments.create('sr400','SR_400',address='GPIB1::20::INSTR')
ls211 = qt.instruments.create('ls211','Lakeshore_211',address='COM8')
awg = qt.instruments.create('awg','Tektronix_AWG5014',address='GPIB0::14::INSTR')
#def __init__(self, name, ni_ins, resistance=500):

#combined.add_variable_combined('waveoffset', [{
#    'instrument': dmm1,
#    'parameter': 'ch2_output',
#    'scale': 1,
#    'offset': 0}, {
#    'instrument': dsgen,
#    'parameter': 'wave',
#    'scale': 0.5,
#    'offset': 0
#    }], format='%.04f')
